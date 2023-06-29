from cv2 import CLAHE
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("2.jpg",0)
plt.imshow(img,cmap=plt.cm.gray)
plt.show()
dst = cv.equalizeHist(img)
plt.imshow(dst,cmap=plt.cm.gray)
plt.show()

# 自适应直方图均衡化
cl = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe = cl.apply(img)
plt.imshow(clahe,cmap=plt.cm.gray)
plt.show()



# API
# dst = cv.equalizeHist(img)
# img:灰度图像
# dst：均衡化后的结果

# cv.createCLAHE(clipLimit, tileGridSize) 自适应均衡化
# clipLimit：对比度限制，默认值是40
# tileGridSize：分块的大小，默认8*8
