import os
import extract_msg

# Static map of PL numbers to product names
PRODUCT_MAP = {
    f"PL 1000/{1000+i}": f"Product {i+1}" for i in range(100)
}

# Static map of change codes to fee types
FEE_TYPE_MAP = {
    "Change Code 1": "Minor",
    "Change Code 2": "Major",
    "Change Code 3": "Grouping",
    "Change Code 4": "Worksharing"
}

def get_change_codes():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "data", "change_codes.txt")
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def load_msg_as_text(msg_file):
    msg = extract_msg.Message(msg_file)
    msg_message = msg.body
    attachments = msg.attachments
    return msg_message, attachments

def get_product_name(pl_number):
    return PRODUCT_MAP.get(pl_number, "")

def get_fee_type(change_code):
    return FEE_TYPE_MAP.get(change_code, "Unknown")