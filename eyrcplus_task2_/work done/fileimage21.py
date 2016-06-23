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
i=2
param1 = [50,100,100]
param2 = [80,255,255]
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower = np.array(param1)    ## Convert the parameters into a form that OpenCV can understand
upper = np.array(param2)
mask  = cv2.inRange(hsv, lower, upper)           ## Detecting
res1   = cv2.bitwise_and(img, img, mask= mask)

#gray = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
#ret,thresh = cv2.threshold(gray,127,255,0)
#ret,thresh2 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
#ret,thresh3 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
#ret,thresh4 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
#ret,thresh5 = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO_INV)
#contours, hierarchy = cv2.findContours(thresh3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(res1,contours,0,(0,255,0),3)
#print len(contours)
############################################

############################################
## Show the image
#cv2.imshow('image',thresh)
#cv2.imshow('image2',thresh2)
#cv2.imshow('image3',thresh3)
#cv2.imshow('image4',thresh4)
#cv2.imshow('image5',thresh5)
cv2.imshow('image00',res1)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
