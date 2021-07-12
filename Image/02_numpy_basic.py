# -*- coding: utf-8 -*-
# ---
# @Time: 2021/6/23
# @File: numpy_basic.py
# @Author: Daqing Shi
# @Desc: Function of this file
# @update: Record important updates
# ---

import cv2 as cv
import numpy as np


def access_pixels(image):
    """

    :param image: 读取的图片
    """
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width:%s, height:%s, channels:%s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for chn in range(channels):
                pv = image[row, col, chn]
                image[row, col, chn] = 255 - pv
    cv.namedWindow("pixel_demo", cv.WINDOW_NORMAL)
    cv.imshow("pixel_demo", image)


def inverse(image):
    """
    图像反变换
    :param image:输入的图像
    """
    dst = cv.bitwise_not(image)
    cv.namedWindow("inverse", cv.WINDOW_NORMAL)
    cv.imshow("inverse", dst)


def create_image():
    """
    多通道
    :return:
    """
    # img = np.zeros([400, 400, 3], np.uint8)
    # # img[:, :, 2] = np.ones([400, 400])*255
    # img[:, :, 1] = np.ones([400, 400])*255
    # cv.imshow("new_img", img)
    # 单通道
    # img = np.ones([400, 400], np.uint8)
    # img = img * 127
    # # img = np.zeros([400, 400], np.uint8)
    # # img[:, :] = np.ones([400, 400])*255
    # cv.imshow("new_img", img)
    m1 = np.ones([3, 3], np.float32)
    m1.fill(4442.2388)
    print(m1)
    m2 = m1.reshape([1, 9])
    print(m2)
    m3 = np.array([[2, 3, 4], [4, 5, 6], [7, 8, 9]], np.int32)
    # m3.fill(9)
    print(m3)


src = cv.imread(r"D:\testgit\Learn\Image\picture\src.png")
# cv.namedWindow("src", cv.WINDOW_NORMAL)
# cv.imshow("src", src)
# 获取CPU占用时间
t1 = cv.getTickCount()
create_image()
inverse(src)
# access_pixels(src)
t2 = cv.getTickCount()
print("time:%s ms" % (((t2-t1)/cv.getTickFrequency())*1000))
cv.waitKey(0)
cv.destroyAllWindows()