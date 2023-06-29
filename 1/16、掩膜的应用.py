import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("2.jpg",0)
plt.imshow(img,cmap=plt.cm.gray)
plt.show()
# 创建掩膜
mask = np.zeros(img.shape[:2],np.uint8)
mask[0:800, 750:1300] = 1
plt.imshow(mask,cmap=plt.cm.gray)
plt.show()
masked_img = cv.bitwise_and(img,img,mask=mask)
plt.imshow(masked_img,cmap=plt.cm.gray)
plt.show()
mask_hist = cv.calcHist([img],[0],mask,[256],[0,256])
plt.plot(mask_hist)
plt.show()

