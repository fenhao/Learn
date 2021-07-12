# -*- coding: utf-8 -*-
# ---
# @Time: 2021/6/27
# @File: blur.py
# @Author: Daqing Shi
# @Desc: Function of this file
# @update: Record important updates
# ---

import cv2 as cv
import numpy as np

def blur_demo(image):
    """
    图像均值模糊操作，用于去噪
    :param image:待处理的图像
    """
    dst = cv.blur(image, (5, 5))
    cv.imshow("dst", dst)

def median_blur_demo(image):
    """
    图像中值模糊操作，用于去噪
    :param image:待处理的图像
    """
    dst = cv.medianBlur(image, 5)
    cv.imshow("median_blur_demo", dst)

def custom_blur_demo(image):
    """
    自定义图像模糊处理
    :param image:待处理的图像
    """
    # kernel = np.ones([5, 5], np.float32)/25
    # kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.float32)/9
    # 锐化操作
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)
    dst = cv.filter2D(image, -1, kernel)
    cv.imshow("custom_blur_demo", dst)


src = cv.imread("lena.jpg")
cv.namedWindow("src", cv.WINDOW_NORMAL)
cv.imshow("src", src)
blur_demo(src)
median_blur_demo(src)
custom_blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
