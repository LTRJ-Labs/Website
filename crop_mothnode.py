from PIL import Image
import os

img_path = r"c:\Users\levip\Downloads\Website\img\MothNodePhoto1.jpg"

try:
    with Image.open(img_path) as img:
        width, height = img.size
        
        # Calculate 20% of width and height
        left = int(width * 0.20)
        top = int(height * 0.20)
        right = int(width * 0.80)
        bottom = int(height * 0.80)
        
        # Crop the image
        cropped_img = img.crop((left, top, right, bottom))
        
        # Save over the original file
        cropped_img.save(img_path)
        print("Cropped MothNodePhoto1 successfully.")
except Exception as e:
    print(f"Error cropping image: {e}")
