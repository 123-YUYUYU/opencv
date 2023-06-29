import imp
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt 
import pytesseract
import os

Width = 640*0.5
Height = 480*0.5
cap = cv.VideoCapture(0)   #获取摄像头信息
cap.set(3, Width)
cap.set(4, Height)
cap.set(10,150)
mid_point_x = 0
mid_point_y = 0

def find_A(image): 
    # pytesseract.pytesseract.tesseract_cmd = "D:\OCR\\tesseract.exe"
    os.environ['TESSDATA_PREFIX'] = 'D:\\OCR\\tessdata'
    H,W = image.shape[:2]
    boxes = pytesseract.image_to_boxes(image)
    for box in boxes.splitlines():
        if box[0] =='A':
            b = box.split(' ')
            x, y, w, h  = int(b[1]), int(b[2]),  int(b[3]), int(b[4])
            cv.rectangle(frame, (x, H-y), (w, H-h),(0, 0, 255), 2 )
            mid_point_x = (x + w)/2
            mid_point_y = ((H-y) + (H-h))/2
            print("mid_point= %.2f,%.2f"%(mid_point_x,mid_point_y))
    cv.imshow("camera",frame)
    cv.waitKey(1)    

if __name__ == "__main__":
    while True:


        id,frame = cap.read()
        img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame = cv.flip(frame,1)
        find_A(img)


