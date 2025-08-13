# -*- coding: utf-8 -*-

from PIL import Image
import os

# Specify the directory containing the JPEG files
input_directory = r"C:\JPEGtoPNGFolder"
output_directory = r"C:\JPEGtoPNGFolder"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Loop through all files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".jpeg") or filename.endswith(".jpg") or filename.endswith(".JPEG") or filename.endswith(".JPG"):  # Check for JPEG files
        # Open the image
        img = Image.open(os.path.join(input_directory, filename))
        
        # Convert to PNG and rename the file
        new_filename = os.path.splitext(filename)[0].replace("IMG_", "PNG_")+'.PNG'
        img.save(os.path.join(output_directory, new_filename), "PNG")

print("Conversion and renaming completed!")
