import pytesseract
from pdf2image import convert_from_path

def ocr_pdf(file_path):
    try:
        pages = convert_from_path(file_path)
        text = ""
        for page in pages:
            text += pytesseract.image_to_string(page)
        return text
    except Exception as e:
        print(f"OCR Extractiomn failed. {e}")