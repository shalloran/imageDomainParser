import cv2
import pytesseract
import re
import csv
import os
import glob
from tqdm import tqdm

# GLOBALS
DOMAINS = []
PATH_TO_FOLDER = input("Please enter the path to the folder containing the images: ")
OUTPUT_FILE_NAME = input("Please enter the path and name for the output .csv file: ")

# Function to read image and extract domains
def domainExtractor(imagePath):
    # Load the image using cv2
    img = cv2.imread(imagePath)

    # Convert the image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use tesseract to do OCR on the image
    text = pytesseract.image_to_string(gray)

    # Use regex to find domains in the text
    found_domains = re.findall(r'[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    
    # Filter and clean domain names, ensuring subdomains are also captured
    for domain in found_domains:
        # Basic cleaning to ensure it's a proper domain (subdomain.example.com)
        # This may exclude some valid domains but ensures quality of the domains extracted
        if '.' in domain and len(domain.split('.')) > 2:
            DOMAINS.append(domain.lower())

# Use glob to get all png and jpg images in the folder
imagePaths = glob.glob(os.path.join(PATH_TO_FOLDER, "*.png")) + glob.glob(os.path.join(PATH_TO_FOLDER, "*.jpg"))

# Process each image
for path in tqdm(imagePaths):
    domainExtractor(path)

# Remove duplicates from the list of domains
unique_domains = list(set(DOMAINS))

# Sort the unique domains alphabetically
sorted_unique_domains = sorted(unique_domains)

# Output the sorted unique domains
sorted_unique_domains

with open(OUTPUT_FILE_NAME, 'w', newline='') as file:
    writer = csv.writer(file)
    for domain in sorted_unique_domains:
        writer.writerow([domain])
