import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


img1 = cv.imread("1.jpg")
plt.imshow(img1[:,:,::-1])
plt.show()
M = np.float32([[1,0,100],[0,1,50]])
rows,cols = img1.shape[:2]
res2 = cv.warpAffine(img1,M,(2*rows,2*cols))
plt.imshow(res2[:,:,::-1])
plt.show()




# API
# cv.warpAffine(img,M,dsize)
# img：输入图像
# M：2*3移动矩阵
# dsize：输出图像的大小