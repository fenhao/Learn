
# -*- coding: utf-8 -*-
# ---
# @Time: 2021/6/23
# @File: save_learn.py
# @Author: Daqing Shi
# @Desc: 图像的加载与保存
# @update: Record important updates
# ---

import cv2 as cv
import numpy as np


def video_demo():
    """
    视频的操作
    """
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_image_info(image):
    """

    :param image: 图片
    """
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


src = cv.imread(r"D:\testgit\Learn\Image\picture\src.png")
cv.namedWindow("src", cv.WINDOW_NORMAL)
cv.imshow("src", src)
get_image_info(src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imwrite("result.png", gray)
# video_demo()
cv.waitKey(0)
cv.destroyAllWindows()
