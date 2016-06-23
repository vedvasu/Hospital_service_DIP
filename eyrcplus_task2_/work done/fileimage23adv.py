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
for z in range (1,20):
    cxa = cx1+40
    cya = cy1
    cxb = cx1
    cyb = cy1-40
    cxc = cx1-40
    cyc = cy1
    cxd = cx1
    cyd = cy1+40
    #cv2.circle(img,(cxa,cya), 2, (255,255,0), -1)
    #cv2.circle(img,(cxb,cyb), 2, (255,255,0), -1)
    #cv2.circle(img,(cxc,cyc), 2, (255,255,0), -1)
    #cv2.circle(img,(cxd,cyd), 2, (255,255,0), -1)
    print cxa,cya,cxb,cyb,cxc,cyc,cxd,cyd
    m1 = ((cxa-cx2)*(cxa-cx2))+((cya-cy2)*(cya-cy2))
    m2 = ((cxb-cx2)*(cxb-cx2))+((cyb-cy2)*(cyb-cy2))
    m3 = ((cxc-cx2)*(cxc-cx2))+((cyc-cy2)*(cyc-cy2))
    m4 = ((cxd-cx2)*(cxd-cx2))+((cyd-cy2)*(cyd-cy2))
    print m1,m2,m3,m4
    b1,g1,r1 =img[cxa,cya]
    b2,g2,r2 =img[cxb,cyb]
    b3,g3,r3 =img[cxc,cyc]
    b4,g4,r4 =img[cxd,cyd]
    small = [m1,m2,m3,m4]
    print b1,g1,r1,b2,g2,r2,b3,g3,r3,b4,g4,r4
    for i in range (0,3):
        for j in range (i+1,4):
            if small[i]>=small[j]:
                t=small[i]
                small[i]=small[j]
                small[j]=t
    print small            
    if b1==255 :
        cv2.line(img,(cx1,cy1),(cxa,cya),(0,0,255),2)
        cx1=cxa
        cy1=cya
    elif b4==255:
        cv2.line(img,(cx1,cy1),(cxd,cyd),(0,0,255),2)
        cx1=cxd
        cy1=cyd    
    elif b3==255:
        cv2.line(img,(cx1,cy1),(cxc,cyc),(0,0,255),2)
        cx1=cxc
        cy1=cyc
    elif b2==255:
        cv2.line(img,(cx1,cy1),(cxb,cyb),(0,0,255),2)
        cx1=cxb
        cy1=cyb
    z=z+1
    if (cx1==cx2)&(cy1==cy2):
        break
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
