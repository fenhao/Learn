
# -*- coding: utf-8 -*-
# ---
# @Time: 2021/6/27
# @File: piexl_operate.py
# @Author: Daqing Shi
# @Desc: 图像像素的操作
# @update: Record important updates
# ---

import cv2 as cv
import numpy as np


def logic_demo(m1, m2):
    """
    对图像进行逻辑运算
    :param m1:第一张图像
    :param m2:第二张图像
    """
    dst = cv.bitwise_and(m1, m2)
    dst1 = cv.bitwise_not(m1, m2)
    dst2 = cv.bitwise_or(m1, m2)
    dst3 = cv.bitwise_xor(m1, m2)
    cv.imshow("logic_demo", dst)
    cv.waitKey(0)
    cv.imshow("logic_demo", dst1)
    cv.waitKey(0)
    cv.imshow("logic_demo", dst2)
    cv.waitKey(0)
    cv.imshow("logic_demo", dst3)


def contrast_brightness_demo(image, c, b):
    """
    调整图像的亮度和对比度
    :param image: 需要调整的图像
    :param c: 对比度
    :param b: 亮度
    """
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.namedWindow("dst", cv.WINDOW_NORMAL)
    cv.imshow("dst", dst)


src = cv.imread(r"D:\testgit\Learn\Image\picture\src.png")
src1 = cv.imread("LinuxLogo.jpg")
src2 = cv.imread("WindowsLogo.jpg")
cv.namedWindow("src", cv.WINDOW_NORMAL)
cv.imshow("src", src)
contrast_brightness_demo(src, 1.2, 10)
# logic_demo(src1, src2)
cv.waitKey(0)
cv.destroyAllWindows()
