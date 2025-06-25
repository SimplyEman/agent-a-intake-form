import streamlit as st
from fpdf import FPDF
import os

def stage2_generate_ectd():
    st.subheader("Generate eCTD Structure")

    data = st.session_state.get("intake_data")
    if not data:
        st.warning("Please complete Stage 1 first.")
        return

    st.write("Generating folder for:")
    st.json(data)

    base_dir = f"{data['pl_number']}_eCTD"
    os.makedirs(base_dir, exist_ok=True)
    with open(f"{base_dir}/eAF.txt", "w") as f:
        f.write("eAF placeholder")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"To: MHRA

Subject: {data['summary']}

PL: {data['pl_number']}")
    pdf.output(f"{base_dir}/cover_letter.pdf")

    st.success(f"eCTD folder created: {base_dir}")
