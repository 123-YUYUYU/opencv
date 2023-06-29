from turtle import ScrolledCanvas
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

dogsp = cv.imread("3.jpg")
plt.imshow(dogsp[:,:,::-1])
plt.show()

dog = cv.blur(dogsp,(5,5))
plt.imshow(dog[:,:,::-1])
plt.show()

dog2 = cv.GaussianBlur(dogsp,(5,5),1)
plt.imshow(dog2[:,:,::-1])
plt.show()

dog3 = cv.medianBlur(dogsp,5)
plt.imshow(dog3[:,:,::-1])
plt.show()




# cv.blur(src,ksize,anchor,borderType)   /均值滤波
# src：输入图像
# ksize：卷积核的大小
# anchor:默认值（-1，-1），表示核中心
# borderType：边界类型

# cv2.GaussianBlur(src,ksize,sigmax,sigmaX,sigmay,borderType)  高斯滤波
# src：输入图像
# ksize：高斯卷积核的大小 注：卷积核的宽度和高度都应为奇数且可以不同 
# sigmaX：水平方向的标准差
# sigmaY：垂直方向的标准差。默认值为0，表示与sigmaX相同 
# borderType：填充边界类型

# cv.medianBlur(src,ksize)  中值滤波
# src：输入图像
# ksize：卷积核的大小

