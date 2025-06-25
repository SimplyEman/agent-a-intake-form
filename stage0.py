
import streamlit as st

def stage0_email_intake():
    st.header("📥 Step 1: Intake Email")
    st.write("Drag and drop the email (.txt format) below. The AI will extract details.")

    uploaded_file = st.file_uploader("Upload Email File", type=["txt"])

    if uploaded_file is not None:
        content = uploaded_file.read().decode("utf-8")
        st.session_state["email_content"] = content
        st.success("Email content uploaded.")
