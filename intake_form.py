import streamlit as st
import datetime
import json
import os

# Load dummy PL numbers
pl_data = {f"PL 10000/{i:04}": f"Product {i}" for i in range(1, 101)}

st.title("🧾 Agent A – Variation Submission Intake Form")

pl_number = st.selectbox("Select PL Number", list(pl_data.keys()))
product_name = st.text_input("Product Name", pl_data[pl_number])

variation_type = st.selectbox("Variation Type", ["Type IA", "Type IB", "Type II"])

change_codes = st.multiselect("Change Code(s)", [
    "B.I.a.1", "B.II.b.2", "C.I.z", "A.II.2", "C.I.11"
])

summary = st.text_area("Brief Summary of Change")

spc_sections = st.multiselect("SPC Sections Updated", ["4.1", "4.2", "4.3", "5.1", "6.6", "Other"])

submission_route = st.radio("Submission Route", ["MHRA Portal", "CESP"])

invoice_id = st.text_input("Invoice Tracking Number (optional)")

uploaded_files = st.file_uploader("Upload Initial Draft Docs (PDF/DOC)", accept_multiple_files=True)

if st.button("Submit Request"):
    data = {
        "PL Number": pl_number,
        "Product Name": product_name,
        "Variation Type": variation_type,
        "Change Codes": change_codes,
        "Summary": summary,
        "SPC Sections": spc_sections,
        "Route": submission_route,
        "Invoice Number": invoice_id,
        "Submitted": str(datetime.datetime.now())
    }

    os.makedirs("submissions", exist_ok=True)
    filename = f"submissions/{pl_number.replace('/', '_')}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    st.success("✅ Submission saved.")