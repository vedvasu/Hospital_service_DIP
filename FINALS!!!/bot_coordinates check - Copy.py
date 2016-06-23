## Import OpenCV
import numpy as np
import cv2
import serial
import time         

img = cv2.imread('o1.jpg')
param1 = [0,80,80]                                 #parameters for yellow colour range
param2 = [100,255,255]
lower = np.array(param1)
upper = np.array(param2)
mask  = cv2.inRange(img,lower, upper)
res1   = cv2.bitwise_and(img, img, mask= mask)
gray = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
blur3 = cv2.medianBlur(thresh1,15)
contours, hierarchy = cv2.findContours(blur3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
l=len(contours)
yellow_marker=[]
yellow_bed=[]
for i in range(0,l):
    M1 = cv2.moments(contours[i])                            
    cyx = int(M1['m10']/M1['m00'])
    cyy = int(M1['m01']/M1['m00'])
    if(cyx<200):
        if(cyx>0)&(cyx<240)&(cyy>0)&(cyy<160):
            cyx=160
            cyy=80
            yellow_marker.append(cyx)
            yellow_marker.append(cyy)
        elif(cyx>0)&(cyx<240)&(cyy>200)&(cyy<320):
             cyx=160
             cyy=280
             yellow_marker.append(cyx)
             yellow_marker.append(cyy)
        elif(cyx>0)&(cyx<240)&(cyy>320)&(cyy<480):
             cyx=160
             cyy=440
             yellow_marker.append(cyx)
             yellow_marker.append(cyy)
    else:
        if(cyx>320)&(cyx<640)&(cyy>0)&(cyy<160):
            cyx=400
            cyy=160
            yellow_bed.append(cyx)
            yellow_bed.append(cyy)
        elif(cyx>320)&(cyx<640)&(cyy>200)&(cyy<320):
             cyx=400
             cyy=280
             yellow_bed.append(cyx)
             yellow_bed.append(cyy)
        elif(cyx>320)&(cyx<640)&(cyy>320)&(cyy<480):
             cyx=400
             cyy=440
             yellow_bed.append(cyx)
             yellow_bed.append(cyy)
print yellow_marker,yellow_bed
cv2.imshow('blur3',blur3)
cv2.imshow('mask',mask)
cv2.imshow('thresh1',thresh1)

cv2.waitKey(0)
cv2.destroyAllWindows()
