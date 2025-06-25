
import streamlit as st
import os
from cover_letter_generator import generate_cover_letter

def stage2_output():
    st.header("📁 Step 2: Generate eCTD Documents")

    intake = st.session_state.get("intake", {})
    if not intake:
        st.warning("Please complete Stage 1 first.")
        return

    st.markdown("### Scope Preview")
    st.code(intake['scope'])

    # Generate button
    if st.button("📄 Generate Cover Letter"):
        pdf_path = generate_cover_letter(intake['scope'])
        st.success("Cover letter generated!")
        with open(pdf_path, "rb") as f:
            st.download_button("⬇️ Download Cover Letter PDF", f, file_name="cover_letter.pdf")

    # Placeholder for folder creation
    st.markdown("✅ eCTD folder generation (Coming soon)")
