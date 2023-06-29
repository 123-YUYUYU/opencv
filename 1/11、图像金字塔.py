import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread("1.jpg")
plt.imshow(img1[:,:,::-1])
plt.show()
imgup = cv.pyrUp(img1)
plt.imshow(imgup[:,:,::-1])
plt.show()
imgup2 = cv.pyrUp(imgup)
plt.imshow(imgup2[:,:,::-1])
plt.show()
imgdown = cv.pyrDown(img1)
plt.imshow(imgdown[:,:,::-1])
plt.show()



# cv.pyrUp(img)     对图像进行上采样
# cv.pyrDown(img)   对图像进行下采样    