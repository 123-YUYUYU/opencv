import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("2.jpg")
plt.imshow(img[:,:,::-1])
plt.show()

rows,cols = img.shape[:2]

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[100,145],[300,100],[80,290],[310,300]])

T = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,T,(cols,rows))
plt.imshow(dst[:,:,::-1])
plt.show()