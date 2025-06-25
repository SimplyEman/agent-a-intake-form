
import streamlit as st
from utils import get_product_name

def main():
    st.title("Agent A - Intake Form")

    pl_number = st.selectbox("Select PL Number", ["PL00001/0001", "PL00002/0002", "PL00003/0003"])
    product_name = get_product_name(pl_number)
    st.text_input("Product Name", value=product_name, disabled=True)

    if st.button("Submit"):
        st.success("Form submitted successfully!")

if __name__ == "__main__":
    main()
