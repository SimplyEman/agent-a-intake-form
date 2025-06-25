def get_product_name(pl_number):
    pl_map = {f"PL{str(i).zfill(5)}/{str(i).zfill(4)}": f"Product {i}" for i in range(1, 101)}
    return pl_map.get(pl_number, "Unknown Product")

def get_fee_type(change_code):
    if "A" in change_code:
        return "Type IA"
    elif "B" in change_code:
        return "Type IB"
    elif "C" in change_code:
        return "Type II"
    elif "CEP" in change_code:
        return "CEP-related"
    else:
        return "Unknown"