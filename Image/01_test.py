# -*- coding: utf-8 -*-
# ---
# @Time: 2021/6/23
# @File: test.py
# @Author: Daqing Shi
# @Desc: Function of this file
# @update: Record important updates
# ---

import cv2 as cv

src = cv.imread(r"D:\testgit\Learn\Image\picture\src.png")
cv.namedWindow("src", cv.WINDOW_NORMAL)
cv.imshow("src", src)
cv.waitKey(0)
cv.destroyAllWindows()
