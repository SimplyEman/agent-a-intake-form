
import streamlit as st
import subprocess
from pathlib import Path

st.set_page_config(layout="wide", page_title="Agent A – Offline LLM Scope Summariser")

st.title("📥 Agent A – Offline Scope Generator")

st.info("This offline version uses llama-cpp-python to run a local Mistral model in GGUF format.")

# User uploads email in .txt format
uploaded_file = st.file_uploader("Drop an email in .txt format", type=["txt"])

model_path = st.text_input("🔍 Path to Mistral .gguf model", value="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf")

if uploaded_file and model_path:
    text = uploaded_file.read().decode("utf-8", errors="ignore")

    # Build prompt
    prompt = f"""[INST]Extract a formal MHRA-style scope summary from the email below. Focus on the type of change, relevant SPC sections, and the purpose of the variation. Make it one formal paragraph.

EMAIL:
{text}[/INST]"""

    # Save prompt to temporary input.txt
    with open("input.txt", "w") as f:
        f.write(prompt)

    st.write("Running offline model...")
    output = subprocess.getoutput(f'./main -m {model_path} -p "{prompt}" -n 512')

    # Display summary
    st.subheader("🧾 Scope Summary Output")
    st.code(output, language="markdown")
    st.success("Generated offline using Mistral")

st.markdown("---")
st.caption("To run this, you must download llama.cpp and a .gguf model into a local 'models' folder.")
