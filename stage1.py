
import streamlit as st

def stage1_form():
    st.subheader("Step 1: Variation Request Form")
    pl_number = st.selectbox("Select PL Number", [f"PL 1000/000{i}" for i in range(1, 6)])
    product_name = f"Product for {pl_number}"
    st.text_input("Product Name", product_name)
    change_code = st.selectbox("Change Code", ["A.2.b - Shelf-life extension", "B.I.z - Other quality change"])
    spc_sections = st.multiselect("SPC Sections Affected", [f"Section {i}" for i in range(1, 11)])
    if st.button("Generate Scope Summary"):
        st.session_state["scope"] = f"To register a variation under {change_code} affecting {', '.join(spc_sections)}."
