# -*- coding: utf-8 -*-
# ---
# @Time: 2021/6/27
# @File: roi+fill.py
# @Author: Daqing Shi
# @Desc: ROI与泛洪填充
# @update: Record important updates
# ---

import cv2 as cv
import numpy as np


def fill_color_demo(image):
    """
    泛洪填充彩色图像
    :param image: 待处理的图像
    """
    copy_img = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    cv.floodFill(copy_img, mask, (30, 30), (0, 255, 255), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo", copy_img)

def fill_binary():
    """
    泛洪填充二值图像
    """
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow("fill_binary", image)
    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301, :] = 0
    cv.floodFill(image, mask, (200, 200), (0, 0, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("fill_binary", image)


src = cv.imread("lena.jpg")
# cv.namedWindow("src", cv.WINDOW_NORMAL)
# cv.imshow("src", src)
# face = src[50:250, 100:300]
# cv.imshow("face", face)
# gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)
# back_face = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
# cv.imshow("backface", back_face)
# src[50:250, 100:300] = back_face
# cv.imshow("src", src)
# fill_color_demo(src)
fill_binary()
cv.waitKey(0)
cv.destroyAllWindows()