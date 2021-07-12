# -*- coding: utf-8 -*-
# ---
# @Time: 2021/6/30
# @File: 13_compare.py
# @Author: Daqing Shi
# @Desc: 模板匹配
# @update: Record important updates
# ---


import cv2 as cv
import numpy as np


def template_demo():
    """
    模板匹配，大图中找小图
    """
    src = cv.imread("lena.jpg")
    tem = cv.imread("tem.png")
    cv.imshow("src", src)
    cv.imshow("tem", tem)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tem.shape[:2]
    for md in methods:
        result = cv.matchTemplate(src, tem, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw, tl[1]+th)
        cv.rectangle(src, tl, br, (0, 0, 255), 2)
        cv.imshow("match"+np.str(md), src)


# src = cv.imread(r"D:\testgit\Learn\Image\picture\src.png")
# cv.namedWindow("src", cv.WINDOW_NORMAL)
# cv.imshow("src", src)
template_demo()
cv.waitKey(0)
cv.destroyAllWindows()

