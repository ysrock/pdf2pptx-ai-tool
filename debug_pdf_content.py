import pdfplumber

def check_pdf_content(pdf_path):
    print(f"Checking PDF: {pdf_path}")
    try:
        with pdfplumber.open(pdf_path) as pdf:
            if len(pdf.pages) == 0:
                print("PDF has no pages.")
                return

            print(f"Total pages: {len(pdf.pages)}")
            
            for i, page in enumerate(pdf.pages[:3]): # Check first 3 pages
                print(f"--- Page {i+1} ---")
                text = page.extract_text()
                words = page.extract_words()
                
                print(f"Extracted Text Length: {len(text) if text else 0}")
                print(f"Extracted Words Count: {len(words)}")
                
                if text:
                    print(f"Sample Text: {text[:200]}...") # Show first 200 chars
                else:
                    print("No text extracted. This might be a scanned PDF (image-based).")
                    
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    check_pdf_content("Medical_City_Global_Ascent_Strategy.pdf")
