
import streamlit as st
from stage0 import stage0_email_intake
from stage1 import stage1_form
from stage2 import stage2_generate_folder

st.set_page_config(page_title="Agent A - SubmissionPrep", layout="centered")

st.title("Agent A - SubmissionPrep")

stage = st.radio("Choose Stage", ["Stage 0: Email Intake", "Stage 1: Intake Form", "Stage 2: eCTD Generator"])

if stage == "Stage 0: Email Intake":
    stage0_email_intake()
elif stage == "Stage 1: Intake Form":
    stage1_form()
elif stage == "Stage 2: eCTD Generator":
    stage2_generate_folder()
