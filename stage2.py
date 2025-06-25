
import streamlit as st
from fpdf import FPDF

def stage2_generate_cover():
    st.header("📄 Step 3: Cover Letter Generator")

    if "scope_summary" not in st.session_state:
        st.warning("Please complete the intake form first.")
        return

    cover_pdf = FPDF()
    cover_pdf.add_page()
    cover_pdf.set_font("Arial", size=12)

    lines = [
        "To: MHRA",
        "Subject: Variation Submission",
        "",
        "Dear Sir/Madam,",
        "",
        st.session_state["scope_summary"],
        "",
        "Please find the attached eCTD submission package.",
        "",
        "Kind regards,",
        "Regulatory Affairs Officer"
    ]

    for line in lines:
        cover_pdf.multi_cell(0, 10, line)

    pdf_path = "/mnt/data/cover_letter.pdf"
    cover_pdf.output(pdf_path)
    st.success("Cover letter generated.")
    with open(pdf_path, "rb") as file:
        st.download_button("📄 Download Cover Letter PDF", file, file_name="cover_letter.pdf")
