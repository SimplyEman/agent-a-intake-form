import os

def get_change_codes():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "data", "change_codes.txt")
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]