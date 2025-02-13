from PIL import Image
import os

# Define input and output directories
input_folder = "images"
output_folder = "output"
output_pdf = os.path.join(output_folder, "merged.pdf")

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

# Get list of JPG and JPEG files sorted alphabetically
image_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith((".jpg", ".jpeg"))])

# Open images and convert them to RGB
images = [Image.open(os.path.join(input_folder, img)).convert("RGB") for img in image_files]

# Save the first image as PDF and append the rest
if images:
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"✅ PDF created successfully: {output_pdf}")
else:
    print("⚠️ No JPG or JPEG images found in the 'images' folder.")
