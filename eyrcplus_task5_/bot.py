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
#position of bot
#position of bot
gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh2 = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
ret,thresh6 = cv2.threshold(thresh2,150,255,cv2.THRESH_BINARY_INV)
ret,thresh1 = cv2.threshold(thresh6,210,255,cv2.THRESH_BINARY)
blur3 = cv2.medianBlur(thresh1,25)
ret,thresh = cv2.threshold(blur3,210,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print len(contours)
#cv2.drawContours(img,contours ,1,(0,255,0),3)
#M1 = cv2.moments(contours[1])
#cbotx = int(M1['m10']/M1['m00'])
#cboty = int(M1['m01']/M1['m00'])
#print cbotx,cboty
#cv2.circle(img,(cbotx,cboty), 5, (0,255,0), -1)
####################################################
## Show the image
cv2.imshow('blur3',blur3)
#cv2.imshow('gray',thresh6)
#cv2.imshow('thresh1',thresh1)
cv2.imshow('image',img)

############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
