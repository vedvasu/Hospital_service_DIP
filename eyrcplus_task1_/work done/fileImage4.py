# -*- coding: cp1252 -*-
############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img = cv2.imread('2.jpg')
############################################

############################################
## Do the processing
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh2 = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
ret,thresh3 = cv2.threshold(gray,145,255,cv2.THRESH_BINARY)
blur3 = cv2.medianBlur(thresh2,33)
ret,thresh = cv2.threshold(blur3,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
M = cv2.moments(contours[1])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
blur2 = cv2.medianBlur(thresh3,25)
ret,thresh = cv2.threshold(blur2,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
M = cv2.moments(contours[1])
cx1 = int(M['m10']/M['m00'])
cy1 = int(M['m01']/M['m00'])
m1=cy-cy1
m2=cx-cx1
if cx1-5*m2<65:
    letter = 'L'
elif  65<cx1-5*m2<135:
    letter = 'M'
elif  135<cx1-5*m2<205:
    letter = 'N'
elif  205<cx1-5*m2<275:
    letter = 'O'
elif  275<cx1-5*m2<345:
    letter = 'P'
elif  345<cx1-5*m2<415:
    letter = 'Q'
elif  415<cx1-5*m2<485:
    letter = 'R'
elif  485<cx1-5*m2<555:
    letter = 'S'
elif  555<cx1-5*m2<625:
    letter = 'T'
elif  625<cx1-5*m2<695:
    letter = 'U'
elif  695<cx1-5*m2<765:
    letter = 'V'

print letter
############################################

############################################
## Show the image
cv2.imshow('image',img)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
