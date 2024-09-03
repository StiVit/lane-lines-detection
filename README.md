# Lane Detection Project

This project focuses on detecting lane lines on the road from images using various image processing techniques in Python, with the help of OpenCV and NumPy. The project is structured to ensure maintainability, readability, and ease of extension.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Key Features](#key-features)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

LaneDetectionProject/ <br>
│ <br>
├── test_images/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# Directory containing test images <br>
│<br>
├── src/<br>
│&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├── __init__.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# Init file for the src module <br>
│&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├── image_utils.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# Utility functions for image handling and display <br>
│&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├── color_selection.py&emsp;&emsp;&emsp;&emsp;&emsp;# Functions for color selection and masking<br>
│&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├── edge_detection.py &emsp;&emsp;&emsp;# Edge detection methods<br>
│&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├── geometry.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# Setting the geometry for drawing the lines logic<br>
│<br>
├── main.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# Main entry point for the lane detection pipeline<br>
│<br>
└── README.md&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# Project documentation<br>



## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/lanedetection.git
    cd lanedetection
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure you have the `test_images` directory populated with images you want to process. The images should be in `.jpg` format.

## Usage

To run the lane detection pipeline, simply execute the `main.py` script:

```sh
python main.py
```

This will load the images from the test_images directory, apply the lane detection pipeline, and display the processed images with lane lines drawn.

## Key features

- <b>Color Selection:</b> Filters images to isolate lane colors (white and yellow) using RGB, HSV, and HSL color spaces.
- <b>Edge Detection:</b> Detects edges in the filtered images using Canny edge detection.
- <b>Region Selection:</b> Focuses on the region of interest where lanes are likely to be found.
- <b>Lane Detection:</b> Uses Hough Transform to detect lane lines and draws them on the original images.

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request. Please ensure that your code is well-structured and adheres to the existing coding style.

## Licence

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.