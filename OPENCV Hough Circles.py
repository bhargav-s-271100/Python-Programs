import os
import cv2
import numpy as np
a=os.getcwd()
b=os.path.dirname(a)
path=os.path.join(b,'Images','image_1.png')
print(path)
input=cv2.imread(path)
cv2.imshow('Original_image',input)
cv2.waitKey(0)
gray=cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)
blur=cv2.medianBlur(gray,5)
circles=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,50,param1=50,param2=30,minRadius=100,maxRadius=300)
detected_circles=np.uint16(np.around(circles))
for (x,y,r) in detected_circles[0,:]:
    cv2.circle(gray,(x,y),r,(255,0,0),5)
cv2.imshow("output",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
