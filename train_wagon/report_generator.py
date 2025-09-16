import os
import img2pdf

def generate_report(image_paths, output_pdf):
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(image_paths))
    return output_pdf
