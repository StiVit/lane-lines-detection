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