'''
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2014)
*                  ================================
*Team id: eYRC+#925
*Author List: VED VASU SHARMA, ARUN SONI
*File Name: eYRC+#925 task5_original configuration code
*Theme: eYRC+ CARETAKER ROBOT Theme
*Functions: bot_position, bot_movement, get_shortestpath, get_perspective_image,
*           yellow_coordinates, blue_coordinates, red_coordinates
*Global Variables: NONE
*
**************************************************************************
'''


'''
*
*Function Name: bot_movement
*
*Input: path_gp->array of paths obtained from get_shortestpath function
*       a->this is the shortest path number obtained from get_shortestpath function
*       d->it is the direction parameter of bot
*Output: d->direction parameter of the bot
*Logic: This function is only called through get_shortestpath function
*      This function observes the direction of bot and compares the position of
*      next coordintes and present coordinates to move accordingly.
*      Commands are given wrt time i.e time for which a particular command is executed.
*Example Call: d = bot_movement(path_gp,a,d)
*
'''
def bot_movement(path_gp,a,d):
    ser = serial.Serial(3,timeout=1)                        #serial port is opened...for my pc it is COM3
    print ser     
    ser.baudrate = 9600
    n = len(path_gp[a])                                     #Baudrate is choosen 9600
    for i in range(0,n):
        a1,b1=path_gp[a][i]                                 #a1,b1->coordinates of start point
        a2,b2=path_gp[a][i+1]                               #a2,b2->coordinates of next point
        print a1,b1,a2,b2
        time.sleep(1)
        print d
        if(a1>a2):                                          #condition testing ->in which direction the bot is supposed to move
            if d==1:                                        #condition testing ->according to the current facing direction of the bot
                ser.write("4")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)                               #motion command is activated according to the time in next statement
                ser.write("5")
                d=4
            elif d==2:
                ser.write("6")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=4
            elif d==3:
                ser.write("4")
                time.sleep(1)
                ser.write("4")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=4
            elif d==4:
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=4
        elif (a1<a2):
            if d==1:
                ser.write("6")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=3
            elif d==2:
                ser.write("4")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=3
            elif d==3:
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=3
            elif d==4:
                ser.write("4")
                time.sleep(1)
                ser.write("4")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=3
        elif (b1<b2):
            if d==1:
                ser.write("6")
                time.sleep(1)
                ser.write("6")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=2
            elif d==2:
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=2
            elif d==3:
                ser.write("6")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=2
            elif d==4:
                ser.write("4")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=2
        elif (b1>b2):
            if d==1:
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=1
            elif d==2:
                ser.write("6")
                time.sleep(1)
                ser.write("6")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=1
            elif d==3:
                ser.write("4")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=1
            elif d==4:
                ser.write("6")
                time.sleep(1)
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=1
        ser.write("5")
    ser.close()
    return d

'''
*
*Function Name: get_shortestpath
*
*Input: cx1,cy1->starting point
*       cx2,cy2->ending point
*       d->direction parameter of the bot
*Output: d->direction parameter of the bot
*Logic: shortest path is obtained through dijkstra's algorithm...as in task2
*Example Call: d=get_shortestpath(cx1,cy1,cx2,cy2)
*
'''

def get_shortestpath(cx1,cy1,cx2,cy2,d):
    a=0                                                                 #a->parameter for path number in path_gp array
    y=1
    x=0
    c=0                                                                 #x,y,c,w,q-<these are counters used appropiately
    w=1
    q=1
    end =(cx2,cy2)                                                      #end point  
    start =(cx1,cy1)                                                    #start point
    path_gp=[[(cx1,cy1)]]                                               #array containing start as the first path    
    check=[start]             
    for z1 in range (0,50):                                             #loop controlling the number of steps
        for z2 in range (x,y):                                          #loop controling the next step in a path->valid or not
            if z2==(2+w*3):
                c=c+1
                w=w+1
            path1=[]                                                    #paths in all four directions
            path2=[]
            path3=[]
            path4=[]
            for z3 in range(0,q):
                path1.append(path_gp[z2][z3])
                path2.append(path_gp[z2][z3])
                path3.append(path_gp[z2][z3])
                path4.append(path_gp[z2][z3])
            c1,c2 = check[z2]
            cxa=c1+40                                                   #coordinates set in all the four directions
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
            for z3 in range(0,y):                                       #for checking the redundancy of any element previously occured in the path
                if check[z3]==(cxa,cya):
                    t1=1
                elif check[z3]==(cxb,cyb):
                    t2=1
                elif check[z3]==(cxc,cyc):
                    t3=1
                elif check[z3]==(cxd,cyd):
                    t4=1
            if (cxa<400)&(cya<400):                                     #conditions testing if next step is valid or not
                b1,g1,r1 = blur[cya,cxa]
                if (cxa+40)<400:
                    bx1,gx1,rx1 = blur[cya,cxa+10]
                    by1,gy1,ry1 = blur[cya,cxa-10]
                    ba11,ga11,ra11 = blur[cya+10,cxa+10]
                    bb11,gb11,rb11 = blur[cya+10,cxa-10]
                    bc11,gc11,rc11 = blur[cya-10,cxa+10]
                    bd11,gd11,rd11 = blur[cya-10,cxa-10]
                else :
                    bx1=255
                    by1=255
                    ba11=255
                    bb11=255
                    bc11=255
                    bd11=255
                if (t1!=1)&(cxa>0)&(cya>0)&(b1==255)&(bx1>100)&(by1>100)&(ba11>100)&(bb11>100)&(bc11>100)&(bd11>100):
                    path1.append(layer1)
                    path_gp.append(path1)
                    check.append(layer1)
            if (cxb<400)&(cyb<400):
                b2,g2,r2 = blur[cyb,cxb]
                if (cxb+40)<400:
                    bx2,gx2,rx2 = blur[cyb,cxb+10]
                    by2,gy2,ry2 = blur[cyb,cxb-10]
                    ba22,ga22,ra22 = blur[cyb+10,cxb+10]
                    bb22,gb22,rb22 = blur[cyb+10,cxb-10]
                    bc22,gc22,rc22 = blur[cyb-10,cxb+10]
                    bd22,gd22,rd22 = blur[cyb-10,cxb-10]
                else:
                    bx2=255
                    by2=255
                    ba22=255
                    bb22=255
                    bc22=255
                    bd22=255
                if (t2!=1)&(cxb>0)&(cyb>0)&(b2==255)&(bx2>100)&(by2>100)&(ba22>100)&(bb22>100)&(bc22>100)&(bd22>100):
                    path2.append(layer2)
                    path_gp.append(path2)
                    check.append(layer2)
            if (cxc<400)&(cyc<400):        
                b3,g3,r3= blur[cyc,cxc]
                if (cxc+40)<400:
                    bx3,gx3,rx3 = blur[cyc,cxc+10]
                    by3,gy3,ry3 = blur[cyc,cxc-10]
                    ba33,ga33,ra33 = blur[cyc+10,cxc+10]
                    bb33,gb33,rb33 = blur[cyc+10,cxc-10]
                    bc33,gc33,rc33 = blur[cyc-10,cxc+10]
                    bd33,gd33,rd33 = blur[cyc-10,cxc-10]
                else:
                    bx3=255
                    by3=255
                    ba33=255
                    bb33=255
                    bc33=255
                    bd33=255
                if (t3!=1)&(cxc>0)&(cyc>0)&(b3==255)&(bx3>100)&(by3>100)&(ba33>100)&(bb33>100)&(bc33>100)&(bd33>100):
                    path3.append(layer3)
                    path_gp.append(path3)
                    check.append(layer3)
            if (cxd<400)&(cyd<400):    
                b4,g4,r4 = blur[cyd,cxd]
                if (cxd+40)<400:
                    bx4,gx4,rx4 = blur[cyd,cxd+10]
                    by4,gy4,ry4 = blur[cyd,cxd-10]
                    ba44,ga44,ra44 = blur[cyd+10,cxd+10]
                    bb44,gb44,rb44 = blur[cyd+10,cxd-10]
                    bc44,gc44,rc44 = blur[cyd-10,cxd+10]
                    bd44,gd44,rd44 = blur[cyd-10,cxd-10]
                else:
                    bx4=255
                    by4=255
                    ba44=255
                    bb44=255
                    bc44=255
                    bd44=255
                if (t4!=1)&(cxd>0)&(cyd>0)&(b4==255)&(bx4>100)&(by4>100)&(ba44>100)&(bb44>100)&(bc44>100)&(bd44>100):
                    path4.append(layer4)
                    path_gp.append(path4)
                    check.append(layer4)
            print z1,z2
            if (layer1 == end)|(layer2 == end)|(layer3 == end)|(layer4 == end):          #checking if the loop reached the end point
                a=z2
                break
        if (layer1 == end)|(layer2 == end)|(layer3 == end)|(layer4 == end):
            break
        x=y
        y=len(check)
        q=q+1
    if a==0:
        print "No Path"                                                                  #if path_gp array not appended a=0 -> no path found
    elif a!=0:
        n = len(path_gp[a])
        for i in range(0,n):
            a1,b1=path_gp[a][i]
            cv2.circle(img,(a1,b1),2,(255,0,0),-1)
        #d=bot_movement(path_gp,a,d)                                              #this function is called to activate bot movement on that path
    return d


'''
*
*Function Name: get_perspective_image
*
*Input: frame->image captured from camera is passed to it and it gives cropped image
*Output: img ->cropped image
*Logic: image inside any rectangle is cropped into desired size-> here 400x400
*       it is same function used in task3 to crop the image
*Example Call: img = get_perspective_image(frame)   ->where frame is image captured
*
'''


def get_perspective_image(frame):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    lower = np.array([0, 0, 0])                                                             #black color mask
    upper = np.array([120, 120, 120])
    mask = cv2.inRange(frame, lower, upper)
    
    ret,thresh1 = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    biggest = 0
    max_area = 0
    min_size = thresh1.size/4
    index1 = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 10000:
            peri = cv2.arcLength(i,True)
        if area > max_area: 
            biggest = index1
            max_area = area
        index1 = index1 + 1
    approx = cv2.approxPolyDP(contours[biggest],0.05*peri,True)
                                                                                    #drawing the biggest polyline
    cv2.polylines(frame, [approx], True, (0,255,0), 3)
    x1 = approx[0][0][0]
    y1 = approx[0][0][1]
    x2 = approx[1][0][0]
    y2 = approx[1][0][1]
    x3 = approx[3][0][0]
    y3 = approx[3][0][1]
    x4 = approx[2][0][0]
    y4 = approx[2][0][1]

    print x1, y1
    print x2, y2
    print x3, y3
    print x4, y4
    
                                                                                    #points remapped from source image from camera
                                                                                    #to cropped image try to match x1, y1,.... to the respective near values
    pts1 = np.float32([[x2,y2],[x4,y4],[x1,y1],[x3,y3]]) 
    pts2 = np.float32([[0,0],[0,400],[400,0],[400,400]])
    persM = cv2.getPerspectiveTransform(pts1,pts2)
    img = cv2.warpPerspective(frame,persM,(400,400))                                # resolution set to 400x400.....we are processing image on this resolution
    return img



'''
*
*Function Name: bot_path_all_different
*Input: cx1,cy1->bot position coordinates
        d->direction of bot
*Output: decides path of the bot
*Logic: depends on which series of colors
*Example Call: bot_path_all_different(cx1,cy1)
*
'''
def bot_path_all_different(cx1,cy1,d):
    cx2=red_marker[0]                             #if it is red then robot carries two markers i.e. red and blue    
    cy2=red_marker[1]

    d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from bot start to red marker 

    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600
    ser.write("a")                                          #red led on
    ser.close()

    cx1=yellow_marker[0]
    cy1=yellow_marker[1]

    d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from red marker to yellow marker

    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600
    ser.write("c")                                          #yellow led on
    ser.close()

    cx2=red_bed[0]
    cy2=red_bed[1]

    d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow marker to red bed

    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600
    ser.write("b")                                          #red led off
    ser.close()

    cx1=yellow_bed[0]
    cy1=yellow_bed[1]

    d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  red bed to yellow bed

    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600
    ser.write("d")                                          #yellow led off
    ser.close()

    cx2=blue_marker[0]
    cy2=blue_marker[1]

    d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow bed to blue marker

    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600
    ser.write("e")                                          #blue led on
    ser.close()

    cx1=blue_bed[0]
    cy1=blue_bed[1]
##
##    d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from red marker to red bed
##
##    ser = serial.Serial(3,timeout=1)
##    ser.baudrate = 9600
##    ser.write("f")                                          #blue led off
##
##    ser.write("7")                                          #continuous beep sound
##    time.sleep(8)
##    ser.write("9")
##    ser.close()    




'''
*
*Function Name: bot_path_2coloursame
*
*Input: cx1,cy1->bot position coordinates
        b1,r1,y1->number of patients markers and position markes with respective colour
        d->direction of bot
*Output: decides path of the bot
*Logic: depends on which two colors are same
*Example Call: bot_path_2coloursame(cx1,cy1,b1,r1,y1)
*
'''



def bot_path_2coloursame(cx1,cy1,b1,r1,y1,d):
    if(b1==4):                                                #if there are two bule demands then check for another demand from patient
        if(r1==2):                                            #if it is red then robot carries two markers i.e. red and blue
            cx2=blue_marker[0]                                 #else it will carry two markers i.e. yellow and blue
            cy2=blue_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from bot start to blue marker 

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("e")                                          #blue led on
            ser.close()

            cx1=red_marker[0]
            cy1=red_marker[1]
            
            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from blue marker to red mark

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("a")                                          #red led on
            ser.close()

            cx2=blue_bed[0]
            cy2=blue_bed[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from red marker to blue bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("f")                                          #blue led off
            ser.close()

            cx1=red_bed[0]
            cy1=red_bed[1]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  blue bed to red bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("b")                                          #red led off
            ser.close()

            cx2=blue_marker[0]
            cy2=blue_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from red bed to blue marker

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("e")                                          #blue led on
            ser.close()

            cx1=blue_bed[2]
            cy1=blue_bed[3]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from blue marker to blue bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("f")                                          #blue led off

            ser.write("7")                                          #continuous beep sound
            time.sleep(8)
            ser.write("9")
            ser.close()

        elif (y1==2):
            cx2=blue_marker[0]                                 
            cy2=blue_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from bot start to blue marker 

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("e")                                          #blue led on
            ser.close()

            cx1=yellow_marker[0]
            cy1=yellow_marker[1]
            
            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from blue marker to yellow mark

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("c")                                          #yellow led on
            ser.close()

            cx2=blue_bed[0]
            cy2=blue_bed[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow marker to blue bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("f")                                          #blue led off
            ser.close()

            cx1=yellow_bed[0]
            cy1=yellow_bed[1]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  blue bed to yellow bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("d")                                          #yellow led off
            ser.close()

            cx2=blue_marker[0]
            cy2=blue_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow bed to blue marker

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("e")                                          #blue led on
            ser.close()

            cx1=blue_bed[2]
            cy1=blue_bed[3]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from blue marker to blue bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("f")                                          #blue led off

            ser.write("7")                                          #continuous beep sound
            time.sleep(8)
            ser.write("9")
            ser.close()

    if(y1==4):                                                
        if(r1==2):                                            
            cx2=yellow_marker[0]                                
            cy2=yellow_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from bot start to yellow marker 

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("c")                                          #yellow led on
            ser.close()

            cx1=red_marker[0]
            cy1=red_marker[1]
            
            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from yellow marker to red mark

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("a")                                          #red led on
            ser.close()

            cx2=yellow_bed[0]
            cy2=yellow_bed[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from red marker to yellow bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("d")                                          #yellow led off
            ser.close()

            cx1=red_bed[0]
            cy1=red_bed[1]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  yellow bed to red bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("b")                                          #red led off
            ser.close()

            cx2=yellow_marker[0]
            cy2=yellow_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from red bed to yellow marker

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("c")                                          #yellow led on
            ser.close()

            cx1=yellow_bed[2]
            cy1=yellow_bed[3]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from yellow marker to yellow bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("d")                                          #yellow led off

            ser.write("7")                                          #continuous beep sound
            time.sleep(8)
            ser.write("9")
            ser.close()

        elif (b1==2):
            cx2=yellow_marker[0]                                
            cy2=yellow_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from bot start to yellow marker 

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("c")                                          #yellow led on
            ser.close()

            cx1=blue_marker[0]
            cy1=blue_marker[1]
            
            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from yellow marker to blue mark

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("e")                                          #blue led on
            ser.close()

            cx2=yellow_bed[0]
            cy2=yellow_bed[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from blue marker to yellow bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("d")                                          #yellow led off
            ser.close()

            cx1=blue_bed[0]
            cy1=blue_bed[1]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  yellow bed to blue bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("f")                                          #blue led off
            ser.close()

            cx2=yellow_marker[0]
            cy2=yellow_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from blue bed to yellow marker

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("c")                                          #yellow led on
            ser.close()

            cx1=yellow_bed[2]
            cy1=yellow_bed[3]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from yellow marker to yellow bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("d")                                          #yellow led off

            ser.write("7")                                          #continuous beep sound
            time.sleep(8)
            ser.write("9")
            ser.close()
            


    if(r1==4):                                                #if there are two bule demands then check for another demand from patient
        if(b1==2):                                            #if it is red then robot carries two markers i.e. red and blue
            cx2=red_marker[0]                                 
            cy2=red_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from bot start to red marker 

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("a")                                          #red led on
            ser.close()

            cx1=blue_marker[0]
            cy1=blue_marker[1]
            
            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from red marker to blue mark

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("e")                                          #blue led on
            ser.close()

            cx2=red_bed[0]
            cy2=red_bed[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from blue marker to red bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("b")                                          #red led off
            ser.close()

            cx1=blue_bed[0]
            cy1=blue_bed[1]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  red bed to blue bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("f")                                          #blue led off
            ser.close()

            cx2=red_marker[0]
            cy2=red_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from blue bed to red marker

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("a")                                          #red led on
            ser.close()

            cx1=red_bed[2]
            cy1=red_bed[3]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from red marker to red bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("b")                                          #red led off

            ser.write("7")                                          #continuous beep sound
            time.sleep(8)
            ser.write("9")
            ser.close()

        elif (y1==2):
            cx2=red_marker[0]                                 
            cy2=red_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from bot start to red marker 

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("a")                                          #red led on
            ser.close()

            cx1=yellow_marker[0]
            cy1=yellow_marker[1]
            
            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from blue marker to yellow mark

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("c")                                          #yellow led on
            ser.close()

            cx2=red_bed[0]
            cy2=red_bed[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow marker to red bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("b")                                          #red led off
            ser.close()

            cx1=yellow_bed[0]
            cy1=yellow_bed[1]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  red bed to yellow bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("d")                                          #yellow led off
            ser.close()

            cx2=red_marker[0]
            cy2=red_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow bed to red marker

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("a")                                          #red led on
            ser.close()

            cx1=red_bed[2]
            cy1=red_bed[3]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from red marker to red bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("b")                                          #red led off

            ser.write("7")                                          #continuous beep sound
            time.sleep(8)
            ser.write("9")
            ser.close()




'''
*
*Function Name: bot_path_3coloursame
*
*Input: cx1,cy1->bot position coordinates
        b1,r1,y1->number of patients markers and position markes with respective colour
        d->direction of bot
*Output: decides path of the bot
*Logic: depends on which three colors are same
*Example Call: bot_path_3coloursame(cx1,cy1,b1,r1,y1)
*
'''



def bot_path_3coloursame(cx1,cy1,b1,r1,y1,d):
    if(r1==6):                                                #if there are two bule demands then check for another demand from patient     
        cx2=red_marker[0]                             #if it is red then robot carries two markers i.e. red and blue    
        cy2=red_marker[1]

        d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from bot start to red marker 

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("a")                                          #red led on
        ser.close()

        cx1=red_bed[0]
        cy1=red_bed[1]
        
        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from red marker to red bed

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("b")                                          #red led off
        ser.close()

        cx2=red_marker[0]
        cy2=red_marker[1]

        d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from red bed to red marker

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("a")                                          #red led on
        ser.close()

        cx1=red_bed[2]
        cy1=red_bed[3]

        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  red marker to red bed

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("b")                                          #red led off
        ser.close()

        cx2=red_marker[0]
        cy2=red_marker[1]

        d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from red bed to red marker

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("a")                                          #red led on
        ser.close()

        cx1=red_bed[4]
        cy1=red_bed[5]

        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from red marker to red bed

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("b")                                          #red led off

        ser.write("7")                                          #continuous beep sound
        time.sleep(8)
        ser.write("9")
        ser.close()    

    elif(b1==6):
        cx2=blue_marker[0]                             #if it is red then robot carries two markers i.e. red and blue    
        cy2=blue_marker[1]

        d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from bot start to blue marker 

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("e")                                          #blue led on
        ser.close()

        cx1=blue_bed[0]
        cy1=blue_bed[1]
        
        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from blue marker to blue bed

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("f")                                          #blue led off
        ser.close()

        cx2=blue_marker[0]
        cy2=blue_marker[1]

        d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from blue bed to blue marker

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("e")                                          #blue led on
        ser.close()

        cx1=blue_bed[2]
        cy1=blue_bed[3]

        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  blue marker to blue bed

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("f")                                          #blue led off
        ser.close()

        cx2=blue_marker[0]
        cy2=blue_marker[1]

        d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from blue bed to blue marker

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("e")                                          #blue led on
        ser.close()

        cx1=blue_bed[4]
        cy1=blue_bed[5]

        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from blue marker to blue bed

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("f")                                          #blue led off

        ser.write("7")                                          #continuous beep sound
        time.sleep(8)
        ser.write("9")
        ser.close()

    elif(y1==6):
        cx2=yellow_marker[0]                             
        cy2=yellow_marker[1]

        d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from bot start to yellow marker 

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("c")                                          #yellow led on
        ser.close()

        cx1=yellow_bed[0]
        cy1=yellow_bed[1]
        
        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from yellow marker to yellow bed

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("d")                                          #yellow led off
        ser.close()

        cx2=yellow_marker[0]
        cy2=yellow_marker[1]

        d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow bed to yellow marker

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("c")                                          #yellow led on
        ser.close()

        cx1=yellow_bed[2]
        cy1=yellow_bed[3]

        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  yellow marker to yellow bed

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("d")                                          #yellow led off
        ser.close()

        cx2=yellow_marker[0]
        cy2=yellow_marker[1]

        d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow bed to yellow marker

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("c")                                          #yellow led on
        ser.close()

        cx1=yellow_bed[4]
        cy1=yellow_bed[5]

        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from yellow marker to yellow bed

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("d")                                          #yellow led off

        ser.write("7")                                          #continuous beep sound
        time.sleep(8)
        ser.write("9")
        ser.close()
        









'''
*
*Function Name: bot_position
*
*Input: img->image captured from camera is passed to it and it gives bot coordinates
*Output: d->direction parameter of the bot
*Logic: image is converted to grayscale and then threshed, now it is blured to get
*       contour of the bot, whose centroid is the bot position
*Example Call: c1,c2 = bot_position(img)   ->where img is image captured
*
'''
def bot_position(img):
    gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh2 = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
    ret,thresh6 = cv2.threshold(thresh2,150,255,cv2.THRESH_BINARY_INV)
    ret,thresh1 = cv2.threshold(thresh6,210,255,cv2.THRESH_BINARY)
    blur3 = cv2.medianBlur(thresh1,99)
    ret,thresh = cv2.threshold(blur3,210,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    M1 = cv2.moments(contours[0])
    cx = int(M1['m10']/M1['m00'])
    cy = int(M1['m01']/M1['m00'])
    print cx,cy

    if(cy<150):
        cbotx=280
        cboty=80
    elif(cy>350):
        cbotx=280
        cboty=240
    elif(cy>150)&(cy<150):
        cbotx=280
        cboty=80
    cv2.circle(img,(cbotx,cboty), 5, (0,255,0), -1)
    return cbotx,cboty

'''
*
*Function Name: yellow_coordinates
*
*Input: img->image captured from camera is passed to it and it gives yellow colour coordinates
*Output: d->direction parameter of the bot
*Logic: image is masked as per the parameters of the colour and then threshed, now it is blured to get
*       exact contours, whose centroid is the position of the color
*       works for two points as per the original configuration
*Example Call: cyx1,cyy1,cyx2,cyy2 = yellow_coordinates(img)   ->where img is image captured
*
'''



def yellow_coordinates(img):
    param1 = [50,150,100]                                 #parameters for yellow colour range
    param2 = [150,255,255]
    lower = np.array(param1)
    upper = np.array(param2)
    mask  = cv2.inRange(img,lower, upper)
    res1   = cv2.bitwise_and(img, img, mask= mask)
    gray = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
    blur3 = cv2.medianBlur(thresh1,15)
    contours, hierarchy = cv2.findContours(blur3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    l=len(contours)
    yellow_marker=[]
    yellow_bed=[]
    for i in range(0,l):
        M1 = cv2.moments(contours[i])                            
        cyx = int(M1['m10']/M1['m00'])
        cyy = int(M1['m01']/M1['m00'])
        if(cyx<200):
            m=cyx%40;                                                             
            cyx=cyx-m+40;                                            
            m=cyy%40;
            cyy=cyy-m;
            yellow_marker.append(cyx)
            yellow_marker.append(cyy) 
        else:
            m=cyx%40;                                                             
            cyx=cyx-m;                                            
            m=cyy%40;
            cyy=cyy+(40-m);
            yellow_bed.append(cyx)
            yellow_bed.append(cyy)
    return yellow_marker,yellow_bed                        #two points returned as per the original configuration
    



'''
*
*Function Name: blue_coodinates
*
*Input: img->image captured from camera is passed to it and it gives blue colour coordinates
*Output: d->direction parameter of the bot
*Logic: image is masked as per the parameters of the colour and then threshed, now it is blured to get
*       exact contours, whose centroid is the position of the color
        works for two points as per the original configuration
*Example Call: cbx1,cby1,cbx2,cby2 = blue_coordinates(img)   ->where img is image captured
*
'''

def blue_coordinates(img):
    param1 = [100,0,0]                                                      #parameters for blue colour range
    param2 = [255,100,100]
    lower = np.array(param1)
    upper = np.array(param2)
    mask  = cv2.inRange(img,lower, upper)
    res1   = cv2.bitwise_and(img, img, mask= mask)
    gray = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
    blur3 = cv2.medianBlur(thresh1,15)
    contours, hierarchy = cv2.findContours(blur3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    l=len(contours)
    blue_marker=[]
    blue_bed=[]
    for i in range(0,l):
        M1 = cv2.moments(contours[i])                            
        cbx = int(M1['m10']/M1['m00'])
        cby = int(M1['m01']/M1['m00'])
        if(cbx<200):
            m=cbx%40;                                                             
            cbx=cbx-m+40;                                            
            m=cby%40;
            cby=cby-m;
            blue_marker.append(cbx)
            blue_marker.append(cby)
        else:
            m=cbx%40;                                                             
            cbx=cbx-m;                                            
            m=cby%40;
            cby=cby+(80-m);
            blue_bed.append(cbx)
            blue_bed.append(cby)
    return blue_marker,blue_bed                        #two points returned as per the original configuration


'''
*
*Function Name: red_coodinates
*
*Input: img->image captured from camera is passed to it and it gives red colour coordinates
*Output: d->direction parameter of the bot
*Logic: image is masked as per the parameters of the colour and then threshed, now it is blured to get
*       exact contours, whose centroid is the position of the color
        works for two points as per the original configuration
*Example Call: crx1,cry1,crx2,cry2 = red_coordinates(img)   ->where img is image captured
*
'''

def red_coordinates(img):
    param1 = [0,0,225]                                                         #parameters for red colour range
    param2 = [200,200,255]
    lower = np.array(param1)
    upper = np.array(param2)
    mask  = cv2.inRange(img,lower, upper)
    res1   = cv2.bitwise_and(img, img, mask= mask)
    gray = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
    blur3 = cv2.medianBlur(thresh1,15)
    contours, hierarchy = cv2.findContours(blur3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    l=len(contours)
    red_marker=[]
    red_bed=[]
    for i in range(0,l):
        M1 = cv2.moments(contours[i])                            
        crx = int(M1['m10']/M1['m00'])
        cry = int(M1['m01']/M1['m00'])
        if(crx<200):
            m=crx%40;                                                             
            crx=crx-m+40;                                            
            m=cry%40;
            cry=cry-m;
            red_marker.append(crx)
            red_marker.append(cry)
        else:
            m=crx%40;                                                             
            crx=crx-m;                                            
            m=cry%40;
            cry=cry+(40-m);
            red_bed.append(crx)
            red_bed.append(cry)
    return red_marker,red_bed                        #two points returned as per the original configuration



'''
*
* Name: Main Program
* Input: None
* Output: None
* Logic: Captures the image from camera, invokes the appropiate functions to get the task done
* Example Call: Called automatically by the Operating System
*
*
'''

######### MAIN PROGRAM STARTING ##############

##############################################
## Import OpenCV
import numpy as np
import cv2
import serial
import time                                                          # impot time for working with time.sleep() statement
#############################################


#cap = cv2.VideoCapture(1)
#ret, frame = cap.read()                                              #image captured with the help of overhead camera
frame = cv2.imread('sample1.jpg')
img = get_perspective_image(frame)                                   #inside of rectangle is cropped

#####now img is cropped image in 400x400 resolution                                                                     
#####Co-ordinates of all the required points are obtained

#cbotx,cboty = bot_position(img)
cbotx=200
cboty=200
yellow_marker,yellow_bed = yellow_coordinates(img)                      #coordinates of yellow colour
blue_marker,blue_bed = blue_coordinates(img)                            #coordinates of blue colour
red_marker,red_bed = red_coordinates(img)                               #coordinates of red colour

cv2.circle(img,(cbotx,cboty), 5, (0,0,0), -1)
cv2.circle(img,(yellow_marker[0],yellow_marker[1]), 5, (0,0,255), -1)
cv2.circle(img,(yellow_bed[0],yellow_bed[1]), 5, (0,0,255), -1)
cv2.circle(img,(blue_marker[0],blue_marker[1]), 5, (0,255,0), -1)
cv2.circle(img,(blue_bed[0],blue_bed[1]), 5, (0,255,0), -1)
cv2.circle(img,(red_marker[0],red_marker[1]), 5, (255,0,0), -1)
cv2.circle(img,(red_bed[0],red_bed[1]), 5, (255,0,0), -1)

print cbotx,cboty
print yellow_marker
print yellow_bed
print blue_marker
print blue_bed
print red_marker
print red_bed


#####image is processed for the proper functioning of the get_shortestpath function -> this function works on blur image in next step
ret,thresh2 = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)
ret,blur = cv2.threshold(thresh2,150,255,cv2.THRESH_BINARY_INV)    #this image is used for making white color completely white

################################################


d=1      #direction parameter of the robot initially set to 1:     1->North      2->South    3->East   4->West


####functions are called with appropiate start and end points......as per the original configuration



'''
we have added following parameters in the zigbee_serial communication code.hex for the working of the led
* redled_on->    ASCII value -> 'a'
* redled_off->   ASCII value -> 'b'
* greenled_on->  ASCII value -> 'c'
* greenled_off-> ASCII value -> 'd'
* blueled_on->   ASCII value -> 'e'
* blueled_off->  ASCII value -> 'f'
'''

cx1=cbotx
cy1=cboty
b1=len(blue_bed)
r1=len(red_bed)
y1=len(yellow_bed)

if(b1==4)|(r1==4)|(y1==4):
    bot_path_2coloursame(cx1,cy1,b1,r1,y1,d)
elif(b1==6)|(r1==6)|(y1==6):
    bot_path_3coloursame(cx1,cy1,b1,r1,y1,d)
elif(b1==2)&(r1==2)&(y1==2):
    bot_path_all_different(cx1,cy1,d)


##################################################
## Show the image
#cv2.imshow('image1',res1)
cv2.imshow('blur',blur)
cv2.imshow('image',img)

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
