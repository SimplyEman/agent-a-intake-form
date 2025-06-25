
import streamlit as st
from stage0 import stage0_email_intake
from stage1 import stage1_form
from stage2 import stage2_generate_cover

st.set_page_config(page_title="Agent A - MHRA Submission Helper", layout="centered")

st.sidebar.title("Navigation")
stage = st.sidebar.radio("Go to:", ["Step 1: Intake Email", "Step 2: Intake Form", "Step 3: Generate Cover Letter"])

if stage == "Step 1: Intake Email":
    stage0_email_intake()
elif stage == "Step 2: Intake Form":
    stage1_form()
elif stage == "Step 3: Generate Cover Letter":
    stage2_generate_cover()
