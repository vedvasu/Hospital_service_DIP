############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img = cv2.imread('s.jpg')
############################################

############################################
## Do the processing
##############################
#Getting the certroid of blue provision
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
cv2.drawContours(res1,contours,-1,(0,255,0),3)
M1 = cv2.moments(contours[0])
cbx1 = int(M1['m10']/M1['m00'])
cby1 = int(M1['m01']/M1['m00'])
print cbx1,cby1
M2 = cv2.moments(contours[1])
cbx2 = int(M2['m10']/M2['m00'])
cby2 = int(M2['m01']/M2['m00'])
print cbx2,cby2
####################################################
##############################
#Getting the certroid of red provision
param1 = [50,200,200]
param2 = [255,255,255]
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower = np.array(param1)
upper = np.array(param2)
mask  = cv2.inRange(hsv, lower, upper)
res1   = cv2.bitwise_and(img, img, mask= mask)
gray = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(res1,contours,-1,(0,255,0),3)
M1 = cv2.moments(contours[0])
crx1 = int(M1['m10']/M1['m00'])
cry1 = int(M1['m01']/M1['m00'])
print crx1,cry1
M2 = cv2.moments(contours[1])
crx2 = int(M2['m10']/M2['m00'])
cry2 = int(M2['m01']/M2['m00'])
print crx2,cry2
####################################################
#Getting the certroid of yellow provision
param1 = [0,200,200]
param2 = [0,255,255]
lower = np.array(param1)
upper = np.array(param2)
mask  = cv2.inRange(img, lower, upper)
res1   = cv2.bitwise_and(img, img, mask= mask)
gray = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(res1,contours,-1,(0,255,0),3)
M1 = cv2.moments(contours[0])
cyx1 = int(M1['m10']/M1['m00'])
cyy1 = int(M1['m01']/M1['m00'])
print cyx1,cyy1
M2 = cv2.moments(contours[1])
cyx2 = int(M2['m10']/M2['m00'])
cyy2 = int(M2['m01']/M2['m00'])
print cyx2,cyy2
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
