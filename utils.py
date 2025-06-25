
import csv

def load_pl_data(filepath="pl_product_map.csv"):
    pl_map = {}
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pl_map[row["PL Number"]] = row["Product Name"]
    return pl_map

def load_change_codes(filepath="change_codes.csv"):
    with open(filepath) as f:
        return [line.strip() for line in f if line.strip()]

def autofill_product_info(pl_number, pl_map):
    return pl_map.get(pl_number, "")
