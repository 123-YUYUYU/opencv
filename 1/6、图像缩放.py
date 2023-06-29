from configparser import Interpolation
from termios import FFDLY
from turtle import ScrolledCanvas
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from qtpy import API

img1 = cv.imread("1.jpg")
plt.imshow(img1[:,:,::-1])
plt.show()
rows,cols = img1.shape[:2]
res = cv.resize(img1,(2*cols,2*rows))
plt.imshow(res[:,:,::-1])
plt.show()
res1 = cv.resize(img1,None,fx=0.5,fy=0.5)
plt.imshow(res1[:,:,::-1])
plt.show()



# API
# cv2.resize(src,dsize,fx=_,fy_,Interpolation=cv2.INTER_LINEAR)
# Scr：输入图像
# dsize：绝对尺寸，直接指定调整后图像的大小
# fx,fy：相对尺寸，将dsize设置为None，然后将fx，fy，设置为比例因子即可
# Interpolation：插值方法