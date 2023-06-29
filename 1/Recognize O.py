import numpy as np 
import cv2 
import matplotlib.pyplot as plt

Width = 640*0.5
Height = 480*0.5
cap = cv2.VideoCapture(0)   #获取摄像头
cap.set(3, Width)
cap.set(4, Height)
cap.set(10,150)        #调节亮度

def find_circle(image):
    try:
        circle = cv2.HoughCircles(cvopen,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=30)
        circle = np.uint16(np.around(circle))
        for i in circle[0]:
           cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
           cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
    except:
        pass
    
   # image1 = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)     
    cv2.imshow("result",frame)
    cv2.waitKey(1)

        
if __name__ == "__main__":
    while True:
        id,frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray1 = cv2.GaussianBlur(gray,(5,5),1)
        kenel = np.ones((5,5),np.uint8)
        cvopen = cv2.morphologyEx(gray1,cv2.MORPH_OPEN,kenel)
        find_circle(cvopen)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()