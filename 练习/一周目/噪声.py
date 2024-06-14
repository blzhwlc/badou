import cv2
from skimage import util

img = cv2.imread("lenna.png")
nois_img = util.random_noise(img,mode='gaussian')

cv2.imshow("source", img)
cv2.imshow("lenna", nois_img)
cv2.waitKey()
cv2.destroyAllWindows()