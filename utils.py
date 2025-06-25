
def get_product_name(pl_number):
    demo = {f"PL{str(i).zfill(5)}/{str(i).zfill(4)}": f"Product {i}" for i in range(1, 101)}
    return demo.get(pl_number, "Unknown Product")

def get_fee_type(change_codes):
    if any("A" in code for code in change_codes):
        return "Type IA"
    elif any("B" in code for code in change_codes):
        return "Type IB"
    elif any("C" in code for code in change_codes):
        return "Type II"
    return "Unknown"

def get_change_codes():
    return [f"A.{i}" for i in range(1, 101)] + [f"B.I.z.{i}" for i in range(1, 21)] + [f"C.{i}" for i in range(1, 20)]
