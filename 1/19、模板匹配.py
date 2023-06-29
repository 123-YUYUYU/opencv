from pipes import Template
from cv2 import threshold
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("1.jpg")
plt.imshow(img[:,:,::-1])
plt.show()
#模板匹配
template = cv.imread("4.jpg")
plt.imshow(template[:,:,::-1])
plt.show()
res = cv.matchTemplate(img,template,cv.TM_CCOEFF)
plt.imshow(res,cmap=plt.cm.gray)
plt.show()
min_val,max_val,min_loc,max_loc = cv.minMaxLoc(res)
top_left = max_loc
h,w = template.shape[:2]
bottom_right = (top_left[0]+w,top_left[1]+h)
cv.rectangle(img,top_left,bottom_right,(0,255,0),2)
plt.imshow(img[:,:,::-1])
plt.show()





# API
# res = cv.matchTemplate(img,template,method)     模板匹配
# img:要进行模板匹配的图像
# Template：模板
# method：实现模板匹配的算法：平方差匹配（CV_TM_SQDIFF） 相关匹配（CV_TM_CCORR）利用相关系数匹配（CV+TM_CCOEFF）
# 完成匹配后，使用cv.minMaxLoc()查找最大值所在位置 若使用平方差作为比较方法则最小值位置是最佳匹配位置。

# 霍夫线检测
# cv.HonghLines(img, rho， theta, threshold)
# img:检测的图像
# rho、theta:ρ和0的精确值
# threshold：阈值累加器中高于该阈值才被认作为直线
