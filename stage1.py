import streamlit as st
from utils import get_product_name, get_fee_type

def stage1_form():
    st.header("📝 Step 1: Intake Form")

    pl_number = st.selectbox("Select PL Number", [f"PL{str(i).zfill(5)}/{str(i).zfill(4)}" for i in range(1, 101)])
    product_name = get_product_name(pl_number)
    st.text_input("Product Name", value=product_name, disabled=True)

    change_code = st.selectbox("Change Code", ["A.2.b", "B.I.z", "C.I.1", "D.II.1", "CEP.1", "CEP.2"])
    fee_type = get_fee_type(change_code)
    st.text_input("Fee Type", value=fee_type, disabled=True)

    st.text_area("Summary / Scope", "To register an update...")

    if st.button("Generate Submission"):
        st.success("Submission data saved. Proceed to Step 2.")