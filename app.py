
import streamlit as st
import re

st.set_page_config(layout="wide", page_title="Agent A - Email Intake with LLM Parser")

st.title("Agent A – Step 1: Drag-and-Drop Email Intake")

email_file = st.file_uploader("Drop an email (.txt) with a variation request", type=["txt"])

def parse_email(text):
    result = {
        "PL Number": None,
        "Variation Type": None,
        "Change Codes": [],
        "SPC Sections": [],
        "Summary": ""
    }

    pl_match = re.search(r"PL\s?\d{5}/\d{4}", text)
    if pl_match:
        result["PL Number"] = pl_match.group()

    if "Type I" in text:
        result["Variation Type"] = "Type I"
    elif "Type II" in text:
        result["Variation Type"] = "Type II"
    elif "Type IB" in text:
        result["Variation Type"] = "Type IB"
    elif "Type IA" in text:
        result["Variation Type"] = "Type IA"

    code_matches = re.findall(r"[A-Z]\.[A-Z]+\.[a-z0-9.]+", text)
    result["Change Codes"] = list(set(code_matches))

    spc_matches = re.findall(r"SPC sections? ([\d., and]+)", text)
    if spc_matches:
        sections = re.findall(r"[\d.]+", spc_matches[0])
        result["SPC Sections"] = sections

    summary_sentences = [s.strip() for s in text.split(".") if "variation" in s.lower()]
    result["Summary"] = summary_sentences[0] if summary_sentences else "No summary detected."

    return result

if email_file:
    raw_text = email_file.read().decode("utf-8", errors="ignore")
    st.text_area("Email Content", raw_text, height=200)
    parsed = parse_email(raw_text)

    st.markdown("### Extracted Fields")
    st.write("**PL Number:**", parsed["PL Number"])
    st.write("**Variation Type:**", parsed["Variation Type"])
    st.write("**Change Codes:**", ", ".join(parsed["Change Codes"]))
    st.write("**SPC Sections:**", ", ".join(parsed["SPC Sections"]))
    st.write("**Summary:**", parsed["Summary"])

    if st.button("Auto-Fill Form"):
        st.success("Form fields populated (simulation).")

st.markdown("---")
st.markdown("## Step 2: Prepare eCTD Folder")
if st.button("Generate eCTD Folder Structure"):
    st.success("Folder structure for eCTD created (simulated here).")
