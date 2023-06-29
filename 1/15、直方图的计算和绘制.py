import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("2.jpg",0)
plt.imshow(img,cmap= plt.cm.gray)
plt.show()

img1 = cv.calcHist([img],[0],None,[256],[0,256])
plt.figure(figsize=(10,8))
plt.plot(img1)
plt.show()



# API
# cv2.calcHist(images,channels,mask,histSize,ranges[,hist[,accumlate]])
# images：原图像，传入函数时用中括号括起来
# channels：若输入图像是灰度图：0  若为彩色可为[0],[1],[2]它们对应B，G，R
# mask：掩模图像，一般统计整幅图像的直方图就设为None
# histSize：BIN的数目，需用中括号括起来
# ranges；像素值范围，[0，256]