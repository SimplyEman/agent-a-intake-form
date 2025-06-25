import streamlit as st
from stage0 import stage0_intro
from stage1 import stage1_form
from stage2 import stage2_generate_files

st.set_page_config(page_title="Agent A - eCTD Submission Helper", layout="wide")

stage = st.sidebar.radio("Choose Stage", ["Stage 0: Email Intake", "Stage 1: Intake Form", "Stage 2: Folder & File Prep"])

if stage == "Stage 0: Email Intake":
    stage0_intro()

elif stage == "Stage 1: Intake Form":
    stage1_form()

elif stage == "Stage 2: Folder & File Prep":
    stage2_generate_files()