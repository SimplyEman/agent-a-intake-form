
import streamlit as st
import json
import datetime
import os

CODES_FILE = "learned_codes.json"
DEFAULT_CODES = [
    "A.2.b – Change in the name of the medicinal product",
    "B.I.z – Other changes to active substance",
    "B.III.1 – Shelf life extension",
    "C.I.z – Other changes to SmPC",
    "CEP Update – Certificate of Suitability update"
]

# Load or initialize learned change codes
if os.path.exists(CODES_FILE):
    with open(CODES_FILE, "r") as f:
        learned_codes = json.load(f)
else:
    learned_codes = DEFAULT_CODES

spc_sections = [
    "1", "2", "3",
    "4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "4.8", "4.9",
    "5.1", "5.2", "5.3",
    "6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7",
    "7", "8", "9", "10"
]

pl_data = {f"PL 10000/{i:04}": f"Product {i}" for i in range(1, 101)}

st.set_page_config(page_title="Agent A – Reactive Intake", layout="centered")
st.title("🧾 Agent A – Variation Submission Intake Form")

with st.sidebar:
    theme_mode = st.radio("Theme", ["🌞 Light Mode", "🌚 Dark Mode"])
    if theme_mode == "🌚 Dark Mode":
        st.markdown("""
        <style>
        .main, .css-18e3th9, .block-container {
            background-color: #1e1e1e;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

# OUTSIDE form block – reactive product name logic
pl_number = st.selectbox("Select PL Number", list(pl_data.keys()), key="pl_number")
if "product_name" not in st.session_state:
    st.session_state.product_name = pl_data.get(pl_number, "")
if pl_number != st.session_state.get("last_pl", ""):
    st.session_state.product_name = pl_data.get(pl_number, "")
    st.session_state.last_pl = pl_number
product_name = st.text_input("Product Name", key="product_name")

# Main form
with st.form("intake_form", clear_on_submit=False):
    variation_type = st.radio("Select Variation Type", ["Type IA", "Type IB", "Type II"], horizontal=True)

    st.markdown("---")
    st.subheader("2️⃣ Scope of Change")

    change_codes_input = st.text_area("Add New Change Codes (optional, one per line)")
    new_codes = [code.strip() for code in change_codes_input.strip().split("\n") if code.strip()]
    for code in new_codes:
        if code not in learned_codes:
            learned_codes.append(code)

    selected_codes = st.multiselect("Select Change Code(s)", learned_codes, default=new_codes)
    selected_spc_sections = st.multiselect("SPC Sections Updated", spc_sections)
    summary = st.text_area("Brief Summary of Change")
    invoice_id = st.text_input("Invoice Tracking Number (optional)")

    st.markdown("---")
    st.subheader("3️⃣ Upload Supporting Documents")
    uploaded_other = st.file_uploader("Upload Optional Supporting Documents", type=["pdf", "doc"], accept_multiple_files=True)

    submitted = st.form_submit_button("Submit Request")

    if submitted:
        data = {
            "PL Number": pl_number,
            "Product Name": st.session_state.product_name,
            "Variation Type": variation_type,
            "Change Codes": selected_codes,
            "SPC Sections": selected_spc_sections,
            "Summary": summary,
            "Invoice Number": invoice_id,
            "Submitted": str(datetime.datetime.now())
        }

        # Save updated code list
        with open(CODES_FILE, "w") as f:
            json.dump(learned_codes, f, indent=4)

        os.makedirs("submissions", exist_ok=True)
        filename = f"submissions/{pl_number.replace('/', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        st.success("✅ Submission saved and codes updated.")
        st.markdown("### 🔍 Submission Preview")
        st.json(data)
