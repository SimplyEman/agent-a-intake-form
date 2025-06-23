
import streamlit as st
import datetime
import json
import os

# Sample data
pl_data = {f"PL 10000/{i:04}": f"Product {i}" for i in range(1, 101)}
change_codes = ['A.I.1', 'A.I.2', 'A.I.3', 'A.II.1', 'A.II.2', 'A.II.3', 'A.II.4', 'B.I.a', 'B.I.b', 'B.I.c', 'B.I.d', 'B.I.e', 'B.I.f', 'B.I.g', 'B.I.z', 'B.II.a', 'B.II.b', 'B.II.c', 'B.II.d', 'B.II.e', 'C.I.1', 'C.I.2', 'C.I.3', 'C.I.4', 'C.I.z', 'C.II.1', 'C.II.2', 'C.II.3', 'C.II.4', 'C.III.1', 'C.III.2']
spc_sections = ['1', '2', '3', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.8', '4.9', '5.1', '5.2', '5.3', '6.1', '6.2', '6.3', '6.4', '6.5', '6.6', '6.7', '7', '8', '9', '10']

st.set_page_config(page_title="Agent A – Intake Form", layout="centered")

st.title("🧾 Agent A – Variation Submission Intake Form")

with st.form("intake_form", clear_on_submit=False):

    st.subheader("1️⃣ Product Information")
    col1, col2 = st.columns(2)
    with col1:
        pl_number = st.selectbox("Select PL Number", list(pl_data.keys()))
    with col2:
        product_name = st.text_input("Product Name", pl_data[pl_number])

    variation_type = st.radio("Select Variation Type", ["Type IA", "Type IB", "Type II"], horizontal=True)

    st.markdown("---")
    st.subheader("2️⃣ Scope of Change")
    selected_change_codes = st.multiselect("Change Code(s)", change_codes)
    selected_spc_sections = st.multiselect("SPC Sections Updated", spc_sections)
    summary = st.text_area("Brief Summary of Change")
    invoice_id = st.text_input("Invoice Tracking Number (optional)")

    st.markdown("---")
    st.subheader("3️⃣ Upload Supporting Documents")

    uploaded_other = st.file_uploader("Upload Optional Supporting Documents", type=["pdf", "doc"], accept_multiple_files=True)

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
