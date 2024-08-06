import cv2
import sys

def threshold_image(img_src):
    """Grayscale image and apply Otsu's threshold"""
    # Grayscale
    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    # Binarisation and Otsu's threshold
    _, img_thresh = cv2.threshold(
        img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return img_thresh, img_gray

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
    img_thresh, img_gray = threshold_image(img_src)

    # Save or display the images
    cv2.imwrite("thresholded_image.jpg", img_thresh)
    cv2.imwrite("grayscale_image.jpg", img_gray)

    print("Images saved successfully.")
