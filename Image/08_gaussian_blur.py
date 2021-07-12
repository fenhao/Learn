# -*- coding: utf-8 -*-
# ---
# @Time: 2021/6/27
# @File: 08_gaussian_blur.py
# @Author: Daqing Shi
# @Desc: 高斯模糊
# @update: Record important updates
# ---

import cv2 as cv
import numpy as np

def clamp(pv):
    """
    像素处理
    :param pv: 像素值
    :return: 像素值
    """
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv


def gaussian_noise(image):
    """
    高斯噪声图片
    :param image: 待处理的图片
    """
    h, w, ch = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("noise_image", image)


src = cv.imread("lena.jpg")
cv.namedWindow("src", cv.WINDOW_NORMAL)
cv.imshow("src", src)
t1 = cv.getTickCount()
gaussian_noise(src)
t2 = cv.getTickCount()
time = (t2 - t1)/cv.getTickFrequency()
print("time consume:%s" % (time*1000))
dst = cv.GaussianBlur(src, (5, 5), 15)
cv.imshow("dst", dst)
cv.waitKey(0)
cv.destroyAllWindows()
