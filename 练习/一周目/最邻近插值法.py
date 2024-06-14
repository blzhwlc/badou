import cv2
import numpy as np

def nearest_inter(img):
    h, w, c = img.shape
    emptyImage = np.zeros((800,800,c), np.uint8)
    sh = 800/h
    sw = 800/w
    for i in range(800):
        for j in range(800):
            x = int(i/sh+0.5)   # int向下取整，需要+0.5
            y = int(j/sw+0.5)
            emptyImage[i,j] = img[x,y]
    return emptyImage

img = cv2.imread("lenna.png")
# new_img = nearest_inter(img)
new_img = cv2.resize(img, (800,800), interpolation=cv2.INTER_NEAREST)
cv2.imshow("img", img)
cv2.imshow("new", new_img)
cv2.waitKey()
cv2.destroyAllWindows()