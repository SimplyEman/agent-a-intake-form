
import streamlit as st
from fpdf import FPDF
import os

def generate_ectd_package():
    st.subheader("Step 2: Generate eCTD Folder")
    if st.button("Create eCTD Package"):
        os.makedirs("output/m1.0", exist_ok=True)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        scope = st.session_state.get("scope", "To register a variation.")
        pdf.multi_cell(0, 10, f"To: MHRA\n\nSubject: Cover Letter\n\n{scope}")
        pdf.output("output/m1.0/cover_letter.pdf")
        st.success("Cover letter generated in output/m1.0/")
