import cv2
import numpy as np


def sort_pixels(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Get image dimensions
    height, width = img.shape[:2]

    # Convert image to grayscale for brightness calculation
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create a copy of the original image for sorting
    sorted_img = img.copy()

    # Flatten the image and grayscale arrays
    flat_img = img.reshape(-1, 3)  # RGB values
    flat_gray = gray.reshape(-1)  # Brightness values

    # Sort pixels by brightness (from darkest to brightest)
    sorted_indices = np.argsort(flat_gray)
    sorted_pixels = flat_img[sorted_indices]

    # Reshape back to original dimensions
    sorted_img = sorted_pixels.reshape(height, width, 3)

    # Create side-by-side comparison
    comparison = np.hstack((img, sorted_img))

    # Add labels
    label_height = 30
    white = (255, 255, 255)
    labeled_comparison = cv2.copyMakeBorder(comparison, label_height, 0, 0, 0,
                                            cv2.BORDER_CONSTANT, value=(0, 0, 0))

    # Add text labels
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(labeled_comparison, 'Original', (width // 4, 20), font,
                0.7, white, 2)
    cv2.putText(labeled_comparison, 'Sorted by Brightness', (width + width // 4, 20),
                font, 0.7, white, 2)

    return labeled_comparison


# Example usage
if __name__ == "__main__":
    # Replace with your image path
    image_path = "test.jpg"

    # Process the image
    result = sort_pixels(image_path)

    # Display the result
    cv2.imshow('Pixel Sorting Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Optionally save the result
    cv2.imwrite('sorted_result.jpg', result)