
import streamlit as st
import yaml
import json
import datetime
import os

theme_mode = st.sidebar.radio("Theme", ["🌞 Light", "🌚 Dark"])
if theme_mode == "🌚 Dark":
    st.markdown("<style>body { background-color: #111111; color: #ffffff; }</style>", unsafe_allow_html=True)

with open("annex_iii_variation_codes.yaml", "r") as f:
    codes_data = yaml.safe_load(f)
    change_codes = codes_data["change_codes"]

code_options = [f'{item["code"]} – {item["description"]}' for item in change_codes]

spc_sections = [
    "1", "2", "3",
    "4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7", "4.8", "4.9",
    "5.1", "5.2", "5.3",
    "6.1", "6.2", "6.3", "6.4", "6.5", "6.6",
    "7", "8", "9", "10"
]

pl_data = {f"PL 10000/{i:04}": f"Product {i}" for i in range(1, 101)}

st.set_page_config(page_title="Agent A – Intake Form", layout="centered")
st.title("🧾 Agent A – Variation Submission Intake Form")

with st.form("intake_form", clear_on_submit=False):
    st.subheader("1️⃣ Product Information")
    col1, col2 = st.columns(2)
    with col1:
        pl_number = st.selectbox("Select PL Number", list(pl_data.keys()), key="pl_number")
    with col2:
        if "product_name" not in st.session_state or st.session_state.get("pl_number"):
            st.session_state.product_name = pl_data[pl_number]
        product_name = st.text_input("Product Name", value=st.session_state.product_name, key="product_name")

    variation_type = st.radio("Select Variation Type", ["Type IA", "Type IB", "Type II"], horizontal=True)

    st.markdown("---")
    st.subheader("2️⃣ Scope of Change")
    selected_change_codes = st.multiselect("Change Code(s)", code_options)
    selected_spc_sections = st.multiselect("SPC Sections Updated", spc_sections)
    summary = st.text_area("Brief Summary of Change")
    invoice_id = st.text_input("Invoice Tracking Number (optional)")

    st.markdown("---")
    st.subheader("3️⃣ Upload Optional Supporting Docs")
    uploaded_other = st.file_uploader("Upload Other Documents", type=["pdf", "doc"], accept_multiple_files=True)

    submitted = st.form_submit_button("Submit Request")
    if submitted:
        data = {
            "PL Number": pl_number,
            "Product Name": product_name,
            "Variation Type": variation_type,
            "Change Codes": selected_change_codes,
            "SPC Sections": selected_spc_sections,
            "Summary": summary,
            "Invoice Number": invoice_id,
            "Submitted": str(datetime.datetime.now())
        }

        os.makedirs("submissions", exist_ok=True)
        filename = f"submissions/{pl_number.replace('/', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        st.success("✅ Submission saved.")
        st.markdown("### 🔍 Submission Preview")
        st.json(data)
