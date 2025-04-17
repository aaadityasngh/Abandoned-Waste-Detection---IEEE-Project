from fpdf import FPDF
import json
import os
from datetime import datetime

def generate_pdf(log_path, output_path):
    if not os.path.exists(log_path):
        return False

    with open(log_path) as f:
        logs = json.load(f)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_title("Abandoned Waste Detection Report")
    pdf.cell(200, 10, txt="Abandoned Waste Detection Summary", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=10)

    for idx, entry in enumerate(logs[:50], 1):
        line = f"{idx}. Frame {entry['frame']} - {entry['detected_items']} at {datetime.fromtimestamp(entry['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}"
        pdf.multi_cell(0, 8, txt=line)

    try:
        pdf.output(output_path)
        return True
    except:
        return False
