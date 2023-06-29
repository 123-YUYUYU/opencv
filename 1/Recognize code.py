import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import pyzbar.pyzbar as pyzbar
from pyzbar.pyzbar import decode

Width = 640*0.5
Height = 480*0.5
cap = cv.VideoCapture(0)   #获取摄像头信息
cap.set(3, Width)
cap.set(4, Height)
cap.set(10,150)

def code(image):
    # img = pyzbar.decode(image)
    for barcode in decode(image):                       #循环检测到的信息
        myData=barcode.data.decode('utf-8')             #解码(utf—8:编码格式)
        pts=np.array([barcode.polygon],np.int32)        #转化成数组
        pts=pts.reshape((-1,1,2))                       #矩阵变成4*1*2维
        cv.polylines(frame,[pts],True,(0, 0, 255), 4)   #传入所画多边形的顶点坐标
        barcodeType = barcode.type
        print("{},{}".format(barcodeType,myData))
        print(myData)                                   #输出识别码的结果
        # pts2=barcode.rect
        # cv.putText(frame,myData,(pts2[0],pts2[1]),cv.FONT_HERSHEY_SIMPLEX,0.9,(255, 0,255),2)
        #在摄像头内输出二维码信息
    cv.imshow('Camera',frame)
    cv.waitKey(1)
        

if __name__ == "__main__":
    while True:
        id,frame = cap.read()
        frame = cv.flip(frame, 1)
        img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        code(img)
