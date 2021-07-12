# -*- coding: utf-8 -*-
# ---
# @Time: 2021/7/1
# @File: 14_threshold.py
# @Author: Daqing Shi
# @Desc: Function of this file
# @update: Record important updates
# ---


import cv2 as cv
import numpy as np


def threshold_demo(image):
    """
    二值化图像，全局阈值
    :param image: 待处理的图像
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TRIANGLE)
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO)
    print("threshold value %s" % ret)
    cv.imshow("binary", binary)

def local_threshold(image):
    """
    二值化图像，局部阈值
    :param image: 待处理的图像
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 10)
    # dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.namedWindow("binary", cv.WINDOW_NORMAL)
    cv.imshow("binary", dst)

def custom_threshold(image):
    """
    自定义二值化
    :param image: 待处理的图像
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w*h])
    mean = m.sum()/(w*h)
    print("mean: %s" % mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.namedWindow("binary", cv.WINDOW_NORMAL)
    cv.imshow("binary", binary)


src = cv.imread("color.jpg")
cv.namedWindow("src", cv.WINDOW_NORMAL)
cv.imshow("src", src)
# threshold_demo(src)
# local_threshold(src)
custom_threshold(src)
cv.waitKey(0)
cv.destroyAllWindows()