# Import usefull packages

from utils.logger_setup import setup_logger
import logging
import matplotlib.pyplot as plt
import glob

from src.image_utils import list_images
from src.color_selection import RGB_color_selection, HSV_color_selection, HSL_color_selection
from src.edge_detection import gray_scale, gaussian_smoothing, canny_detector, region_selection
from src.geometry import hough_transform, draw_lines, lane_lines, draw_lane_lines

app_logger = setup_logger("app_logger", logging.INFO)

if __name__ == "__main__":
    test_images = [plt.imread(img) for img in glob.glob('test_images/*.jpg')]
    # list_images(test_images)

    # list_images(list(map(RGB_color_selection, test_images)))
    app_logger.info("Images successfully rbg-masked")

    # list_images(list(map(HSV_color_selection, test_images)))
    app_logger.info("Images successfully hsv-masked")

    # list_images(list(map(HSL_color_selection, test_images)))
    app_logger.info("Images successfully hsl-masked")

    color_selected_images = list(map(HSL_color_selection, test_images))
    gray_images = list(map(gray_scale, color_selected_images))
    blur_images = list(map(gaussian_smoothing, gray_images))
    app_logger.info("Images successfully blurred")
    # list_images(blur_images)


    edge_detected_images = list(map(canny_detector, blur_images))
    app_logger.info("Images' edges successfully detected")
    # list_images(edge_detected_images)

    masked_image = list(map(region_selection, edge_detected_images))
    app_logger.info("region mask successfully applied")
    # list_images(masked_image)

    hough_lines = list(map(hough_transform, masked_image))
    app_logger.info("hough transformation successfully applied")
    line_images = []
    for image, lines in zip(test_images, hough_lines):
        line_images.append(draw_lines(image, lines))
    app_logger.info("Lines successfully drew")
    # list_images(line_images)

    lane_images = []
    for image, lines in zip(test_images, hough_lines):
        lane_images.append(draw_lane_lines(image, lane_lines(image, lines)))
    app_logger.info("Lines successfully processed")
    list_images(lane_images)