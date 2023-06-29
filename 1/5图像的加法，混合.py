import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from qtpy import API

img1 = cv.imread("1.jpg")
img2 = cv.imread("2.jpg")

img3 = cv.add(img1,img2)
img4 = img1+img2

img5 = cv.addWeighted(img1,0.7,img2,0.3,0)

plt.imshow(img3[:,:,::-1])
plt.show()
plt.imshow(img4[:,:,::-1])
plt.show()
plt.imshow(img5[:,:,::-1])
plt.show()



# API
