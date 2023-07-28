import pytesseract
from PIL import Image

# Open the image file
image = Image.open('Screenshot_1.png')

# Convert the image to grayscale
image = image.convert('L')

# Use pytesseract to recognize text in the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)