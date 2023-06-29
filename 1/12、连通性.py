from fileinput import close
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("2.jpg")
plt.imshow(img[:,:,::-1])
plt.show()
# 腐蚀与膨胀
kenel = np.ones((5,5),np.uint8)     #新建和结构
img2 = cv.erode(img,kenel)
plt.imshow(img2[:,:,::-1])
# plt.show()
img1 = cv.dilate(img,kenel)
plt.imshow(img1[:,:,::-1])
# plt.show()

#开闭运算
cvopen = cv.morphologyEx(img1,cv.MORPH_OPEN,kenel)
plt.imshow(cvopen[:,:,::-1])
plt.show()

cvclose = cv.morphologyEx(img1,cv.MORPH_CLOSE,kenel)
plt.imshow(cvclose[:,:,::-1])
plt.show()



# 腐蚀：求局部最大值
# 膨胀：求局部最小值

# 开运算：先腐蚀再膨胀
# 闭运算：先膨胀再腐蚀


# API
# cv.morphologyEx(img,op,kernel)
# img：要处理的图像
# op：处理方式
# cv.MORPH_CLOSE    闭运算
# cv.MORPH_OPEN     开运算
# cv.MORPH_TOPHAT   礼帽运算
# cv.MORPH_BLACKHAT 黑帽运算