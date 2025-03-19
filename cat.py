from PIL import Image

# Specify the path to your downloaded cat image
image_path = "C:\\Users\\KAVIYA\\OneDrive\\Pictures\\cat.jpg"  # Update this with the correct path

# Open the image using Pillow
img = Image.open(image_path)

# Show the image
img.show()
