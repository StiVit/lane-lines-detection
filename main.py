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

test_images = [plt.imread(img) for img in glob.glob('test_images/*.jpg')]
list_images(test_images)


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

    return masked_image


list_images(list(map(RGB_color_selection, test_images)))

