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
img = cv2.imread('7.jpg')
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

grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,threshit2 = cv2.threshold(grayscale,50,255,cv2.THRESH_BINARY)
ret,threshit3 = cv2.threshold(grayscale,145,255,cv2.THRESH_BINARY)
blur = cv2.medianBlur(threshit2,33)
ret,threshit = cv2.threshold(blur,127,255,0)
contours, hierarchy = cv2.findContours(threshit,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,-1,(0,255,0),3)

M = cv2.moments(contours[1])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print "Centroid = ", cx, ", ", cy

blur2 = cv2.medianBlur(threshit3,25)

ret,threshit = cv2.threshold(blur2,127,255,0)
contours, hierarchy = cv2.findContours(threshit,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours ,1,(0,255,0),3)
M = cv2.moments(contours[1])
cx1 = int(M['m10']/M['m00'])
cy1 = int(M['m01']/M['m00'])
print "Centroid = ", cx1, ", ", cy1

m1=cy-cy1
m2=cx-cx1
cv2.line(img,(cx,cy),(cx1-5*m2,cy1-5*m1),(255,0,0),3)
print "Centroid = ", cx, ", ", cy
print "Centroid = ", cx1, ", ", cy1
if cx1-5*m2<65:
    print 'L'
elif  65<cx1-5*m2<135:
    print 'M'
elif  135<cx1-5*m2<205:
    print 'N'
elif  205<cx1-5*m2<275:
    print 'O'
elif  275<cx1-5*m2<345:
    print 'P'
elif  345<cx1-5*m2<415:
    print 'Q'
elif  415<cx1-5*m2<485:
    print 'R'
elif  485<cx1-5*m2<555:
    print 'S'
elif  555<cx1-5*m2<625:
    print 'T'
elif  625<cx1-5*m2<695:
    print 'U'
elif  695<cx1-5*m2<765:
    print 'V'


############################################

############################################
## Show the image
cv2.imshow('image',img)
cv2.imwrite('test.jpg',img)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
