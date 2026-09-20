# OpenCV Image Toolkit

A beginner-friendly image-processing toolkit built with Python and OpenCV. This project demonstrates fundamental computer vision operations through small, reusable Python functions.

## Features

The toolkit currently supports:

- Loading images
- Converting images to grayscale
- Resizing while preserving the aspect ratio
- Cropping
- Horizontal and vertical flipping
- Rotation
- Gaussian blurring
- Canny edge detection
- Binary thresholding
- Displaying images with Matplotlib
- Saving processed images

## Project Structure

```text
opencv-image-toolkit/
├── images/
│   └── dog.jpg
├── output/
│   └── .gitkeep
├── .gitignore
├── image_toolkit.py
├── main.py
├── README.md
└── requirements.txt
```

- `image_toolkit.py` contains the reusable image-processing functions.
- `main.py` demonstrates how to use the toolkit.
- `images/` contains input images.
- `output/` stores generated images and is ignored by Git.

## Requirements

- Python 3.9 or later
- OpenCV
- NumPy
- Matplotlib

## Installation

Clone the repository:

```bash
git clone https://github.com/bhumikapandey05/opencv-image-toolkit.git
cd opencv-image-toolkit
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Place an image inside the `images/` directory. The example program expects:

```text
images/dog.jpg
```

Run the toolkit:

```bash
python3 main.py
```

The program applies the following processing pipeline:

```text
Load image
  → Grayscale
  → Resize
  → Crop
  → Flip
  → Rotate
  → Gaussian blur
  → Canny edge detection
  → Binary threshold
```

Processed images are displayed using Matplotlib. Saved results are written to the `output/` directory.

## Example

```python
from image_toolkit import (
    apply_canny_edge_detection,
    convert_to_grayscale,
    load_image,
    resize_image,
    save_image,
)

image = load_image("images/dog.jpg")
grayscale_image = convert_to_grayscale(image)
resized_image = resize_image(grayscale_image, width=300)
edges = apply_canny_edge_detection(
    resized_image,
    threshold1=100,
    threshold2=200,
)

save_image(edges, "output/dog_edges.jpg")
```

## Available Functions

| Function | Description |
|---|---|
| `load_image()` | Loads an image from a file |
| `convert_to_grayscale()` | Converts a BGR image to grayscale |
| `resize_image()` | Resizes an image while preserving its aspect ratio |
| `crop_image()` | Crops an image using coordinate boundaries |
| `flip_image()` | Flips an image horizontally, vertically, or both |
| `rotate_image()` | Rotates an image around its center |
| `apply_gaussian_blur()` | Applies Gaussian smoothing |
| `apply_canny_edge_detection()` | Detects edges with the Canny algorithm |
| `apply_threshold()` | Converts an image into a binary image |
| `display_image()` | Displays an image with Matplotlib |
| `save_image()` | Saves an image to disk |

## Flip Codes

OpenCV uses the following flip codes:

| Code | Result |
|---:|---|
| `0` | Vertical flip |
| `1` | Horizontal flip |
| `-1` | Horizontal and vertical flip |

## Planned Improvements

- Brightness and contrast adjustment
- Additional blur filters
- Adaptive and Otsu thresholding
- Sobel and Laplacian edge detection
- Command-line arguments
- Automated tests
- Interactive user interface

## Learning Objectives

This project was created to practice:

- Organizing Python code into reusable functions
- Reading and writing images with OpenCV
- Understanding common image transformations
- Applying fundamental image-processing techniques
- Structuring a computer vision project for GitHub

## License

This project is intended for educational use.