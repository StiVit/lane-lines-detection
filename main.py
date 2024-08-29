# Import usefull packages

from utils.logger_setup import setup_logger
import logging
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import os
import glob
# from moviepy.editor import VideoFileClip

# @matplotlib inline

app_logger = setup_logger("app_logger", logging.INFO)

def list_images(images, cols = 2, rows = 5, cmap = None):
    plt.figure(figsize=(10, 11))
    for i, image in enumerate(images):
        plt.subplot(rows, cols, i+1)
        cmap = 'gray' if len(image.shape) == 2 else cmap
        plt.imshow(image, cmap=cmap)
        plt.xticks([])
        plt.yticks([])
    plt.tight_layout(pad=0, h_pad=0, w_pad=0)
    plt.show()


def RGB_color_selection(image):
    # While color mask
    lower_threshold = np.uint8([200,200,200])
    upper_threshold = np.uint8([255,255,255])
    white_mask = cv2.inRange(image, lower_threshold, upper_threshold)

    # Yellow color mask
    lower_threshold = np.uint8([175,175,0])
    upper_threshold = np.uint8([255,255,255])
    yellow_mask = cv2.inRange(image, lower_threshold, upper_threshold)

    # Combine white and yellow masks
    mask = cv2.bitwise_or(white_mask, yellow_mask)
    masked_image = cv2.bitwise_and(image, image, mask = mask)
    app_logger.info("Image successfully rbg-masked")

    return masked_image


def convert_hsv(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2HSV)


def HSV_color_selection(image):
    converted_image = convert_hsv(image)

    # While color mask
    lower_threshold = np.uint8([0,0,210])
    upper_threshold = np.uint8([255, 30, 255])
    white_mask = cv2.inRange(converted_image, lower_threshold, upper_threshold)

    # Yellow color mask
    lower_threshold = np.uint8([18, 80, 80])
    upper_threshold = np.uint8([30, 255, 255])
    yellow_mask = cv2.inRange(converted_image, lower_threshold, upper_threshold)

    # Combine white and yellow masks
    mask = cv2.bitwise_or(white_mask, yellow_mask)
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    app_logger.info("Image successfully hsv-masked")

    return masked_image


def convert_hsl(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2HLS)


def HSL_color_selection(image):
    converted_image = convert_hsl(image)
    # While color mask
    lower_threshold = np.uint8([0, 200, 0])
    upper_threshold = np.uint8([255, 255, 255])
    white_mask = cv2.inRange(converted_image, lower_threshold, upper_threshold)

    # Yellow color mask
    lower_threshold = np.uint8([10, 0, 100])
    upper_threshold = np.uint8([40, 255, 255])
    yellow_mask = cv2.inRange(converted_image, lower_threshold, upper_threshold)

    # Combine white and yellow masks
    mask = cv2.bitwise_or(white_mask, yellow_mask)
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    app_logger.info("Image successfully hsl-masked")

    return masked_image


def gray_scale(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def gaussian_smoothing(image, kernel_size = 13):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def canny_detector(image, low_threshold = 50, high_threshold = 150):
    return cv2.Canny(image, low_threshold, high_threshold)

if __name__ == "__main__":
    test_images = [plt.imread(img) for img in glob.glob('test_images/*.jpg')]
    # list_images(test_images)

    # list_images(list(map(RGB_color_selection, test_images)))

    # list_images(list(map(HSV_color_selection, test_images)))

    # list_images(list(map(HSL_color_selection, test_images)))

    color_selected_images = list(map(HSL_color_selection, test_images))
    gray_images = list(map(gray_scale, color_selected_images))
    blur_images = list(map(gaussian_smoothing, gray_images))
    # list_images(blur_images)

    edge_detected_images = list(map(canny_detector, blur_images))
    list_images(edge_detected_images)