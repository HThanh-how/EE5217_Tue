import fitz
import os

pdf_path = 'd:/Phd/EE5217_Tue/refs/3-Digital System Test and Testable Design_ Using HDL Models and Architectures.pdf'
out_dir = 'd:/Phd/EE5217_Tue/images/raw_extracted'
os.makedirs(out_dir, exist_ok=True)

# Chapter 7 is approximately pages 212 to 260. Let's extract all images in this range.
doc = fitz.open(pdf_path)
page_start = 210
page_end = 265

img_count = 0
for page_num in range(page_start, page_end):
    page = doc.load_page(page_num)
    images = page.get_images(full=True)
    for img_idx, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        # Save image with page number and index
        image_name = f"page{page_num+1}_img{img_idx}.{image_ext}"
        filepath = os.path.join(out_dir, image_name)
        with open(filepath, "wb") as f:
            f.write(image_bytes)
        img_count += 1

print(f"Extracted {img_count} raw images from pages {page_start+1} to {page_end}.")
