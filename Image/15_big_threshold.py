# -*- coding: utf-8 -*-
# ---
# @Time: 2021/7/1
# @File: 15_big_threshold.py
# @Author: Daqing Shi
# @Desc: 超大图像二值化
# @update: Record important updates
# ---

import cv2 as cv
import numpy as np


def big_image_binary(image):
    """
    对图像进行切块之后进行二值化的分割
    :param image:待处理的图像
    """
    print(image.shape)
    h, w = image.shape[:2]
    ch = 256
    cw = 256
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:col+cw]
            # ret, binary = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
            # binary = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)
            print(np.std(roi), np.mean(roi))
            dev = np.std(roi)
            if dev < 15:
                gray[row:row + ch, col:col + cw] = 255
            else:
                ret, binary = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
                gray[row:row+ch, col:col+cw] = binary
            # print(np.std(binary), np.mean(binary))
    cv.imwrite("binary_result.jpg", gray)


# src = cv.imread(r"D:\testgit\Learn\Image\picture\src.png")
src = cv.imread("color.jpg")
cv.namedWindow("src", cv.WINDOW_NORMAL)
cv.imshow("src", src)
big_image_binary(src)
cv.waitKey(0)
cv.destroyAllWindows()