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
a=10
b=10
print cmp(a,b)
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
