
import streamlit as st
import os
import re
from fpdf import FPDF
from datetime import date
from dotenv import load_dotenv
import openai

st.set_page_config(layout="wide", page_title="Agent A – LLM Intake Assistant")

# Load OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("📥 Agent A – Email to eCTD Intake + Cover Letter")

# Upload section
st.header("Step 1: Upload Email")
email_file = st.file_uploader("Drop a .txt version of the email", type=["txt"])

def extract_summary_from_llm(email_text):
    prompt = f"""Extract a formal regulatory scope statement from the email below, suitable for use in a cover letter to the MHRA. Focus only on the variation change being made, SPC sections involved, and reason for the change. Keep it brief, one paragraph.

EMAIL:
{email_text}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"[Error generating summary: {e}]"

def parse_email(text):
    result = {
        "PL Number": None,
        "Variation Type": None,
        "Change Codes": [],
        "SPC Sections": [],
        "Summary": ""
    }

    pl_match = re.search(r"PL\s?\d{5}/\d{4}", text)
    if pl_match:
        result["PL Number"] = pl_match.group()

    if "Type I" in text:
        result["Variation Type"] = "Type I"
    elif "Type II" in text:
        result["Variation Type"] = "Type II"
    elif "Type IB" in text:
        result["Variation Type"] = "Type IB"
    elif "Type IA" in text:
        result["Variation Type"] = "Type IA"

    code_matches = re.findall(r"[A-Z]\.[A-Z]+\.[a-z0-9.]+", text)
    result["Change Codes"] = list(set(code_matches))

    spc_matches = re.findall(r"SPC sections? ([\d., and]+)", text)
    if spc_matches:
        sections = re.findall(r"[\d.]+", spc_matches[0])
        result["SPC Sections"] = sections

    result["Summary"] = extract_summary_from_llm(text)
    return result

parsed_data = {}

if email_file:
    raw_email = email_file.read().decode("utf-8", errors="ignore")
    parsed_data = parse_email(raw_email)

    st.success("Parsed successfully.")
    st.write(parsed_data)

    st.header("Step 2: Confirm/Adjust Intake Info")
    pl_number = st.text_input("PL Number", value=parsed_data.get("PL Number", ""))
    variation_type = st.text_input("Variation Type", value=parsed_data.get("Variation Type", ""))
    change_codes = st.text_input("Change Codes", value=", ".join(parsed_data.get("Change Codes", [])))
    spc_sections = st.text_input("SPC Sections", value=", ".join(parsed_data.get("SPC Sections", [])))
    summary_scope = st.text_area("Summary / Scope", value=parsed_data.get("Summary", ""), height=120)

    st.header("Step 3: Generate Cover Letter")
    today = date.today().strftime("%d %B %Y")

    cover_letter = f"""{today}

To: Medicines and Healthcare products Regulatory Agency (MHRA)

Subject: Variation Submission – {pl_number}

Dear Sir/Madam,

Please find enclosed a submission for a {variation_type} variation to product licence {pl_number}, classified under change code(s): {change_codes}.

This variation involves updates to SPC sections: {spc_sections}. The scope of the change is as follows:

{summary_scope}

All required documentation has been included.

Yours faithfully,

Regulatory Affairs Team
"""

    cover_letter = st.text_area("Edit Cover Letter Below", value=cover_letter, height=300)

    if st.button("Export to eCTD Folder (as PDF)"):
        folder_path = os.path.join(os.getcwd(), "output_ectd", "m1.0")
        os.makedirs(folder_path, exist_ok=True)
        pdf_path = os.path.join(folder_path, "cover_letter.pdf")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)
        for line in cover_letter.split("\n"):
            pdf.multi_cell(0, 10, line)
        pdf.output(pdf_path)

        st.success(f"Cover letter exported to: {pdf_path}")
        st.balloons()
