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
for z in range (1,20):
    cxa = cx1+40
    cya = cy1
    cxb = cx1
    cyb = cy1-40
    cxc = cx1-40
    cyc = cy1
    cxd = cx1
    cyd = cy1+40
    cv2.circle(img,(cxa,cya), 2, (0,0,255), -1)
    cv2.circle(img,(cxb,cyb), 2, (0,0,255), -1)
    cv2.circle(img,(cxc,cyc), 2, (0,0,255), -1)
    cv2.circle(img,(cxd,cyd), 2, (0,0,255), -1)
    print cxa,cya,cxb,cyb,cxc,cyc,cxd,cyd
    m1 = ((cxa-cx2)*(cxa-cx2))+((cya-cy2)*(cya-cy2))
    m2 = ((cxb-cx2)*(cxb-cx2))+((cyb-cy2)*(cyb-cy2))
    m3 = ((cxc-cx2)*(cxc-cx2))+((cyc-cy2)*(cyc-cy2))
    m4 = ((cxd-cx2)*(cxd-cx2))+((cyd-cy2)*(cyd-cy2))
    print m1,m2,m3,m4
    if (m1<=m2)&(m1<=m3)&(m1<=m4):
        cv2.line(img,(cx1,cy1),(cxa,cya),(0,255,0),2)
        cx1=cxa
        cy1=cya
    elif (m2<=m1)&(m2<=m3)&(m2<=m4):
        cv2.line(img,(cx1,cy1),(cxb,cyb),(0,255,0),2)
        cx1=cxb
        cy1=cyb
    elif (m3<=m2)&(m3<=m1)&(m3<=m4):
        cv2.line(img,(cx1,cy1),(cxc,cyc),(0,255,0),2)
        cx1=cxc
        cy1=cyc
    elif (m4<=m2)&(m4<=m3)&(m4<=m1):
        cv2.line(img,(cx1,cy1),(cxd,cyd),(0,255,0),2)
        cx1=cxd
        cy1=cyd
    print cx1
    z=z+1
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
