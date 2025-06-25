
import streamlit as st
import csv
from utils import get_product_name, get_change_codes, get_fee_type

def stage1_form():
    st.header("📥 Step 1: Submission Intake Form")

    # Load mapping files
    pl_map = get_product_name()
    change_codes = get_change_codes()

    # PL dropdown
    pl_number = st.selectbox("Select PL Number", list(pl_map.keys()))
    product_name = pl_map.get(pl_number, "")
    st.text_input("Product Name", value=product_name, disabled=True)

    # Change code multiselect
    selected_codes = st.multiselect("Select Change Codes", options=change_codes)

    # SPC sections
    spc_sections = [f"{i}" for i in range(1, 11)]
    selected_spc = st.multiselect("Updated SPC Sections", options=spc_sections)

    # Fee type autofill
    fee_type = get_fee_type(selected_codes)
    st.text_input("Fee Type", value=fee_type, disabled=True)

    # Summary/scope
    scope = st.text_area("Summary of Changes")

    # Confirm button
    if st.button("Confirm and Continue to Stage 2"):
        st.session_state['intake'] = {
            "pl_number": pl_number,
            "product_name": product_name,
            "change_codes": selected_codes,
            "spc_sections": selected_spc,
            "fee_type": fee_type,
            "scope": scope
        }
        st.success("Intake confirmed. Move to Step 2.")
