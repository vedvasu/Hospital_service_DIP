############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img = cv2.imread('output_image.jpg')
############################################

############################################
## Do the processing
##############################

####################################################
#Getting the certroid of blue provision
param1 = [100,0,0]
param2 = [255,100,100]

lower = np.array(param1)
upper = np.array(param2)
#mask  = cv2.inRange(img,lower, upper)
#res1   = cv2.bitwise_and(img, img, mask= mask)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC_INV)
blur3 = cv2.medianBlur(thresh1,15)
contours, hierarchy = cv2.findContours(blur3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,0),3)
print len(contours)
#M1 = cv2.moments(contours[0])
#cbx1 = int(M1['m10']/M1['m00'])
#cby1 = int(M1['m01']/M1['m00'])
#print cbx1,cby1
#M2 = cv2.moments(contours[1])
#cbx2 = int(M2['m10']/M2['m00'])
#cby2 = int(M2['m01']/M2['m00'])
#print cbx2,cby2
#cv2.circle(img,(cbx1,cby1), 5, (0,255,0), -1)
#cv2.circle(img,(cbx2,cby2), 5, (0,255,0), -1)
####################################################
## Show the image
cv2.imshow('blur3',blur3)
#cv2.imshow('mask',mask)
cv2.imshow('gray',gray)
#cv2.imshow('thresh1',thresh1)
#cv2.imshow('res1',res1)
cv2.imshow('image',img)

############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
