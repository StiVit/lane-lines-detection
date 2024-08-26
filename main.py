# Import usefull packages
from utils.logger_setup import setup_logger
import logging
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import os
import glob
from moviepy.editor import VideoFileClip

app_logger = setup_logger("app_logger", logging.INFO)

