# Image Pixel Sorter

A Python application that sorts pixels in an image based on brightness, rearranging them from darkest to brightest starting from the top-left corner to the bottom-right. The program provides a side-by-side comparison of the original and sorted images.

## Features

- Pixel sorting based on brightness values
- Side-by-side comparison view of original and processed images
- Labeled output for easy comparison
- Support for various image formats (JPG, PNG, etc.)
- Option to save the processed result

## Requirements

- Python 3.6+
- OpenCV (cv2)
- NumPy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mosvlad/image_sort
cd image-sort
```

2. Install required dependencies:
```bash
pip install opencv-python numpy
```

## Usage

1. Place your input image in the project directory or note its path
2. Run the script:
```bash
python pixel_sorter.py
```

3. By default, the program will:
   - Display the processing result in a window
   - Wait for a key press before closing
   - Save the result as 'sorted_result.jpg'

To use the script with your own image, modify the `image_path` variable in the code:
```python
image_path = "path/to/your/image.jpg"
```

## Code Structure

```python
sort_pixels(image_path)  # Main function that processes the image
```

The function performs the following steps:
1. Loads the input image
2. Converts it to grayscale for brightness calculation
3. Sorts pixels based on brightness values
4. Creates a side-by-side comparison
5. Adds labels for clarity

## Output Example

The program generates a window displaying:
- Left side: Original image
- Right side: Brightness-sorted image
- Labels above each image for identification


## License

MIT License - feel free to use and modify the code as needed.

