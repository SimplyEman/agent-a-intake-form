
import streamlit as st
from email_parser import parse_email_scope
from utils import load_msg_as_text
from stage1 import stage1_form
from stage2 import stage2_output

st.set_page_config(page_title="Agent A: SubmissionPrep", layout="centered")

st.title("💊 Agent A: SubmissionPrep")

step = st.sidebar.radio("Choose Step", ["0 - Intake via Email", "1 - Intake Form", "2 - Generate eCTD Docs"])

if step == "0 - Intake via Email":
    st.header("📩 Step 0: Drag-and-Drop Email")
    uploaded_msg = st.file_uploader("Upload .msg Email File", type=["msg"])
    if uploaded_msg:
        msg_txt = load_msg_as_text(uploaded_msg)
        st.markdown("### Email Content")
        st.code(msg_txt)

        if st.button("🧠 Generate Scope from Email"):
            extracted = parse_email_scope(msg_txt)
            st.session_state["email_scope"] = extracted
            st.success("Scope generated.")
            st.text_area("Scope Output", value=extracted, height=200)

elif step == "1 - Intake Form":
    stage1_form()

elif step == "2 - Generate eCTD Docs":
    stage2_output()
