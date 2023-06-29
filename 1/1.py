import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# 1 读取图像
img = cv.imread("1.jpg")  #读取当前路径下的图像文件lena,jpg
# cv.imshow("1.jpg",img)        
# cv.waitKey(0)                #等待用户输入
# cv.destroyAllWindows()       #用户一旦输入任意键后，程序关闭窗口

# # 1.2matplotlib
plt.imshow(img[:,:,::-1])
plt.show()