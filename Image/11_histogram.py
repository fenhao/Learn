# -*- coding: utf-8 -*-
# ---
# @Time: 2021/6/29
# @File: 11_histogram.py
# @Author: Daqing Shi
# @Desc: 直方图均衡化和直方图比较
# @update: Record important updates
# ---


import cv2 as cv
import numpy as np


def equal_hist(image):
    """
    全局直方图均衡化
    :param image:待处理的图像
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.namedWindow("equal_hist", cv.WINDOW_NORMAL)
    cv.imshow("equal_hist", dst)

def clahe_demo(image):
    """
    自适应直方图均衡化
    :param image:待处理的图像
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.namedWindow("clahe_demo", cv.WINDOW_NORMAL)
    cv.imshow("clahe_demo", dst)

def create_rgb_hist(image):
    """
    rgb直方图
    :param image:待处理的图像
    """
    h, w, ch = image.shape
    rgb_hist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256/16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = int(b/bsize)*16*16+int(g/bsize)*16+int(r/bsize)
            rgb_hist[int(index), 0] += 1
    return rgb_hist

def hist_compare(image1, image2):
    """
    相关性比较
    :param image1: 待对比图片1
    :param image2: 待对比图片2
    """
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴氏距离：%s， 相关性：%s ,卡方：%s" % (match1, match2, match3))


img1 = cv.imread("result.png")
img2 = cv.imread("lena.jpg")
# cv.namedWindow("img1", cv.WINDOW_NORMAL)
# cv.imshow("img1", img1)
# cv.namedWindow("img2", cv.WINDOW_NORMAL)
# cv.imshow("img2", img2)
# equal_hist(src)
# clahe_demo(src)
t1 = cv.getTickCount()
hist_compare(img1, img2)
t2 = cv.getTickFrequency()
time_count = (t1 - t2)/cv.getTickFrequency()
print("花费的时间为：%s" % time_count)
cv.waitKey(0)
cv.destroyAllWindows()
