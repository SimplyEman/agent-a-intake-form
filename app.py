
import streamlit as st

st.set_page_config(layout="wide", page_title="Agent A - MHRA Variation Intake")

st.title("Agent A – MHRA Variation Submission Assistant")

st.markdown("## Step 1: Upload Email Request")
email_file = st.file_uploader("Drag & drop an email file (.txt, .eml, or .msg)", type=["txt", "eml", "msg"])

if email_file:
    email_text = email_file.read().decode("utf-8", errors="ignore")
    st.markdown("### Extracted Email Content:")
    st.text_area("Raw Email Text", email_text, height=200)

    # Placeholder for LLM parser
    if st.button("Run LLM Parser"):
        st.success("LLM would extract PL number, change codes, SPC sections, and summary here.")
        st.info("Example: PL 13579/0042 — Update shelf life from 18 to 24 months (SPC: 4.2, 5.1, 6.3)")

st.markdown("---")
st.markdown("## Step 2: Prepare eCTD Folder")
if st.button("Generate eCTD Folder Structure"):
    st.success("Folder structure for eCTD created (simulated here).")
    st.info("Generated: m1.0, m1.2, m3p33, m3p34 folders with placement logic.")
