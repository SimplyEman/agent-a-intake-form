
import streamlit as st
import os
from fpdf import FPDF

def stage2_generate_folder():
    st.subheader("Stage 2: eCTD Folder & Cover Letter")

    data = st.session_state.get("intake_data")
    if not data:
        st.warning("Please complete Stage 1 first.")
        return

    base_dir = f"/mnt/data/eCTD_{data['pl_number'].replace('/', '_')}"
    os.makedirs(base_dir, exist_ok=True)

    # Write scope to cover letter
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Cover Letter", ln=True)
    pdf.multi_cell(0, 10, f"To: MHRA

Subject: Variation Submission

Scope: {data['scope_summary']}")
    pdf.output(f"{base_dir}/cover_letter.pdf")

    st.success(f"eCTD folder created: {base_dir}")
    st.download_button("Download Cover Letter", data=open(f"{base_dir}/cover_letter.pdf", "rb").read(), file_name="cover_letter.pdf")
