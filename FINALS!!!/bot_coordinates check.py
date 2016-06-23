## Import OpenCV
import numpy as np
import cv2
import serial
import time         

img = cv2.imread('b.jpg')
b1,g1,r1=img[80,280]
print b1,g1,r1
b2,g2,r2=img[240,280]
print b2,g2,r2
b3,g3,r3=img[440,280]
print b3,g3,r3
if(b1<b2):
    if(b3<b1):
        small=b3
    elif(b3>b1):
        small=b1
  
elif(b1>b2):
    if(b3<b2):
        small=b3
    elif(b3>b2):
        small=b2
        
if(b1==small):
    cbotx=280
    cboty=80
elif(b2==small):
    cbotx=280
    cboty=240
elif(b3==small):
    cbotx=280
    cboty=440
print b1,g1,r1   
cv2.circle(img,(cbotx,cboty), 5, (0,255,0), -1)
print cbotx,cboty

cv2.imshow('blur',thresh2)
cv2.imshow('image',thresh6)

cv2.imshow('blur',blur3)
cv2.imshow('image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()
