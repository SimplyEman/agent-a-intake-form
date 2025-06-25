import streamlit as st
import os
from fpdf import FPDF

def stage2_generate_files():
    st.header("📁 Step 2: Generate eCTD Folder + Files")

    product = st.text_input("Product Name", "Product X")
    change_summary = st.text_area("Change Summary", "To register...")

    if st.button("Generate Cover Letter PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, f"To: MHRA

Subject: {change_summary}

Regards,
RA Officer")
        os.makedirs("output", exist_ok=True)
        pdf.output("output/cover_letter.pdf")
        st.success("PDF cover letter generated in 'output/cover_letter.pdf'")