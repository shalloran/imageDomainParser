# Domain Parser

This Python script extracts domain names from images using Optical Character Recognition (OCR).

## Description

The script prompts the user for a directory path, then processes all .png and .jpg images in that directory. It uses the OpenCV library to load and convert each image to grayscale, then uses the pytesseract library (a Python wrapper for Google's Tesseract-OCR Engine) to perform OCR on the image and extract text.

The script then uses regular expressions to find domain names in the extracted text. It filters and cleans the domain names, ensuring subdomains are also captured. The script removes duplicates from the list of domains, sorts the unique domains alphabetically, and writes them to a .csv file.

## Dependencies

This script requires the following Python libraries:

- OpenCV (cv2)
- pytesseract
- glob
- os
- csv
- tqdm

You can install these libraries using pip:

`` bash
  pip install opencv-python pytesseract glob2 tqdm
`

Note: The script also requires the Tesseract-OCR Engine to be installed on your system. You can download it from [here](https://github.com/tesseract-ocr/tesseract/wiki).

## Usage

Run the script in your terminal:

`` bash
  python domain-parser.py
`

When prompted, enter the path to the folder containing the images and the path and name for the output .csv file.
