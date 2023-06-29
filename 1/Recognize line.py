import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

Width = 640*0.5
Height = 480*0.5
cap = cv.VideoCapture(0)   #获取摄像头信息
cap.set(3, Width)
cap.set(4, Height)
cap.set(10,150)

def find_lines():



if __name__ == "__main__":
    while True:
        id,frame = cap.read()
        frame = cv.flip(frame, 1)
        img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        find_lines(frame)
