import cv2
import numpy as np

img = cv2.imread("sunset-8437462_640.webp",0)

x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

dstx = cv2.convertScaleAbs(x)
dsty = cv2.convertScaleAbs(y)

dst = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)

cv2.imshow("x", dstx)
cv2.imshow("y", dsty)
cv2.imshow("dst", dst)
cv2.waitKey()