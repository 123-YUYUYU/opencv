import cv2
import numpy as np

Width = 640*0.5
Height = 480*0.5
cap = cv2.VideoCapture(0)
cap.set(3, Width)
cap.set(4, Height)
cap.set(10,150)

class Function():
    def __init__(self) -> None:
        # 自定义阈值  前三位为HSV的min   后三位为HSV的max
        self.pen_color = [[68,110,60],[255,0,255],[0,255,0]]
        #  自定义画笔颜色

    def find_color(self,image):
        low = np.array([87,53,197])
        high = np.array([107,255,255])
        kernel = np.ones((5,5),np.uint8)   #定义滤波函数
        mask = cv2.erode(image,kernel=kernel,iterations=2)  #图像腐蚀
        mask = cv2.dilate(mask,kernel=kernel,iterations=1)  #图像膨胀
        mask = cv2.inRange(image,low,high)              #用以确认元素值是否介于某个区域
        cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]    #查找轮廓的图像
        try:
            are_max = max(cnts, key=cv2.contourArea)     #计算轮廓面积
            rect = cv2.minAreaRect(are_max)   #该函数是找轮廓函数返回轮廓数组后，绘制每个轮廓的最小外接矩形的方法
            box = cv2.boxPoints(rect)        #获取该矩形的四个顶点坐标
            cv2.drawContours(image, [np.int0(box)], -1, (0, 255, 255), 2)   #用于轮廓的绘制或填充
        except:
            pass
        cv2.imshow('camera', image)
        cv2.waitKey(1)




if __name__ == "__main__":
    fun = Function()
    while True:
        id,frame = cap.read()
        image = cv2.GaussianBlur(frame, (5, 5), 0)      #返回进行高斯滤波处理过的结果
        imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  #返回从一种颜色空间到另一种颜色空间
        fun.find_color(imgHSV)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()     #删除建立的所有窗口

