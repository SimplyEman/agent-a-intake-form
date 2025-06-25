
import streamlit as st
from stage0 import email_intake
from stage1 import stage1_form
from stage2 import generate_ectd_package

st.set_page_config(page_title="Agent A: SubmissionPrep", layout="wide")

st.title("Agent A: SubmissionPrep - MHRA eCTD Assistant")

tabs = st.tabs(["📥 Step 0: Email Intake", "📄 Step 1: Request Form", "📁 Step 2: eCTD Packaging"])

with tabs[0]:
    email_intake()

with tabs[1]:
    stage1_form()

with tabs[2]:
    generate_ectd_package()
