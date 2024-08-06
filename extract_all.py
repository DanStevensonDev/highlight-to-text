import cv2
import sys
import pytesseract
from pytesseract import Output

class Levels:
    PAGE = 1
    BLOCK = 2
    PARAGRAPH = 3
    LINE = 4
    WORD = 5

def extract_all(img_src):
    # Extract all text as one string
    # string_ocr = pytesseract.image_to_string(
    #     img_thresh, lang='eng', config='--psm 6')
    # Extract all text and meta data as dictionary
    data_ocr = pytesseract.image_to_data(
        img_src, lang='eng', config='--psm 6', output_type=Output.DICT)
    # Copy source image to draw rectangles
    img_result = img_src.copy()

    # Iterate through all words
    for i in range(len(data_ocr['text'])):
        # Skip other levels than 5 (word)
        if data_ocr['level'][i] != Levels.WORD: 
            continue
        # Get bounding box position and size of word
        (x, y, w, h) = (data_ocr['left'][i], data_ocr['top']
                        [i], data_ocr['width'][i], data_ocr['height'][i])
        # Draw rectangle for word bounding box
        cv2.rectangle(img_result, (x, y), (x + w, y + h), (0,0,255), 2)

    return img_result

if __name__ == "__main__":
    # Check if an image file is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 threshold_image.py <image_file>")
        sys.exit(1)

    # Read the image file
    img_file = sys.argv[1]
    img_src = cv2.imread(img_file)

    if img_src is None:
        print(f"Error: Unable to read image file '{img_file}'")
        sys.exit(1)

    # Apply thresholding
    img_result = extract_all(img_src)

    # Save or display the images
    cv2.imwrite("img_result.jpg", img_result)

    print("Image saved successfully.")
