
import extract_msg
import os
import csv
import yaml

def load_msg_as_text(uploaded_file):
    with open("/tmp/temp_email.msg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    msg = extract_msg.Message("/tmp/temp_email.msg")
    return msg.body

def get_product_name():
    # Simple demo map of PL numbers to product names
    return {f"PL1000{i}": f"Product {i}" for i in range(1, 101)}

def get_change_codes():
    with open("data/change_codes.txt") as f:
        return [line.strip() for line in f if line.strip()]

def get_fee_type(change_codes):
    # Dummy logic to return a fixed fee type for now
    return "Type IA" if any("A" in c for c in change_codes) else "Type IB"
