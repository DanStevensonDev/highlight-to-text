import cv2
import numpy as np
import pytesseract

def extract_underlined_text(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the orange color
    lower_orange = np.array([5, 100, 100])
    upper_orange = np.array([15, 255, 255])

    # Create a mask to extract orange regions
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on size and aspect ratio
    valid_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100 and cv2.arcLength(cnt, True) > 2 * cv2.contourArea(cnt)]

    # Iterate through the filtered contours
    for contour in valid_contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Check if the region is roughly horizontal
        if h > 5 and w > 50 and w > 2 * h:
            # Crop the region above the line to extract text
            cropped_img = img[0:y, 0:img.shape[1]]

            # Convert the cropped image to grayscale
            cropped_gray = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)

            # Perform OCR on the cropped image
            text = pytesseract.image_to_string(cropped_gray)

            # Print the extracted text
            print("Underlined Text:", text.strip())

# Update the image path
image_path = '/Users/dan/Projects/personal/highlights-to-text/img.JPG'
extract_underlined_text(image_path)
