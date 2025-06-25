
import streamlit as st
from utils import get_product_name, get_fee_type, get_change_codes

def stage1_form():
    st.header("📝 Step 2: Complete Intake Form")

    pl_number = st.selectbox("PL Number", [f"PL{str(i).zfill(5)}/{str(i).zfill(4)}" for i in range(1, 101)])
    product_name = get_product_name(pl_number)
    st.text_input("Product Name", value=product_name, disabled=True)

    change_codes = get_change_codes()
    selected_change_codes = st.multiselect("Select Change Codes", change_codes)

    fee_type = get_fee_type(selected_change_codes)
    st.text_input("Expected Fee Type", value=fee_type, disabled=True)

    scope = st.text_area("Scope of Submission", placeholder="Summarise the submission purpose...")

    if st.button("Generate Scope Summary"):
        st.session_state["scope_summary"] = f"This submission includes {', '.join(selected_change_codes)} for {product_name}."

    if st.button("Confirm and Proceed"):
        st.success("Form saved. Proceed to Cover Letter generation.")
