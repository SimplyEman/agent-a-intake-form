
def get_product_name(pl_number):
    pl_dict = {
        "PL00001/0001": "Product A",
        "PL00002/0002": "Product B",
        "PL00003/0003": "Product C",
        # Add more mappings here as needed
    }
    return pl_dict.get(pl_number, "Unknown Product")
