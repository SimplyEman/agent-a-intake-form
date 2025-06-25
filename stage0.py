
import streamlit as st

def stage0_email_intake():
    st.subheader("Stage 0: Email Intake")
    uploaded_file = st.file_uploader("Drop an email (.txt)", type=["txt"])
    if uploaded_file:
        email_text = uploaded_file.read().decode("utf-8")
        st.session_state["autofill"] = {
            "pl_number": "PL12345/0001",
            "change_codes": ["B.I.a.1", "A.2.b"],
            "spc_sections": ["4.2", "6.3"],
            "scope_summary": "To register an update to section 4.2 based on new stability data.",
        }
        st.success("Fields extracted and pre-filled in intake form.")
