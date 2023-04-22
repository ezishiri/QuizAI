import urllib.request
import cv2
import pytesseract

def extract_text_from_image(url):
    # Download image from URL
    urllib.request.urlretrieve(url, "image.jpg")

    # Read image using OpenCV
    img = cv2.imread("image.jpg")

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to extract text from image
    text = pytesseract.image_to_string(gray)

    # Split text into lines
    lines = text.splitlines()

    # Convert lines to lowercase or uppercase if needed
    # Example: lines = [line.lower() for line in lines]

    # Return list of strings
    return lines
