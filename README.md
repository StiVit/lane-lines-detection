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
├── test_images/<br>
│<br>
├── src/<br>
│ ├── __init__.py<br>
│ ├── image_utils.py<br>
│ ├── color_selection.py<br>
│ ├── edge_detection.py <br>
│ ├── geometry.py<br>
│<br>
├── main.py<br>
│<br>
└── README.md<br>



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