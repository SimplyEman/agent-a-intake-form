import streamlit as st

st.set_page_config(page_title="Agent A Intake Form", layout="centered")

st.title("Agent A – eCTD Variation Intake")
st.markdown("📋 Submit variation details for automated eCTD prep")

# Simple form UI
with st.form("variation_form"):
    pl_number = st.text_input("PL Number", placeholder="PL 12345/0001")
    product_name = st.text_input("Product Name", placeholder="Auto-filled...")
    variation_code = st.text_input("Change Code(s)", placeholder="e.g. A.2.b, B.I.z")
    scope = st.text_area("Scope / Summary of Change")
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success("Variation captured successfully!")
