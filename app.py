
import streamlit as st
import os
from fpdf import FPDF
from integrate_stage1_stage2 import generate_ectd_folders_from_intake

st.set_page_config(page_title="Agent A – Intake Form", layout="centered")
st.title("📥 MHRA Variation Request Intake")

# Input fields
pl_number = st.selectbox("PL Number", ["PL00000/0000", "PL00001/0001"])
product_name = st.text_input("Product Name")
change_code = st.text_input("Change Code (e.g., A.2.b)")
summary = st.text_area("Summary / Scope")
fee_type = st.selectbox("Fee Type", ["Standard", "Grouped", "No Fee"])
invoice_number = st.text_input("Invoice Tracking Number")

if st.button("✅ Submit and Generate Files"):
    # Create base path
    base_path = f"stage_2_output/{pl_number.replace('/', '_')}/0001/"
    folders = [
        "m1/m1.0", "m1/m1.2", "m1/m1.3.1", "m1/m1.8.2",
        "m3/m3p/m3p3/m3p33", "m3/m3p/m3p4", "m3/m3p/m3p5", "m3/m3p/m3p3/m3p34"
    ]
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    # Save PDF: Cover Letter
    cover_pdf = FPDF()
    cover_pdf.add_page()
    cover_pdf.set_font("Arial", size=12)
    cover_pdf.multi_cell(0, 10, f"To: MHRA

Subject: Variation Submission

Summary: {summary}

Change Code: {change_code}")
    cover_pdf.output(os.path.join(base_path, "m1/m1.0/cover_letter.pdf"))

    # Save PDF: eAF
    eaf_pdf = FPDF()
    eaf_pdf.add_page()
    eaf_pdf.set_font("Arial", size=12)
    eaf_pdf.multi_cell(0, 10, f"Product Name: {product_name}
PL Number: {pl_number}
Fee Type: {fee_type}
Invoice: {invoice_number}")
    eaf_pdf.output(os.path.join(base_path, "m1/m1.2/eaf_form.pdf"))

    st.success("✅ Files generated in eCTD folder structure.")
    st.code(f"Folder: {base_path}", language="bash")

# Add theme toggle
dark_mode = st.checkbox("🌙 Dark Mode")
if dark_mode:
    st.markdown(
        "<style>body{ background-color: #111; color: #eee; }</style>",
        unsafe_allow_html=True,
    )
