import cv2
import numpy as np

def bilinear_interpolation(img, image_size):
    src_h, src_w, src_c = img.shape
    dst_h, dst_w = image_size[0], image_size[1]
    if src_h == dst_h and src_w == dst_w:
        return img.copy()
    dst_img = np.zeros((dst_h,dst_w,src_c), np.uint8)
    scale_x, scale_y = float(src_w)/dst_w, float(src_h)/dst_h
    for i in range(src_c):
        for dst_y in range(dst_h):
            for dst_x in range(dst_w):
                src_x = (dst_x+0.5) * scale_x - 0.5
                src_y = (dst_y+0.5) * scale_y - 0.5

                """ 大图与原图所对应的点不会正好是整数，
                    所以用floor向下取整
                """
                src_x1 = int(np.floor(src_x))
                src_x2 = min(src_x1+1, src_w-1)
                src_y1 = int(np.floor(src_y))
                src_y2 = min(src_y1 + 1, src_h - 1)

                temp0 = (src_x2-src_x)*img[src_y1,src_x1,i] + (src_x-src_x1)*img[src_y1,src_x2,i]
                temp1 = (src_x2-src_x)*img[src_y2,src_x1,i] + (src_x-src_x1)*img[src_y2,src_x2,i]
                dst_img[dst_y, dst_x, i] = int((src_y2-src_y)*temp0 + (src_y-src_y1)*temp1)
    return dst_img

if __name__=='__main__':
    img = cv2.imread("lenna.png")
    dst = bilinear_interpolation(img,(800,800))
    cv2.imshow("OD",img)
    cv2.imshow("1",dst)
    cv2.waitKey()
    cv2.destroyAllWindows()