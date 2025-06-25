import streamlit as st
import pandas as pd
import os
import datetime
import zipfile
import io
from fpdf import FPDF
import extract_msg
import openai
from dotenv import load_dotenv

st.set_page_config(page_title="Agent A", page_icon="🤖", layout="wide")
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@st.cache_data
def get_mhra_codes():
    try:
        df = pd.read_csv("data/mhra_change_codes.csv")
        return df
    except FileNotFoundError:
        st.error("data/mhra_change_codes.csv not found.")
        return pd.DataFrame()

def parse_email_with_llm(content):
    if not openai.api_key:
        st.error("No OpenAI API key.")
        return None
    try:
        prompt = f'''
        Extract: PL number, Scope of Change, Suggested Change Code, SPC Sections.

        Email:
        ---
        {content}
        ---
        '''
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful RA assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"AI parser error: {e}")
        return None

class PDF(FPDF):
    def header(self): self.set_font('Arial', 'B', 12); self.cell(0, 10, 'Cover Letter', 0, 1, 'C'); self.ln(10)
    def footer(self): self.set_y(-15); self.set_font('Arial', 'I', 8); self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_cover_letter_pdf(data):
    pdf = PDF(); pdf.add_page(); pdf.set_font('Arial', '', 11)
    pdf.cell(0, 10, f"Date: {datetime.date.today().strftime('%d-%b-%Y')}", 0, 1); pdf.ln(10)
    pdf.multi_cell(0, 10, f"To: The Licensing Authority, MHRA")
    pdf.ln(5)
    pdf.multi_cell(0, 7, f"Product: {data['product_name']} (PL {data['pl_number']})")
    pdf.multi_cell(0, 7, f"Type: {data['fee_type']}")
    pdf.multi_cell(0, 7, f"Scope: {data['summary_scope']}")
    pdf.multi_cell(0, 7, f"Change Code(s): {', '.join(data['change_codes'])}")
    pdf.multi_cell(0, 7, f"SPC Sections: {', '.join(data['spc_sections'])}")
    pdf.multi_cell(0, 7, "Yours faithfully, [RA Officer]")
    return pdf.output(dest='S').encode('latin-1')

st.title("🤖 Agent A")

mhra_codes_df = get_mhra_codes()
product_db = {"PL 12345/0001": "ReguloX 10mg", "PL 54321/0002": "CardioWell 5mg"}

if 'parsed_data' not in st.session_state: st.session_state.parsed_data = {}
if 'form_data' not in st.session_state: st.session_state.form_data = None

with st.expander("📨 Stage 0: Email Intake", expanded=True):
    uploaded_file = st.file_uploader("Upload .msg or .txt", type=['msg', 'txt'])
    if uploaded_file:
        body = extract_msg.Message(uploaded_file).body if uploaded_file.name.endswith('.msg') else uploaded_file.read().decode('utf-8')
        st.text_area("Email", body, height=200)
        if st.button("Parse Email"):
            parsed = parse_email_with_llm(body)
            if parsed:
                for line in parsed.split('\n'):
                    if ':' in line:
                        k,v = line.split(':',1)
                        st.session_state.parsed_data[k.strip().lower().replace(' ','_')] = v.strip()
                st.rerun()
    if st.session_state.parsed_data.get('product_license_number_(pl)'):
        st.write(st.session_state.parsed_data)

with st.expander("🧾 Stage 1: Intake Form"):
    with st.form("form"):
        pl_options = list(product_db.keys())
        default_pl = st.session_state.parsed_data.get('product_license_number_(pl)', pl_options[0])
        pl = st.selectbox("PL", pl_options, index=pl_options.index(default_pl) if default_pl in pl_options else 0)
        name = st.text_input("Product Name", product_db.get(pl, "N/A"), disabled=True)
        codes = st.multiselect("Change Codes", mhra_codes_df['code'].tolist(),
                               default=[st.session_state.parsed_data.get('suggested_change_code', '')])
        fee = "N/A"
        if codes:
            fee = mhra_codes_df[mhra_codes_df['code'].isin(codes)]['type'].iloc[0]
        st.text_input("Fee Type", value=fee, disabled=True)
        spc = st.multiselect("SPC Sections", [str(i) for i in range(1,11)],
                             default=[st.session_state.parsed_data.get('affected_spc_sections','')])
        scope = st.text_area("Summary", value=st.session_state.parsed_data.get('scope_of_change',''))
        submit = st.form_submit_button("Lock Details")
    if submit:
        st.session_state.form_data = {
            "pl_number": pl, "product_name": name, "change_codes": codes,
            "fee_type": fee, "spc_sections": spc, "summary_scope": scope
        }
        st.success("Form complete")

with st.expander("📁 Stage 2: Generate eCTD Package"):
    if not st.session_state.form_data:
        st.warning("Please fill Stage 1 first.")
    else:
        if st.button("Generate ZIP"):
            buffer = io.BytesIO()
            seq = f"eCTD_{st.session_state.form_data['pl_number'].replace('/','-')}_{datetime.date.today():%Y%m%d}"
            with zipfile.ZipFile(buffer, 'a', zipfile.ZIP_DEFLATED) as zf:
                path1, path2 = os.path.join(seq, '0000', 'm1', 'eu', '1.0-cover-letter'), os.path.join(seq, '0000', 'm1', 'eu', '1.2-eaf')
                zf.writestr(path1+'/', ''); zf.writestr(path2+'/', '')
                zf.writestr(os.path.join(path1, 'cover-letter.pdf'), generate_cover_letter_pdf(st.session_state.form_data))
                zf.writestr(os.path.join(path2, 'eaf.txt'), "Placeholder eAF")
            st.download_button("Download ZIP", data=buffer.getvalue(), file_name=f"{seq}.zip", mime="application/zip")