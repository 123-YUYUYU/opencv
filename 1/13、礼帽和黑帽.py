import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread("2.jpg")
plt.imshow(img1[:,:,::-1])
plt.show()

kenel = np.ones((10,10),np.uint8)

top = cv.morphologyEx(img1,cv.MORPH_TOPHAT,kenel)
plt.imshow(top[:,:,::-1])
plt.show()

black = cv.morphologyEx(img1,cv.MORPH_BLACKHAT,kenel)
plt.imshow(black[:,:,::-1])
plt.show()


# 礼帽：原图像与开运算之差
# 黑帽：原图像与闭运算之差
