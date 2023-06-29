import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("1.jpg")

rows,cols = img.shape[:2]
img1 = np.float32([[50,50],[200,50],[50,200]])
img2 = np.float32([[100,100],[200,50],[100,250]])

M = cv.getAffineTransform(img1,img2)

img3 = cv.warpAffine(img,M,(cols,rows))
plt.imshow(img[:,:,::-1])
plt.show()