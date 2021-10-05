
# removing the redundant line between fake cells
import cv2
from pandas import np

from week_9.kernels import h_line_ker_10x10

# # Erosion
two_cells_img = cv2.imread('SampleImages/SampleImages/two_connected_cells.jpg', 0)
erosion_kernel = h_line_ker_10x10
fixed_img = cv2.erode(two_cells_img, erosion_kernel, iterations=1)
cv2.imshow("erosion", erosion_kernel)
cv2.imshow("original", two_cells_img)
cv2.imshow("fixed", fixed_img)
cv2.waitKey(0)


# img = cv2.imread("SampleImages/SampleImages/cells.jpg", 0)
# kernel_size = (5,5)
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
# iterations = range(3)
# fixed_img = np.copy(img)
# for iter_ in iterations:
#     fixed_img = cv2.morphologyEx(fixed_img, cv2.MORPH_OPEN, kernel)
# cv2.imshow("original", img)
# cv2.imshow("fixed", fixed_img)
# cv2.waitKey(0)
