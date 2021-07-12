# -*- coding: utf-8 -*-
# ---
# @Time: 2021/6/28
# @File: 09_EPF.py
# @Author: Daqing Shi
# @Desc: 边缘保留滤波EPF--高斯双边和均值迁移
# @update: Record important updates
# ---

import cv2 as cv


def bi_demo(image):
    """
    双边模糊，与高斯模糊的差别：轮廓得到保留
    :param image: 待处理的图像
    """
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_demo", dst)

def shift_demo(image):
    """
    均值迁移，边缘部分会有过度模糊的情况
    :param image: 待处理的图像
    """
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("shift_demo", dst)


src = cv.imread("lena.jpg")
cv.namedWindow("src", cv.WINDOW_NORMAL)
cv.imshow("src", src)
# bi_demo(src)
shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
