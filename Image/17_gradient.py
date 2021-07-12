# -*- coding: utf-8 -*-
# ---
# @Time: 2021/7/12
# @File: 17_gradient.py
# @Author: Daqing Shi
# @Desc: 图像梯度
# @update: Record important updates
# ---

import cv2 as cv
import numpy as np


def lapalian_demo(image):
    """
    拉普拉斯算子
    :param image: 待处理的图像
    """
    # dst = cv.Laplacian(image, cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    dst = cv.filter2D(image, cv.CV_32F, kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.namedWindow("lpls", cv.WINDOW_NORMAL)
    cv.imshow("lpls", lpls)

def sobel_demo(image):
    """
    sobel算子
    :param image: 待处理的图像
    """
    # grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    # grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)
    grad_y = cv.Scharr(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.namedWindow("gradient-x", cv.WINDOW_NORMAL)
    cv.imshow("gradient-x", gradx)
    cv.namedWindow("gradient-y", cv.WINDOW_NORMAL)
    cv.imshow("gradient-y", grady)
    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.namedWindow("gradient", cv.WINDOW_NORMAL)
    cv.imshow("gradient", gradxy)
    # ret, binary = cv.threshold(gradxy, 127, 255, cv.THRESH_BINARY)
    # cv.namedWindow("binary", cv.WINDOW_NORMAL)
    # cv.imshow("binary", binary)


src = cv.imread(r"color.jpg")
cv.namedWindow("src", cv.WINDOW_NORMAL)
cv.imshow("src", src)
# sobel_demo(src)
lapalian_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()