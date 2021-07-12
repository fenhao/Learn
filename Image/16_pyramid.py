# -*- coding: utf-8 -*-
# ---
# @Time: 2021/7/1
# @File: 16_pyramid.py
# @Author: Daqing Shi
# @Desc: 图像金字塔-高斯金字塔和拉普拉斯金字塔。原理-高斯模糊+降采样
# @update: Record important updates
# ---

import cv2 as cv
import numpy as np

def pyramid_demo(image):
    """
    图像金字塔
    :param image: 待处理的图像
    :return: 返回图像金字塔的图片
    """
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_down"+str(i), dst)
        temp = dst.copy()
    return pyramid_images

def lapalian_demo(image):
    """
    拉普拉斯金字塔
    :param image: 待处理的图像
    """
    pyramid_images = pyramid_demo(image)
    level = len(pyramid_images)
    for i in range(level-1, -1, -1):
        if i-1 < 0:
            expand = cv.pyrUp(pyramid_images[i], dstsize=image.shape[:2])
            lpls = cv.subtract(image, expand)
            cv.imshow("lapalian_demo" + str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i-1].shape[:2])
            lpls = cv.subtract(pyramid_images[i-1], expand)
            cv.imshow("lapalian_demo"+str(i), lpls)


# src = cv.imread(r"D:\testgit\Learn\Image\picture\src.png")
src = cv.imread("lena.jpg")
cv.namedWindow("src", cv.WINDOW_NORMAL)
cv.imshow("src", src)
pyramid_demo(src)
lapalian_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()