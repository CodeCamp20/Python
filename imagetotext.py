from PIL import Image
import pytesseract

#Include tesseract exe. path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# image object
image = Image.open('image.jpg')

#Pass image object to text

text = pytesseract.image_to_string(image, lang='eng')

print(text)
