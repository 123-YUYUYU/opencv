import imghdr
from cv2 import COLOR_BAYER_BG2GRAY
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
A = cv.imread("lena.jpg")
plt.imshow(A[:,:,::-1])
plt.show()
b,g,r = cv.split(A) 
plt.imshow(b,cmap=plt.cm.gray)
plt.show() 
img2 = cv.merge((b,g,r))
plt.imshow(img2[:,:,::-1])
plt.show()
gray = cv.cvtColor(A,cv.COLOR_BGR2GRAY)
plt.imshow(gray,cmap=plt.cm.gray)            
plt.show()
hsv = cv.cvtColor(A,cv.COLOR_BGR2HSV)
plt.imshow(hsv)
plt.show()