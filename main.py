# Import usefull packages

from utils.logger_setup import setup_logger
import logging
import matplotlib.pyplot as plt
import numpy as np
import cv2
import glob

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


    return masked_image


def gray_scale(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def gaussian_smoothing(image, kernel_size = 13):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def canny_detector(image, low_threshold = 50, high_threshold = 150):
    return cv2.Canny(image, low_threshold, high_threshold)


def region_selection(image):
    mask = np.zeros_like(image)
    if len(image.shape) > 2:
        channel_count = image.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
    rows,cols = image.shape[:2]
    bottom_left = [cols * 0.1, rows * 0.95]
    top_left = [cols * 0.4, rows * 0.6]
    bottom_right = [cols * 0.9, rows * 0.95]
    top_right = [cols * 0.6, rows * 0.6]
    vertices = np.array([[bottom_left, top_left, top_right, bottom_right]], dtype=np.int32)
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

def hough_transform(image):
    rho = 1
    theta = np.pi/180
    threshold = 20
    minLineLength = 20
    maxLineGap = 300
    return cv2.HoughLinesP(image, rho=rho, theta=theta, threshold=threshold, minLineLength=minLineLength, maxLineGap=maxLineGap)


def draw_lines(image, lines, color = [255, 0, 0], thickness = 2):
    image = np.copy(image)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(image, (x1,y1), (x2,y2), color, thickness)
    return image


def average_slope_intercept(lines):
    left_lines = []
    left_weights = []
    right_lines = []
    right_weights = []

    for line in lines:
        for x1, y1, x2, y2 in line:
            if x1 == x2:
                continue
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - (slope * x1)
            length = np.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))
            if slope < 0:
                left_lines.append((slope, intercept))
                left_weights.append((length))
            else:
                right_lines.append((slope, intercept))
                right_weights.append((length))
    left_lane = np.dot(left_weights, left_lines) / np.sum(left_weights) if len(left_weights) > 0 else None
    right_lane = np.dot(right_weights, right_lines) / np.sum(right_weights) if len(right_weights) > 0 else None
    return left_lane, right_lane


def pixel_points(y1, y2, line):
    if line is None:
        return None
    slope, intercept = line
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept)/slope)
    y1 = int(y1)
    y2 = int(y2)
    return ((x1, y1), (x2, y2))


def lane_lines(image, lines):
    left_lane, right_lane = average_slope_intercept(lines)
    y1 = image.shape[0]
    y2 = y1 * 0.6
    left_line = pixel_points(y1 , y2, left_lane)
    right_lane = pixel_points(y1, y2, right_lane)
    return left_line, right_lane


def draw_lane_lines(image, lines, color = [255, 0, 0], thickness = 12):
    line_image = np.zeros_like(image)
    for line in lines:
        if line is not None:
            cv2.line(line_image, *line, color, thickness)
    return cv2.addWeighted(image, 1.0, line_image, 1.0, 0.0)






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