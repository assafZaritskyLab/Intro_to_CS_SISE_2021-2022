import numpy as np
import cv2
circle_ker_3x3 = np.array([
    [0, 255, 0],
    [255, 255, 255],
    [0, 255, 0]
], np.uint8)
rtriangle_ker_3x3 = np.array([
    [0, 255, 0],
    [0, 255, 255],
    [0, 0, 0]
], np.uint8)
ltriangle_ker_3x3 = np.array([
    [0, 255, 0],
    [255, 255, 0],
    [0, 0, 0]
], np.uint8)
square_ker_3x3 = np.array([
    [255, 255, 255],
    [255, 255, 255],
    [255, 255, 255]
], np.uint8)
v_line_ker_3x3 = np.array([
    [0, 255, 0],
    [0, 255, 0],
    [0, 255, 0]
], np.uint8)

h_line_ker_3x3 = np.array([
    [0, 0, 0],
    [255, 255, 255],
    [0, 0, 0]
], np.uint8)

h_line_ker_10x10 = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
], np.uint8)
# cv2.imshow('line', h_line_ker_10x10)
# cv2.waitKey(0)