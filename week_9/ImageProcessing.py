import numpy as np
import cv2
import matplotlib.pyplot as plt
from kernels import square_ker_3x3, rtriangle_ker_3x3, circle_ker_3x3, ltriangle_ker_3x3, v_line_ker_3x3, h_line_ker_3x3, h_line_ker_10x10

# creating a two cell illustration
# two_cells = np.zeros((100,100), np.uint8)
# cellular_foreground = 250
# two_cells[3:30, 2:40] = cellular_foreground
# two_cells[50:80, 42:72] = cellular_foreground
# two_cells[30:53, 37:42] = cellular_foreground
# cv2.imshow("img", two_cells)
# cv2.imwrite("two_connected_cells.jpg", two_cells)


# creating a bad text scan
# img = cv2.imread('SampleImages/Scan1.jpeg', 0)
# cv2.imshow('img', img)
# kernel = np.ones((3,3),np.uint8)
# erosion = cv2.erode(img, kernel, iterations=1)
# cv2.imwrite('SampleImages/Scan1_eroded.jpg', erosion)
#
# fixing the bad text scan
# bad_txt = cv2.imread('SampleImages/Scan1_eroded.jpg', 0)
# dilation_kernel = circle_ker_3x3
# fixed_text = cv2.dilate(bad_txt, dilation_kernel, iterations=1)
# cv2.imshow("original", bad_txt)
# cv2.imshow("fixed text", fixed_text)

# removing the redundant line between cells
# two_cells_img = cv2.imread('SampleImages/two_connected_cells.jpg', 0)
# erosion_kernel = h_line_ker_10x10
# fixed_img = cv2.erode(two_cells_img, erosion_kernel, iterations=1)
# cv2.imshow("original", two_cells_img)
# cv2.imshow("fixed", fixed_img)

# real cells dilation
# real_cells = cv2.imread("SampleImages/cells.jpg", 0)
# dilation_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# fixed_img = cv2.dilate(real_cells, dilation_kernel, iterations=1)
# cv2.imshow("original", real_cells)
# cv2.imshow("fixed", fixed_img)
# cv2.imwrite("SampleImages/RESULTS/org.jpg", real_cells)
# cv2.imwrite("SampleImages/RESULTS/fixed.jpg", fixed_img)
# removing noise, opening
# img = cv2.imread("SampleImages/cells.jpg", 0)
# kernel_size = (5,5)
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
# iterations = range(3)
# fixed_img = np.copy(img)
# for iter_ in iterations:
#     fixed_img = cv2.morphologyEx(fixed_img, cv2.MORPH_OPEN, kernel)
# cv2.imshow("original", img)
# cv2.imshow("fixed", fixed_img)
# cv2.imwrite("SampleImages/RESULTS/org.jpg", img)
# cv2.imwrite("SampleImages/RESULTS/fixed.jpg", fixed_img)

# closing
# img = cv2.imread("SampleImages/cells.jpg", 0)
# kernel_size = (5,5)
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
# iterations = range(3)
# fixed_img = np.copy(img)
# for iter_ in iterations:
#     fixed_img = cv2.morphologyEx(fixed_img, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("original", img)
# cv2.imshow("fixed", fixed_img)
# cv2.imwrite("SampleImages/RESULTS/org.jpg", img)
# cv2.imwrite("SampleImages/RESULTS/fixed.jpg", fixed_img)


# get the cells contour
img = cv2.imread("SampleImages/cells.jpg", 0)
kernel_size = (3,3)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
fixed_img = np.copy(img)
# fixed_img = cv2.morphologyEx(fixed_img, cv2.MORPH_CLOSE, kernel)
fixed_img = cv2.erode(img, kernel, iterations=1)
fixed_img = img - fixed_img
for i in range(200):
    kernel = h_line_ker_3x3
    fixed_img = cv2.morphologyEx(fixed_img, cv2.MORPH_OPEN, kernel)
    kernel = v_line_ker_3x3
    fixed_img = cv2.morphologyEx(fixed_img, cv2.MORPH_OPEN, kernel)
cv2.imshow("original", img)
cv2.imshow("fixed", fixed_img)
# cv2.imwrite("SampleImages/RESULTS/org.jpg", img)
# cv2.imwrite("SampleImages/RESULTS/fixed.jpg", fixed_img)

# cv2.imshow("img", img)
# # cv2.waitKey(0)
# # # closing all open windows
# # cv2.destroyAllWindows()
#
# # erode than dilate
# kernel = np.ones((3,3),np.uint8)
# erosion = cv2.erode(img, kernel, iterations=1)
# erosion_and_dilation = cv2.dilate(erosion, kernel, iterations=1)
# # cv2.imshow("img Eroded&Dilated", erosion_and_dilation)
# # cv2.waitKey(0)
# # # closing all open windows
# # cv2.destroyAllWindows()\
# # dilate again
# final_ = cv2.dilate(erosion_and_dilation, kernel, iterations=1)
# final_ = cv2.erode(erosion_and_dilation, kernel, iterations=1)
# cv2.imshow("final", final_)
cv2.waitKey(0)

