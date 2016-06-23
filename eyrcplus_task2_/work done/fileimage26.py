############################################
## Import OpenCV
import numpy as np
import cv2
############################################

############################################
## Read the image
img = cv2.imread('e.png')
############################################

############################################
## Do the processing
##############################
#Getting the certroid of blue color(Starting point)
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
cv2.drawContours(res1,contours,0,(0,255,0),3)
M = cv2.moments(contours[0])
cx1 = int(M['m10']/M['m00'])
cy1 = int(M['m01']/M['m00'])
print cx1,cy1
###############################
#Getting the certroid of green color(End point)
param1 = [50,100,100]
param2 = [80,255,255]
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower = np.array(param1)
upper = np.array(param2)
mask  = cv2.inRange(hsv, lower, upper)
res2   = cv2.bitwise_and(img, img, mask= mask)
gray = cv2.cvtColor(res2,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(res2,contours,0,(0,255,0),3)
M = cv2.moments(contours[0])
cx2 = int(M['m10']/M['m00'])
cy2 = int(M['m01']/M['m00'])
print cx2,cy2
############################################
#finding the smllest path
param1 = [50,200,200]
param2 = [255,255,255]
lower = np.array(param1)
upper = np.array(param2)
a=0
y=1
x=0
c=0
w=1
q=1
#c1=cx1
#c2=cy1
end =(cx2,cy2)
start =(cx1,cy1)
path_gp=[[(cx1,cy1)]]
check=[start]
print path_gp
for z1 in range (0,50):
    for z2 in range (x,y):
        if z2==(2+w*3):
            c=c+1
            w=w+1
        print z1,z2,c,check[c]
        path1=[]
        path2=[]
        path3=[]
        path4=[]
        for z3 in range(0,q):
            path1.append(path_gp[z2][z3])
            path2.append(path_gp[z2][z3])
            path3.append(path_gp[z2][z3])
            path4.append(path_gp[z2][z3])
        c1,c2 = check[z2]
        #print check[z2]
        cxa=c1+40
        cya=c2
        layer1 = (cxa,cya)
        cxb=c1
        cyb=c2-40
        layer2 = (cxb,cyb)
        cxc=c1-40
        cyc=c2
        layer3 = (cxc,cyc)
        cxd=c1
        cyd=c2+40
        layer4 = (cxd,cyd)
        t1=0
        t2=0
        t3=0
        t4=0
        for z3 in range(0,y):                                      #for checking the redundancy of any element previously occured in the path
            if check[z3]==(cxa,cya):
                t1=1
            elif check[z3]==(cxb,cyb):
                t2=1
            elif check[z3]==(cxc,cyc):
                t3=1
            elif check[z3]==(cxd,cyd):
                t4=1;
        if (cxa<400)&(cya<400):
            b1,g1,r1 = img[cya,cxa]
            #print b1
            if (t1!=1)&(cxa>0)&(cya>0)&(b1==255):
                path1.append(layer1)
                #print path1
                path_gp.append(path1)
                check.append(layer1)
        if (cxb<400)&(cyb<400):
            b2,g2,r2 = img[cyb,cxb]
            #print b2
            if (t2!=1)&(cxb>0)&(cyb>0)&(b2==255):
                path2.append(layer2)
                #print path2
                path_gp.append(path2)
                check.append(layer2)
        if (cxc<400)&(cyc<400):        
            b3,g3,r3= img[cyc,cxc]
            #print b3
            if (t3!=1)&(cxc>0)&(cyc>0)&(b3==255):
                path3.append(layer3)
                #print path3
                path_gp.append(path3)
                check.append(layer3)
        if (cxd<400)&(cyd<400):    
            b4,g4,r4 = img[cyd,cxd]
            #print b4
            if (t4!=1)&(cxd>0)&(cyd>0)&(b4==255):
                path4.append(layer4)
                #print path4
                path_gp.append(path4)
                check.append(layer4)
        #print " \n"        
        if (layer1 == end)|(layer2 == end)|(layer3 == end)|(layer4 == end):
            a=z2
            break
    if (layer1 == end)|(layer2 == end)|(layer3 == end)|(layer4 == end):
        break
    x=y
    y=len(check)
    #y=y*3+2
    q=q+1
if a==0:
    print "No Path"
elif a!=0:
    #print a
    print start
    print end
    #print path_gp
    #print check
    print path_gp[a]
    n = len(path_gp[a])
    for i in range(0,n):
        a1,b1=path_gp[a][i]
        cv2.circle(img,(a1,b1),2,(255,0,0),-1)
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
