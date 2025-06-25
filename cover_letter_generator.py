
from fpdf import FPDF
from datetime import datetime

def generate_cover_letter(scope_summary, output_path="cover_letter.pdf"):
    cover_pdf = FPDF()
    cover_pdf.add_page()
    cover_pdf.set_font("Arial", size=12)

    # Header
    cover_pdf.set_font("Arial", style="B", size=14)
    cover_pdf.cell(200, 10, txt="Cover Letter", ln=True, align="C")

    cover_pdf.set_font("Arial", size=12)
    cover_pdf.ln(10)
    message = f"To: MHRA\n\nSubmission Date: {datetime.today().strftime('%Y-%m-%d')}\n\n{scope_summary}"
    for line in message.split("\n"):
        cover_pdf.multi_cell(0, 10, line)

    cover_pdf.output(output_path)
    return output_path
