# -*- coding: cp1252 -*-
'''
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2014)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Fundamentals
*  Filename: fileImage.py
*  Version: 1.0.0  
*  Date: November 3, 2014
*  
*  Author: Arun Mukundan, e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
'''

############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img = cv2.imread('1.jpg')
############################################

############################################
## Do the processing
img1 = np.zeros((475,770,3), np.uint8)

cv2.rectangle(img1,(5,10),(65,100),(255,255,255),-1)
cv2.rectangle(img1,(75,10),(135,100),(255,255,255),-1)
cv2.rectangle(img1,(145,10),(205,100),(255,255,255),-1)
cv2.rectangle(img1,(215,10),(275,100),(255,255,255),-1)
cv2.rectangle(img1,(285,10),(345,100),(255,255,255),-1)
cv2.rectangle(img1,(355,10),(415,100),(255,255,255),-1)
cv2.rectangle(img1,(425,10),(485,100),(255,255,255),-1)
cv2.rectangle(img1,(495,10),(555,100),(255,255,255),-1)
cv2.rectangle(img1,(565,10),(625,100),(255,255,255),-1)
cv2.rectangle(img1,(635,10),(695,100),(255,255,255),-1)
cv2.rectangle(img1,(705,10),(765,100),(255,255,255),-1)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh2 = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
ret,thresh3 = cv2.threshold(gray,145,255,cv2.THRESH_BINARY)
blur3 = cv2.medianBlur(thresh2,33)
ret,thresh = cv2.threshold(blur3,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,-1,(0,255,0),3)

M = cv2.moments(contours[1])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print "Centroid = ", cx, ", ", cy

blur2 = cv2.medianBlur(thresh3,25)

ret,thresh = cv2.threshold(blur2,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours ,1,(0,255,0),3)
M = cv2.moments(contours[1])
cx1 = int(M['m10']/M['m00'])
cy1 = int(M['m01']/M['m00'])
print "Centroid = ", cx1, ", ", cy1
cv2.line(img,(cx,cy),(cx1,cy1),(255,0,0),3)
print "Centroid = ", cx, ", ", cy
print "Centroid = ", cx1, ", ", cy1


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
