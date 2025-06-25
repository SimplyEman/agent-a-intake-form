
import streamlit as st

def email_intake():
    st.subheader("Step 0: Intake Email")
    uploaded_file = st.file_uploader("Upload an email (.txt)", type=["txt"])
    if uploaded_file:
        email_text = uploaded_file.read().decode("utf-8")
        st.text_area("Parsed Email Text", email_text, height=200)
        st.session_state["email_summary"] = email_text
