import os
from pdfminer.high_level import extract_text

input_folder = "pdfs"
output_folder = "markdowns"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(input_folder, filename)
        text = extract_text(pdf_path)
        md_filename = filename.replace(".pdf", ".md")
        md_path = os.path.join(output_folder, md_filename)
        with open(md_path, "w", encoding="utf-8") as md_file:
            md_file.write(text)
        print(f"Converted: {filename} → {md_filename}")
