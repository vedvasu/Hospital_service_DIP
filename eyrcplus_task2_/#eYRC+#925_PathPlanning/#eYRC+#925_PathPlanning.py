import numpy as np
import cv2
#Teams can add other helper functions
#which can be added here
#Function for getting the centroid of the start point(blue color)
###################################################################################################
def start_point(img):
    param1 = [80,100,150]
    param2 = [130,200,255]                                                       #range for blue color
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
    return cx1,cy1
#####################################################################################################
#Function for getting the centroid of end point(green color)
def end_point(img):
    param1 = [50,100,100]
    param2 = [80,255,255]                                                       #range for green color
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
    return cx2,cy2
#####################################################################################################
#Function for finding the shortest path
def play(img):
    '''
    img-- a single test image as input argument
    route_length  -- returns the single integer specifying the route length
    '''
    cx1,cy1=start_point(img)
    cx2,cy2=end_point(img)
    a=0
    y=1
    x=0
    c=0
    w=1
    q=1
    end =(cx2,cy2)
    start =(cx1,cy1)
    path_gp=[[(cx1,cy1)]]                                           #matrix containing all the possible path
    check=[start]                                                   #check list for points already occured
    for z1 in range (0,20):                                         #loop for the number path_length
        for z2 in range (x,y):                                      #loop for the possible paths
            path1=[]                                                #path list for creating new paths
            path2=[]
            path3=[]
            path4=[]
            for z3 in range(0,q):
                path1.append(path_gp[z2][z3])
                path2.append(path_gp[z2][z3])
                path3.append(path_gp[z2][z3])
                path4.append(path_gp[z2][z3])
            c1,c2 = check[z2]                                       #possible 4 points in the horizontal and vertical direction
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
            for z3 in range(0,y):                                   #for checking the redundancy of any element previously occured in that path or other paths
                if check[z3]==(cxa,cya):
                    t1=1
                elif check[z3]==(cxb,cyb):
                    t2=1
                elif check[z3]==(cxc,cyc):
                    t3=1
                elif check[z3]==(cxd,cyd):
                    t4=1;
            if (cxa<400)&(cya<400):                                 #for checking that the points should not be out of the plane
                b1,g1,r1 = img[cya,cxa]                             #for checking the obsticle by identifying the red color
                if (t1!=1)&(cxa>0)&(cya>0)&(b1==255):               #conditions for accurate next path element
                    path1.append(layer1)
                    path_gp.append(path1)
                    check.append(layer1)
            if (cxb<400)&(cyb<400):
                b2,g2,r2 = img[cyb,cxb]
                if (t2!=1)&(cxb>0)&(cyb>0)&(b2==255):
                    path2.append(layer2)
                    path_gp.append(path2)
                    check.append(layer2)
            if (cxc<400)&(cyc<400):        
                b3,g3,r3= img[cyc,cxc]
                if (t3!=1)&(cxc>0)&(cyc>0)&(b3==255):
                    path3.append(layer3)
                    path_gp.append(path3)
                    check.append(layer3)
            if (cxd<400)&(cyd<400):    
                b4,g4,r4 = img[cyd,cxd]
                if (t4!=1)&(cxd>0)&(cyd>0)&(b4==255):
                    path4.append(layer4)
                    path_gp.append(path4)
                    check.append(layer4)
            if (layer1 == end)|(layer2 == end)|(layer3 == end)|(layer4 == end):             #checking for the end point
                a=z2
                break
        if (layer1 == end)|(layer2 == end)|(layer3 == end)|(layer4 == end):
            break
        x=y
        y=len(check)
        q=q+1
    if a==0:
        print "NO PATH!!!"                                          #if end point is never reached then function returns 0 and prints "no path"
        route_length = 0
        route_path =[0]
    elif a!=0:
        route_length = len(path_gp[a])
        route_path=[]
        for i in range(1,route_length):                                                         #loop for changing pixel values into single digit value 
            a1,b1=path_gp[a][i]
            a2=(a1+20)/40
            b2=(b1+20)/40
            point=(a2,b2)
            route_path.append(point)
        x=(end[0]+20)/40
        y=(end[1]+20)/40
        end_dot = (x,y)
        route_path.append(end_dot)
    return route_length, route_path

################################################################################################
if __name__ == "__main__":
    #code for checking output for single image
    img = cv2.imread('test_images/test_image1.png')
    route_length, route_path = play(img)
    print "route length = ", route_length
    print "route path   = ", route_path
    #code for checking output for all images
    route_length_list = []
    route_path_list   = []
    for file_number in range(1,6):
        file_name = "test_images/test_image"+str(file_number)+".png"
        pic = cv2.imread(file_name)
        route_length, route_path = play(pic)
        route_length_list.append(route_length)
        route_path_list.append(route_path)
    print route_length_list
    print route_path_list
