import streamlit as st
import datetime
import json
import os

pl_data = {f"PL 10000/{i:04}": f"Product {i}" for i in range(1, 101)}

change_codes = ['A.I.1', 'A.I.2', 'A.I.3', 'A.II.1', 'A.II.2', 'A.II.3', 'A.II.4', 'B.I.a.1', 'B.I.a.2', 'B.I.a.3', 'B.I.b.1', 'B.I.b.2', 'B.II.a.1', 'B.II.b.1', 'B.II.b.2', 'C.I.1', 'C.I.2', 'C.I.3', 'C.I.4', 'C.I.z', 'C.II.1', 'C.II.2', 'C.II.3', 'C.II.4', 'C.III.1', 'C.III.2']
spc_sections = ['1', '2', '3', '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.7', '4.8', '4.9', '5.1', '5.2', '5.3', '6.1', '6.2', '6.3', '6.4', '6.5', '6.6', '6.7', '7', '8', '9', '10']

st.title("🧾 Agent A – Variation Submission Intake Form")

pl_number = st.selectbox("Select PL Number", list(pl_data.keys()))
product_name = st.text_input("Product Name", pl_data[pl_number])

variation_type = st.selectbox("Variation Type", ["Type IA", "Type IB", "Type II"])

selected_change_codes = st.multiselect("Change Code(s)", change_codes)

summary = st.text_area("Brief Summary of Change")

selected_spc_sections = st.multiselect("SPC Sections Updated", spc_sections)

submission_route = st.radio("Submission Route", ["MHRA Portal", "CESP"])

invoice_id = st.text_input("Invoice Tracking Number (optional)")

uploaded_files = st.file_uploader("Upload Initial Draft Docs (PDF/DOC)", accept_multiple_files=True)

if st.button("Submit Request"):
    data = {
        "PL Number": pl_number,
        "Product Name": product_name,
        "Variation Type": variation_type,
        "Change Codes": selected_change_codes,
        "Summary": summary,
        "SPC Sections": selected_spc_sections,
        "Route": submission_route,
        "Invoice Number": invoice_id,
        "Submitted": str(datetime.datetime.now())
    }

    os.makedirs("submissions", exist_ok=True)
    filename = f"submissions/{pl_number.replace('/', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    st.success("✅ Submission saved.")
