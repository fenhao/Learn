# -*- coding: utf-8 -*-
# ---
# @Time: 2021/6/29
# @File: 12_histogram.py
# @Author: Daqing Shi
# @Desc: 反向直方图投影
# @update: Record important updates
# ---

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def back_projection_demo():
    """
    反向直方图投影
    """
    sample = cv.imread("sample.png")
    target = cv.imread("lena.jpg")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)
    cv.imshow("sample", sample)
    cv.imshow("target", target)
    # roi_hist = cv.calcHist([roi_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    roi_hist = cv.calcHist([roi_hsv], [0, 1], None, [32, 48], [0, 180, 0, 256])
    cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv], [0, 1], roi_hist, [0, 180, 0, 256], 1)
    cv.imshow("back_projection-demo", dst)
    result = cv.bitwise_and(dst, dst)
    cv.imshow("result-demo", result)


def hist2d_demo(image):
    """
    二维直方图
    :param image: 待处理的图片
    """
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # cv.imshow("hist2d", hist)
    plt.imshow(hist, interpolation="nearest")
    plt.title("2D Histogram")
    plt.show()


src = cv.imread(r"D:\testgit\Learn\Image\picture\src.png")
# cv.namedWindow("src", cv.WINDOW_NORMAL)
# cv.imshow("src", src)
back_projection_demo()
# hist2d_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
