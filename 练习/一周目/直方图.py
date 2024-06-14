import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lenna.png")
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

dst = cv2.equalizeHist(gray)    # 对gary进行直方图均衡化
cv2.imshow("1", np.hstack([gray,dst]))
cv2.waitKey()

plt.figure()
plt.hist(dst.ravel(), 256)
plt.show()


# 彩色
img = cv2.imread("lenna.png")
(b,g,r) = cv2.split(img)
b_h = cv2.equalizeHist(b)
g_h = cv2.equalizeHist(g)
r_h = cv2.equalizeHist(r)

dst = cv2.merge((b_h,g_h,r_h))
cv2.imshow("dst", np.hstack([img,dst]))
cv2.waitKey()