
import streamlit as st
import os
from pathlib import Path
from email_parser import parse_email_scope
from utils import load_pl_data, load_change_codes, autofill_product_info
from cover_letter_generator import generate_cover_letter

# Stage 0 – Email Intake
st.title("Agent A – eCTD Submission Assistant")

st.header("📩 Step 0 – Intake via Email")
uploaded_email = st.file_uploader("Drag and drop email (.txt)", type=["txt"])
parsed_scope = ""

if uploaded_email:
    email_text = uploaded_email.read().decode("utf-8")
    parsed_scope = parse_email_scope(email_text)
    st.success("Scope extracted:")
    st.markdown(f"> {parsed_scope}")

# Continue to Stage 1 below (placeholder UI)
st.header("📝 Step 1 – Intake Form")
st.info("Stage 1 and 2 appear below in the original app sections...")
