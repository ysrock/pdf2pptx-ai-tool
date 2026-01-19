import pdfplumber
import numpy as np
from rapidocr_onnxruntime import RapidOCR
import sys

def test_ocr(pdf_path, resolution=250):
    print(f"Testing OCR on Page 1 with Resolution={resolution} DPI...")
    
    ocr_engine = RapidOCR()
    
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[0]
        img_obj = page.to_image(resolution=resolution)
        img_np = np.array(img_obj.original)
        
        result, _ = ocr_engine(img_np)
        
        print("\n--- Detection Results ---")
        if result:
            for i, line in enumerate(result):
                print(f"[{i}] Conf: {line[2]:.2f} | Text: {line[1]}")
        else:
            print("No text detected.")

if __name__ == "__main__":
    pdf = "Medical_City_Global_Ascent_Strategy.pdf"
    if len(sys.argv) > 1:
        pdf = sys.argv[1]
    test_ocr(pdf)
