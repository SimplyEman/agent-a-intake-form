
import streamlit as st
import re
from datetime import date
from fpdf import FPDF
import os

st.set_page_config(layout="wide", page_title="Agent A – Intake + Cover Letter Generator")

st.title("📥 Agent A – MHRA Variation Intake Assistant")

# Email Upload
st.header("Step 1: Upload Email")
email_file = st.file_uploader("Drop a .txt file with the variation request", type=["txt"])

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

    # Smart summary for cover letter
    summary_sentences = [s.strip() for s in text.split(".") if "variation" in s.lower() or "change" in s.lower()]
    result["Summary"] = summary_sentences[0] if summary_sentences else "To register a variation as described."

    return result

parsed_data = {}

if email_file:
    raw_email = email_file.read().decode("utf-8", errors="ignore")
    parsed_data = parse_email(raw_email)

    st.success("Parsed successfully.")
    st.write(parsed_data)

    # Form Fields
    st.header("Step 2: Confirm/Adjust Intake Info")
    pl_number = st.text_input("PL Number", value=parsed_data.get("PL Number", ""))
    variation_type = st.text_input("Variation Type", value=parsed_data.get("Variation Type", ""))
    change_codes = st.text_input("Change Codes (comma separated)", value=", ".join(parsed_data.get("Change Codes", [])))
    spc_sections = st.text_input("SPC Sections (comma separated)", value=", ".join(parsed_data.get("SPC Sections", [])))
    summary_scope = st.text_area("Summary / Scope", value=parsed_data.get("Summary", ""), height=100)

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
