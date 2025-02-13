import fitz
import os

# Define input and output directories
input_folder = "pdfs"
output_folder = "output"

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

# Get the first PDF in the input folder
pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]

if not pdf_files:
    print("⚠️ No PDF files found in the 'pdfs' folder.")
    exit()

pdf_path = os.path.join(input_folder, pdf_files[0])  # Select the first PDF

# Open PDF
doc = fitz.open(pdf_path)

# Convert each page to an image
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=300)  # High resolution
    image_path = os.path.join(output_folder, f"page_{i+1}.jpg")
    pix.save(image_path)
    print(f"✅ Saved: {image_path}")

print(f"🎉 All pages from '{pdf_files[0]}' have been converted to JPGs.")
