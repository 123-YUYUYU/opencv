from cv2 import Canny, Laplacian
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("2.jpg",0)
plt.imshow(img,cmap=plt.cm.gray)
plt.show()
# Sobel算子
x = cv.Sobel(img,cv.CV_16S, 1, 0)
y = cv.Sobel(img,cv.CV_16S, 0, 1)
absx = cv.convertScaleAbs(x)
absy = cv.convertScaleAbs(y)
res = cv.addWeighted(absx,0.5,absy,0.5,0)
plt.imshow(res,cmap=plt.cm.gray)
plt.show()
# Scharr算子
x = cv.Sobel(img,cv.CV_16S, 1, 0,ksize=-1)
y = cv.Sobel(img,cv.CV_16S, 0, 1,ksize=-1)
absx = cv.convertScaleAbs(x)
absy = cv.convertScaleAbs(y)
res = cv.addWeighted(absx,0.5,absy,0.5,0)
plt.imshow(res,cmap=plt.cm.gray)
plt.show()
# Laplacia
res = cv.Laplacian(img,cv.CV_16S)
res = cv.convertScaleAbs(res)
plt.imshow(res,cmap=plt.cm.gray)
plt.show()
# Canny
res = cv.Canny(img,0,100)
plt.imshow(res,cmap=plt.cm.gray)
plt.show()



# API 
# Sobel_x_or_y = cv2.Sobel(src,ddepth,dx,dy,dst,kszie,scale,delta,borderType) 
# src:传入的图像
# ddepth：图像的深度
# dx dy：求导的阶级 0~1
# ksize：Sobel算子的大小 卷积核的大小 当设为-1时就是利用Scharr进行边缘检测
# scale：缩放导数的比例常数
# borderType：图像边界的模式

# Laplacian = cv.Laplacian(src,ddepth[, dst[, ksize[, scale[, delta[,borderType]]]]])
# src :需要处理的图像
# Ddepth:图像的深度 -1表示与原图像相同的深度，目标图像的深度必须大于等于原图像的深度
# ksize:算子的大小，即卷积核的大小 奇数

# Canny
# 1、噪声去除（高斯滤波）
# 2、计算图像梯度
# 3、非极大值抑制
# 4、滞后阈值
# API
# canny = cv.Canny(image, threshold1, threshold2)
# image:
# thres