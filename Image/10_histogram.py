# -*- coding: utf-8 -*-
# ---
# @Time: 2021/6/28
# @File: 10_histogram.py
# @Author: Daqing Shi
# @Desc: 图像直方图
# @update: Record important updates
# ---

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def plot_demo(image):
    """
    直方图图像
    :param image: 待处理的图像
    """
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show()

def image_hist(image):
    """
    图像直方图
    :param image: 待处理的图像
    """
    color = ("blue", "green", "red")
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


src = cv.imread(r"D:\testgit\Learn\Image\picture\src.png")
cv.namedWindow("src", cv.WINDOW_NORMAL)
cv.imshow("src", src)
# plot_demo(src)
image_hist(src)
cv.waitKey(0)
cv.destroyAllWindows()
