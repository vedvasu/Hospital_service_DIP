############################################
## Import OpenCV
import numpy as np
import cv2
import serial
import time
############################################
def bot_position(img):
    gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh2 = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
    ret,thresh6 = cv2.threshold(thresh2,150,255,cv2.THRESH_BINARY_INV)
    ret,thresh1 = cv2.threshold(thresh6,210,255,cv2.THRESH_BINARY)
    blur3 = cv2.medianBlur(thresh1,99)
    ret,thresh = cv2.threshold(blur3,210,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print len(contours)
    #cv2.drawContours(img,contours ,-1,(0,255,0),3)
    M1 = cv2.moments(contours[0])
    cbotx = int(M1['m10']/M1['m00'])
    cboty = int(M1['m01']/M1['m00'])
    print cbotx,cboty
    cv2.circle(img,(cbotx,cboty), 5, (0,255,0), -1)
    return cbotx,cboty
def bot_movement(path_gp,a,d):
    ser = serial.Serial(3,timeout=1)
    print ser
    ser.baudrate = 9600
    n = len(path_gp[a])
    a1,b1=path_gp[a][0]
    final=a1,b1
    for i in range(1,n-1):
        
        if(a1>a2):
            if d==1:
                ser.write("4")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                d=4
            elif d==2:
                ser.write("6")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                d=4
            elif d==3:
                ser.write("4")
                time.sleep(2)
                ser.write("8")
                time.sleep(1)
                d=4
            elif d==4:
                ser.write("4")
                time.sleep(2)
                ser.write("8")
                time.sleep(1)
                d=4
        elif (a1<a2):
            if d==1:
                ser.write("6")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                d=3
            elif d==2:
                ser.write("4")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                d=3
            elif d==3:
                ser.write("8")
                time.sleep(1)
                d=3
            elif d==4:
                ser.write("4")
                time.sleep(2)
                ser.write("8")
                time.sleep(1)
                d=3
        elif (b1<b2):
            if d==1:
                ser.write("4")
                time.sleep(2)
                ser.write("8")
                time.sleep(1)
                d=2
            elif d==2:
                ser.write("8")
                time.sleep(1)
                d=2
            elif d==3:
                ser.write("6")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                d=2
            elif d==4:
                ser.write("4")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                d=2
        elif (b1>b2):
            if d==1:
                ser.write("8")
                time.sleep(1)
                d=1
            elif d==2:
                ser.write("4")
                time.sleep(2)
                ser.write("8")
                time.sleep(1)
                d=1
            elif d==3:
                ser.write("4")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                d=1
            elif d==4:
                ser.write("6")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                d=1
        ser.write("5")
    ser.close()
    return d
def get_shortestpath(cx1,cy1,cx2,cy2,d):
    a=0
    y=1
    x=0
    c=0
    w=1
    q=1
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
                    t4=1
            #print t1,t2,t3,t4        
            if (cxa<400)&(cya<400):
                b1,g1,r1 = blur[cya,cxa]
                if (cxa+40)<400:
                    bx1,gx1,rx1 = blur[cya,cxa+10]
                    by1,gy1,ry1 = blur[cya,cxa-10]
                else :
                    bx1=255
                    by1=255
                #print b1,bx1
                if (t1!=1)&(cxa>0)&(cya>0)&(b1==255)&(bx1>200)&(by1>200):
                    path1.append(layer1)
                    #print path1
                    path_gp.append(path1)
                    check.append(layer1)
            if (cxb<400)&(cyb<400):
                b2,g2,r2 = blur[cyb,cxb]
                if (cxb+40)<400:
                    bx2,gx2,rx2 = blur[cyb,cxb+10]
                    by2,gy2,ry2 = blur[cyb,cxb-10]
                else:
                    bx2=255
                    by2=255
                #print b2,bx2
                if (t2!=1)&(cxb>0)&(cyb>0)&(b2==255)&(bx2>200)&(by2>200):
                    path2.append(layer2)
                    #print path2
                    path_gp.append(path2)
                    check.append(layer2)
            if (cxc<400)&(cyc<400):        
                b3,g3,r3= blur[cyc,cxc]
                if (cxc+40)<400:
                    bx3,gx3,rx3 = blur[cyc,cxc+10]
                    by3,gy3,ry3 = blur[cyc,cxc-10]
                else:
                    bx3=255
                    by3=255
                #print b3,bx3
                if (t3!=1)&(cxc>0)&(cyc>0)&(b3==255)&(bx3>200)&(by3>200):
                    path3.append(layer3)
                    #print path3
                    path_gp.append(path3)
                    check.append(layer3)
            if (cxd<400)&(cyd<400):    
                b4,g4,r4 = blur[cyd,cxd]
                if (cxd+40)<400:
                    bx4,gx4,rx4 = blur[cyd,cxd+10]
                    by4,gy4,ry4 = blur[cyd,cxd-10]
                else:
                    bx4=255
                    by4=255
                #print b4,bx4
                if (t4!=1)&(cxd>0)&(cyd>0)&(b4==255)&(bx4>200)&(by4>200):
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
    cv2.circle(img,(cx1,cy1), 5, (150,255,0), -1)
    cv2.circle(img,(cx2,cy2), 5, (0,255,150), -1)
    #d=bot_movement(path_gp,a,d)
    return d
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
############################################
#position of bot
cv2.circle(img,(200,40), 5, (0,0,255), -1)
############################################
#Shortest path
cbotx=200
cboty=80
ret,thresh2 = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)
ret,blur = cv2.threshold(thresh2,150,255,cv2.THRESH_BINARY_INV)
#blur = cv2.medianBlur(thresh,5)

m=cyx1%40;
cyx1=cyx1-m;
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
cbx2=cbx2-m;
m=cby2%40;
cby2=cby2+(40-m);
m=crx1%40;
crx1=crx1+(40-m);
m=cry1%40;
cry1=cry1-m;
m=crx2%40;
crx2=crx2-m;
m=cry2%40;
cry2=cry2+(40-m);
d=1
cx1=cyx2
cy1=cyy2
cx2=cbx2
cy2=cby2
d=get_shortestpath(cyx1,cyy1,cbx1,cby1,d)
#d=get_shortestpath(cx1,cy1,cx2,cy2,d)
cx1=cyx2
cy1=cyy2
#d=get_shortestpath(cx2,cy2,cx1,cy1,d)
cx2=cyx1
cy2=cyy1
#d=get_shortestpath(cx1,cy1,cx2,cy2,d)
cx1=crx1
cy1=cry1
#d=get_shortestpath(cx2,cy2,cx1,cy1,d)
cx2=crx2
cy2=cry2
#d=get_shortestpath(cx1,cy1,cx2,cy2,d)
############################################
## Show the image
#cv2.imshow('blur',blur)
#cv2.imshow('image2',thresh)
cv2.imshow('image',img)
############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
