
import os
import shutil

def generate_ectd_folders_from_intake(intake_data):
    base_path = "stage_2_output/PL00000_0000/0001/"
    folders = [
        "m1/m1.0", "m1/m1.2", "m1/m1.3.1", "m1/m1.8.2",
        "m3/m3p/m3p3/m3p33", "m3/m3p/m3p4", "m3/m3p/m3p5", "m3/m3p/m3p3/m3p34"
    ]
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    # Simulate file generation
    with open(os.path.join(base_path, "m1/m1.0/cover_letter.pdf"), "w") as f:
        f.write("Cover letter generated from intake: " + intake_data.get("summary", "No summary provided"))

    with open(os.path.join(base_path, "m1/m1.2/eaf_form.pdf"), "w") as f:
        f.write("eAF generated from intake: " + intake_data.get("product_name", "No product name provided"))

    print("✅ eCTD folders and files have been generated.")

# Example simulated data from intake form
if __name__ == "__main__":
    test_data = {
        "summary": "To update shelf life based on stability data",
        "product_name": "Paracetamol 500mg Tablets"
    }
    generate_ectd_folders_from_intake(test_data)
