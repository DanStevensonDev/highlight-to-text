import cv2
import numpy as np
import pytesseract

def extract_highlighted_text(image_path):
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_orange = np.array([5, 100, 100])
    upper_orange = np.array([15, 255, 255])
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        # Crop to the exact bounding box of the contour
        if w > 50 and h > 20:  # Adjust size thresholds as needed
            cropped_img = img[y:y+h, x:x+w]
            cropped_gray = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(cropped_gray)
            print("Highlighted Text:", text.strip())

image_path = './img.jpg'
extract_highlighted_text(image_path)
