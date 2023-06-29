import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = np.zeros((256,256,3), np.uint8)
plt.imshow(img[:,:,::-1])
plt.show()
img[100,100] = (0,0,255)
plt.imshow(img[:,:,::-1])
plt.show()

