############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img = cv2.imread('ey1.jpg')
############################################

############################################
## Do the processing
##############################

#Getting the certroid of yellow provision
param1 = [50,150,100]
param2 = [150,255,255]
lower = np.array(param1)
upper = np.array(param2)
mask  = cv2.inRange(img,lower, upper)
res1   = cv2.bitwise_and(img, img, mask= mask)
gray = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
blur3 = cv2.medianBlur(thresh1,15)
contours, hierarchy = cv2.findContours(blur3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(res1,contours,-1,(0,255,0),3)
print len(contours)
M1 = cv2.moments(contours[0])
cyx1 = int(M1['m10']/M1['m00'])
cyy1 = int(M1['m01']/M1['m00'])
print cyx1,cyy1
M2 = cv2.moments(contours[1])
cyx2 = int(M2['m10']/M2['m00'])
cyy2 = int(M2['m01']/M2['m00'])
print cyx2,cyy2
#cv2.circle(img,(cyx1,cyy1), 5, (0,255,0), -1)
#cv2.circle(img,(cyx2,cyy2), 5, (0,255,0), -1)
####################################################
#Getting the certroid of red provision
param1 = [0,0,225]
param2 = [200,200,255]
lower = np.array(param1)
upper = np.array(param2)
mask  = cv2.inRange(img,lower, upper)
res1   = cv2.bitwise_and(img, img, mask= mask)
gray = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
blur3 = cv2.medianBlur(thresh1,15)
contours, hierarchy = cv2.findContours(blur3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(res1,contours,-1,(0,255,0),3)
print len(contours)
M1 = cv2.moments(contours[0])
crx1 = int(M1['m10']/M1['m00'])
cry1 = int(M1['m01']/M1['m00'])
print crx1,cry1
M2 = cv2.moments(contours[1])
crx2 = int(M2['m10']/M2['m00'])
cry2 = int(M2['m01']/M2['m00'])
print crx2,cry2
#cv2.circle(img,(crx1,cry1), 5, (0,255,0), -1)
#cv2.circle(img,(crx2,cry2), 5, (0,255,0), -1)
################################################
#Getting the certroid of blue provision
param1 = [100,0,0]
param2 = [255,100,100]
lower = np.array(param1)
upper = np.array(param2)
mask  = cv2.inRange(img,lower, upper)
res1   = cv2.bitwise_and(img, img, mask= mask)
gray = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
blur3 = cv2.medianBlur(thresh1,15)
contours, hierarchy = cv2.findContours(blur3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(res1,contours,-1,(0,255,0),3)
print len(contours)
M1 = cv2.moments(contours[0])
cbx1 = int(M1['m10']/M1['m00'])
cby1 = int(M1['m01']/M1['m00'])
print cbx1,cby1
M2 = cv2.moments(contours[1])
cbx2 = int(M2['m10']/M2['m00'])
cby2 = int(M2['m01']/M2['m00'])
print cbx2,cby2
#cv2.circle(img,(cbx1,cby1), 5, (0,255,0), -1)
#cv2.circle(img,(cbx2,cby2), 5, (0,255,0), -1)

m=cyx1%40;
cyx1=cyx1-m-40;
m=cyy1%40;
cyy1=cyy1-m;
m=cyx2%40;
cyx2=cyx2+(40-m);
m=cyy2%40;
cyy2=cyy2+(40-m);
m=cbx1%40;
cbx1=cbx1+(40-m);
m=cby1%40;
cby1=cby1-m;
m=cbx2%40;
cbx2=cbx2-m-40;
m=cby2%40;
cby2=cby2+(40-m);
m=crx1%40;
crx1=crx1+(40-m);
m=cry1%40;
cry1=cry1-m;
m=crx2%40;
crx2=crx2-m-40;
m=cry2%40;
cry2=cry2+(40-m);

cv2.circle(img,(cbx1,cby1), 5, (0,255,0), -1)
cv2.circle(img,(cbx2,cby2), 5, (0,255,0), -1)
cv2.circle(img,(cbx1,cby1), 5, (0,255,0), -1)
cv2.circle(img,(cbx2,cby2), 5, (0,255,0), -1)

cv2.circle(img,(cyx1,cyy1), 5, (0,255,0), -1)
cv2.circle(img,(cyx2,cyy2), 5, (0,255,0), -1)
cv2.circle(img,(cyx1,cyy1), 5, (0,255,0), -1)
cv2.circle(img,(cyx2,cyy2), 5, (0,255,0), -1)

cv2.circle(img,(crx1,cry1), 5, (0,255,0), -1)
cv2.circle(img,(crx2,cry2), 5, (0,255,0), -1)
cv2.circle(img,(crx1,cry1), 5, (0,255,0), -1)
cv2.circle(img,(crx2,cry2), 5, (0,255,0), -1)

print cyx1,cyy1,cyx2,cyy2;
print cbx1,cby1,cbx2,cby2;
print crx1,cry1,crx2,cry2;
############################################
#Shortest path

############################################
## Show the image
cv2.imshow('image1',mask)
#cv2.imshow('image2',res2)
cv2.imshow('image',img)
############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
