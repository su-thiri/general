from PIL import Image
import cv2
import numpy as np
import pytesseract

def remove_table_lines(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detector
    edges = cv2.Canny(blurred, 50, 150)

    # Dilate the edges to make them more prominent
    dilated = cv2.dilate(edges, None, iterations=2)

    # Find contours in the dilated image
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw white rectangles over the detected contours to remove the lines
    cv2.drawContours(img, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

    return img

def crop_and_extract_text(input_path, output_path, left, top, right, bottom):
    # Open the image file
    img = Image.open(input_path)
    img_array = np.array(img)

    # Remove table lines
    img_array = remove_table_lines(img_array)

    # Crop the image
    cropped_img = Image.fromarray(img_array[top:bottom, left:right])

    # Save the cropped image
    cropped_img.save(output_path)

    # Extract text using Tesseract OCR
    extracted_text = pytesseract.image_to_string(cropped_img)
    print("Extracted Text:\n", extracted_text)

# Example usage:
input_image_path = 'logo_real.jpg'
output_image_path = 'progress.jpg'

# Define the coordinates of the area to be cropped (left, top, right, bottom)
crop_coordinates = (20, 500, 1250, 710)

crop_and_extract_text(input_image_path, output_image_path, *crop_coordinates)
