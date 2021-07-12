# -*- coding: utf-8 -*-
# ---
# @Time: 2021/6/27
# @File: space_color.py
# @Author: Daqing Shi
# @Desc: 色彩空间知识
# @update: Record important updates
# ---

import cv2 as cv
import numpy as np


def extrace_object_demo():
    """
    读取视频，并跟踪里面的黄色圆点
    """
    capture = cv.VideoCapture("D-VIDEO.mp4")
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([26, 43, 46])
        upper_hsv = np.array([34, 255, 255])
        mask = cv.inRange(hsv, lower_hsv, upper_hsv)
        dst = cv.bitwise_and(frame, frame, mask=mask)
        # cv.imshow("video", frame)
        # cv.imshow("mask", mask)
        cv.imshow("dst", dst)
        c = cv.waitKey(40)
        if c == 27:
            break


def color_space_demo(image):
    """
    色彩空间转换
    :param image: 要转换的土坯那
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.namedWindow("gray", cv.WINDOW_NORMAL)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.namedWindow("hsv", cv.WINDOW_NORMAL)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.namedWindow("yuv", cv.WINDOW_NORMAL)
    cv.imshow("yuv", yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.namedWindow("ycrcb", cv.WINDOW_NORMAL)
    cv.imshow("ycrcb", ycrcb)


src = cv.imread(r"D:\testgit\Learn\Image\picture\src.png")
# cv.namedWindow("src", cv.WINDOW_NORMAL)
# cv.imshow("src", src)
b, g, r = cv.split(src)
# cv.imshow("blue", b)
# cv.imshow("green", g)
# cv.imshow("red", r)
src[:, :, 2] = 0
src = cv.merge([b, g, r])
src[:, :, 0] = 0
# cv.namedWindow("src", cv.WINDOW_NORMAL)
# cv.imshow("src", src)
extrace_object_demo()
# color_space_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
