from tkinter import CENTER
from cv2 import getRotationMatrix2D
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("1.jpg")
rows,cols = img.shape[:2]
M = cv.getRotationMatrix2D((cols/2,rows/2),15,0.70)
dst = cv.warpAffine(img,M,(cols,rows))
plt.imshow(dst[:,:,::-1])
plt.show()



# API
# cv2.getRotationMatrix2D(center,angle,scale)
# center：旋转中心
# angle：旋转角度
# scale 缩放比例
