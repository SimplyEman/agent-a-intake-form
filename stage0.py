import streamlit as st

def stage0_intro():
    st.header("📩 Step 0: Intake via Email (Drag & Drop)")
    uploaded_file = st.file_uploader("Drop your .msg or .txt email here", type=["msg", "txt"])
    if uploaded_file:
        email_text = uploaded_file.read().decode("utf-8", errors="ignore")
        st.text_area("Extracted Email Text", email_text, height=300)