############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img = cv2.imread('d.png')
############################################

############################################
## Do the processing
##############################
#Getting the certroid of blue color(Starting point)
param1 = [80,100,150]
param2 = [130,200,255]
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower = np.array(param1)
upper = np.array(param2)
mask  = cv2.inRange(hsv, lower, upper)
res1   = cv2.bitwise_and(img, img, mask= mask)
gray = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(res1,contours,0,(0,255,0),3)
M = cv2.moments(contours[0])
cx1 = int(M['m10']/M['m00'])
cy1 = int(M['m01']/M['m00'])
print cx1,cy1
###############################
#Getting the certroid of green color(End point)
param1 = [50,100,100]
param2 = [80,255,255]
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower = np.array(param1)
upper = np.array(param2)
mask  = cv2.inRange(hsv, lower, upper)
res2   = cv2.bitwise_and(img, img, mask= mask)
gray = cv2.cvtColor(res2,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(res2,contours,0,(0,255,0),3)
M = cv2.moments(contours[0])
cx2 = int(M['m10']/M['m00'])
cy2 = int(M['m01']/M['m00'])
print cx2,cy2
############################################
#finding the smllest path
param1 = [50,200,200]
param2 = [255,255,255]
lower = np.array(param1)
upper = np.array(param2)
start = [cx1,cy1]
path = []
path.append(start)
print path
z=1
m=0
x=1
for z1 in range (0,10):
    print m,x
    for z2 in range (m,x,2):
        #print start[z2]
        #print start[z2+1]
        cxa = start[z2]+40
        cya = start[z2+1]
        start.append(cxa)
        start.append(cya)
        if z2==x-1:
            cxb = start[z2]
            cyb = start[z2+1]+40
            start.append(cxb)
            start.append(cyb)
        cv2.circle(img,(cxa,cya),2,(255,0,0),-1)
        cv2.circle(img,(cxb,cyb),2,(0,255,0),-1)
    m=m+2*z
    z=z+1
    x=x+2*z
print start    
####################################################
## Show the image
#cv2.imshow('image1',res1)
#cv2.imshow('image2',res2)
cv2.imshow('image',img)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
