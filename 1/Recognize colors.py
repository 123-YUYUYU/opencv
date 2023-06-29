import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

Width = 640*0.5
Height = 480*0.5
cap = cv.VideoCapture(0)   #获取摄像头信息
cap.set(3, Width)
cap.set(4, Height)
cap.set(10,150)

ball_color = 'red'
color_dist={
                'red': {'low': np.array([151, 106, 159]), 'high': np.array([179, 225, 255])},
             'orange': {'low': np.array([  6,  81, 159]), 'high': np.array([ 57, 150, 255])},
              'green': {'low': np.array([ 66, 105,  10]), 'high': np.array([ 83, 255, 255])},
               'blue': {'low': np.array([ 96, 125, 160]), 'high': np.array([134, 255, 255])},
             'purple': {'low': np.array([138,  60,  95]), 'high': np.array([152, 220, 255])},
             'yellow': {'low': np.array([ 15, 110, 170]), 'high': np.array([ 83, 255, 255])}
            }
def find_color(image):
        kernel = np.ones((5,5),np.uint8)   #定义滤波函数
        mask = cv.erode(image,kernel=kernel,iterations=2)  #图像腐蚀
        mask = cv.dilate(mask,kernel=kernel,iterations=1)  #图像膨胀
        mask = cv.inRange(image,color_dist[ball_color]['low'], color_dist[ball_color]['high'])              #用以确认元素值是否介于某个区域
        cnts = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]    #查找轮廓的图像
        try:
            are_max = max(cnts, key=cv.contourArea)     #计算轮廓面积
            rect = cv.minAreaRect(are_max)   #该函数是找轮廓函数返回轮廓数组后，绘制每个轮廓的最小外接矩形的方法
            box = cv.boxPoints(rect)        #获取该矩形的四个顶点坐标
            left_point_x = np.min(box[:, 0])
            right_point_x = np.max(box[:, 0])
            top_point_y = np.min(box[:, 1])
            bottom_point_y = np.max(box[:, 1])
            mid_point_x = (left_point_x + right_point_x)/2
            mid_point_y = (top_point_y + bottom_point_y)/2
            print("mid_point= %.2f,%.2f"%(mid_point_x,mid_point_y))
            cv.drawContours(frame, [np.int0(box)], -1, (0, 255, 255), 2)   #用于轮廓的绘制或填充
        except:
            pass
        # plt.imshow(image[:,:,::-1])
        # plt.show()  
        cv.imshow('camera', frame)
        cv.waitKey(1)
if __name__ == "__main__":
    while True:
        id,frame = cap.read()
        image = cv.GaussianBlur(frame, (5, 5), 0)      #返回进行高斯滤波处理过的结果
        imgHSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)  #返回从一种颜色空间到另一种颜色空间
        find_color(imgHSV)


