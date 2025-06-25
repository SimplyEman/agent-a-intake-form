
import streamlit as st

def stage1_form():
    st.subheader("Stage 1: Intake Form")

    demo_pls = {f"PL10000/{i:04}": f"Product {i}" for i in range(1, 101)}
    pl_number = st.selectbox("Select PL number", list(demo_pls.keys()))
    product_name = demo_pls.get(pl_number, "")

    autofill = st.session_state.get("autofill", {})
    default_change_codes = autofill.get("change_codes", [])
    default_scope = autofill.get("scope_summary", "")
    default_spc = autofill.get("spc_sections", [])

    change_codes = st.multiselect("Select Change Codes", 
                                  ["A.2.b", "B.I.a.1", "B.I.z", "C.I.z", "D.I.a.1", "D.II.b", "D.III.z"], 
                                  default=default_change_codes)
    spc_sections = st.multiselect("Select SPC Sections", [f"{i}.{j}" if j else f"{i}" for i in range(1, 11) for j in ["", "1", "2", "3", "4", "5", "6"]], default=default_spc)
    scope_summary = st.text_area("Scope Summary", default_scope)

    fee_type = "Standard Variation Fee" if change_codes else "Not Determined"

    if st.button("Confirm Intake"):
        st.session_state["intake_data"] = {
            "pl_number": pl_number,
            "product_name": product_name,
            "change_codes": change_codes,
            "spc_sections": spc_sections,
            "scope_summary": scope_summary,
            "fee_type": fee_type
        }
        st.success("Form confirmed and data saved.")
