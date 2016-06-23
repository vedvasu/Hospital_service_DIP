############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img = cv2.imread('500.jpg')
############################################

############################################
## Do the processing
#######################################
ret,thresh = cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
h,w,c =thresh.shape
z=0
c=0
print h,w
for i in range (0,h):
    for j in range (0,w):
        r,g,b = thresh[i,j]
        if (r==255)&(g==255)&(b==255):
            cx1=i
            cy1=j
            c=1
            break
    if c==1:
         break  
c=0
for i in range (w-1,0,-1):
    for j in range (h-1,0,-1):
        r,g,b = thresh[j,i]
        if (r==255)&(g==255)&(b==255):
            cx2=i
            cy2=j
            c=1
            break
    if c==1:
        break
cv2.rectangle(img,(cx1,cy1),(cx2,cy2),(0,0,0),5)
############################################
## Show the image
cv2.imshow('image',img)
cv2.imshow('image1',thresh)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
