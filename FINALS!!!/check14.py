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

def inside():
    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600
    ser.write("8")
    time.sleep(1)
    ser.write("8")
    time.sleep(1)
    ser.write("5")
    time.sleep(2)
    ser.write("2")
    time.sleep(1)
    ser.write("2")
    time.sleep(1)
    ser.write("5")
    time.sleep(1.5)
    ser.close()



    
def bot_movement(path_gp,a,d):
    ser = serial.Serial(3,timeout=1)                        #serial port is opened...for my pc it is COM3
    print ser     
    ser.baudrate = 9600
    n = len(path_gp[a])                                     #Baudrate is choosen 9600
    print path_gp[a]
    ax,bx=path_gp[a][n-1]
    c=0
    m=0
    for i in range(0,n):
##        if(c==5):
##            ser.write("8")
##            time.sleep(1)
##            ser.write("5")
##        if (m==5):
##            ser.write("8")
##            time.sleep(1)
##            ser.write("5")
##        if(d==2)|(d==1):
##            c=c+1
##            m=0
##        elif (d==3)|(d==4):
##            c=0
##            m=m+1
        a1,b1=path_gp[a][i]                                   #a1,b1->coordinates of start point
        #a2,b2=path_gp[a][i+1]
        if(i<n-1):
            a2,b2=path_gp[a][i+1]                               #a2,b2->coordinates of next point
        elif(i==n-1):
            if(a1>200):
                a2=a1+40
            else:
                a2=a1-40
        print a1,b1,a2,b2
        time.sleep(1)
        print d
        if(a1>a2):                                          #condition testing ->in which direction the bot is supposed to move
            if d==1:                                        #condition testing ->according to the current facing direction of the bot
                ser.write("4")
                time.sleep(1.3)
                if(ax!=a2):
                    ser.write("8")
                    time.sleep(1)
                if(a1==ax)&(b1==bx)&(ax<320):
                    time.sleep(0.5)
                    ser.write("2")
                    time.sleep(1)                               #motion command is activated according to the time in next statement
                ser.write("5")
                d=4
            elif d==2:
                ser.write("6")
                time.sleep(1.3)
                if(ax!=a2):
                    ser.write("8")
                    time.sleep(1)
                if(a1==ax)&(b1==bx)&(ax<320):
                    time.sleep(0.5)
                    ser.write("2")
                    time.sleep(1)
                ser.write("5")
                d=4
            elif d==3:
                ser.write("i")
                time.sleep(1.5)
                if(ax!=a2):
                    ser.write("8")
                    time.sleep(1)
                if(a1==ax)&(b1==bx)&(ax<320):
                    time.sleep(0.5)
                    ser.write("2")
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
                time.sleep(1.3)
                ser.write("8")
                time.sleep(1)
                if(a1==ax)&(b1==bx)&(ax<320):
                    time.sleep(0.5)
                    ser.write("2")
                    time.sleep(1)
                ser.write("5")
                d=3
            elif d==2:
                ser.write("4")
                time.sleep(1.3)
                ser.write("8")
                time.sleep(1)
                if(a1==ax)&(b1==bx)&(ax<320):
                    time.sleep(0.5)
                    ser.write("2")
                    time.sleep(1)
                ser.write("5")
                d=3
            elif d==3:
                ser.write("8")
                time.sleep(1)
                ser.write("5")
                d=3
            elif d==4:
                ser.write("i")
                time.sleep(1.5)
                ser.write("8")
                time.sleep(1)
                if(a1==ax)&(b1==bx)&(ax<320):
                    time.sleep(0.5)
                    ser.write("2")
                    time.sleep(1)
                ser.write("5")
                d=3
        elif (b1<b2):
            if d==1:
                ser.write("i")
                time.sleep(1.5)
                ser.write("8")
                time.sleep(1)
                if(a1==ax)&(b1==bx)&(ax<320):
                    time.sleep(0.5)
                    ser.write("2")
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
                time.sleep(1.3)
                ser.write("8")
                time.sleep(1)
                if(a1==ax)&(b1==bx)&(ax<320):
                    time.sleep(0.5)
                    ser.write("2")
                    time.sleep(1)
                ser.write("5")
                d=2
            elif d==4:
                ser.write("4")
                time.sleep(1.3)
                ser.write("8")
                time.sleep(1)
                if(a1==ax)&(b1==bx)&(ax<320):
                    time.sleep(0.5)
                    ser.write("2")
                    time.sleep(1)
                ser.write("5")
                d=2
        elif (b1>b2):
            if d==1:
                ser.write("8")
                time.sleep(1.2)
                ser.write("5")
                d=1
            elif d==2:
                ser.write("i")
                time.sleep(1.5)
                ser.write("8")
                time.sleep(1)
                if(a1==ax)&(b1==bx)&(ax<320):
                    time.sleep(0.5)
                    ser.write("2")
                    time.sleep(1)
                ser.write("5")
                d=1
            elif d==3:
                ser.write("4")
                time.sleep(1.3)
                ser.write("8")
                time.sleep(1)
                if(a1==ax)&(b1==bx)&(ax<320):
                    time.sleep(0.5)
                    ser.write("2")
                    time.sleep(1)
                ser.write("5")
                d=1
            elif d==4:
                ser.write("6")
                time.sleep(1.3)
                ser.write("8")
                time.sleep(1)
                if(a1==ax)&(b1==bx)&(ax<320):
                    time.sleep(0.5)
                    ser.write("2")
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
            if (cxa<640)&(cya<480):                                     #conditions testing if next step is valid or not
                b1,g1,r1 = blur[cya,cxa]
                if (cxa+40)<640:
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
            if (cxb<640)&(cyb<480):
                b2,g2,r2 = blur[cyb,cxb]
                if (cxb+40)<640:
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
            if (cxc<640)&(cyc<480):        
                b3,g3,r3= blur[cyc,cxc]
                if (cxc+40)<640:
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
            if (cxd<640)&(cyd<480):    
                b4,g4,r4 = blur[cyd,cxd]
                if (cxd+40)<640:
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
    path_gp[a].append(end)
    if a==0:
        print "No Path"                                                                  #if path_gp array not appended a=0 -> no path found
    elif a!=0:
        print path_gp[a]
        n = len(path_gp[a])
        for i in range(0,n):
            a1,b1=path_gp[a][i]
            cv2.circle(img,(a1,b1),2,(255,0,0),-1)
        d=bot_movement(path_gp,a,d)                                              #this function is called to activate bot movement on that path
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
    lower = np.array([0, 0, 0]) #black color mask
    upper = np.array([120, 120, 120])
    mask = cv2.inRange(frame, lower, upper)
    
    ret,thresh1 = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame,contours,-1,(0,255,0),3)
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
    pts2 = np.float32([[0,0],[0,480],[640,0],[640,480]])
    persM = cv2.getPerspectiveTransform(pts1,pts2)
    img = cv2.warpPerspective(frame,persM,(640,480))                          # resolution set to 400x400.....we are processing image on this resolution
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
    time.sleep(1)
    ser.write("a")                                          #red led on
    time.sleep(1)
    ser.close()

    cx1=yellow_marker[0]
    cy1=yellow_marker[1]

    d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from red marker to yellow marker

    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600
    time.sleep(1)
    ser.write("t")                                           #yellow led on
    time.sleep(1)
    ser.close()

    cx2=red_bed[0]
    cy2=red_bed[1]

    d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow marker to red bed

    inside()
    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600
    ser.write("b")                                             #red led off
    time.sleep(1)
    ser.close()

    cx1=yellow_bed[0]
    cy1=yellow_bed[1]

    d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  red bed to yellow bed

    inside()
    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600
    ser.write("u")                                          #yellow led off
    time.sleep(1)
    ser.close()

    cx2=blue_marker[0]
    cy2=blue_marker[1]

    d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow bed to blue marker

    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600
    time.sleep(1)
    ser.write("c")                                          #blue led on
    time.sleep(1)
    ser.close()

    cx1=blue_bed[0]
    cy1=blue_bed[1]

    d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from red marker to red bed

    inside()
    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600
    ser.write("d")                                      #blue led off
    time.sleep(1)
    ser.close()

    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600 
    ser.write("7")                                          #continuous beep sound
    time.sleep(8)
    ser.write("9")
    ser.close()    




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
            ser.write("c")                                          #blue led on
            ser.close()

            cx1=red_marker[0]
            cy1=red_marker[1]
            
            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from blue marker to red mark

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("p")                                          #red led on
            ser.close()

            cx2=blue_bed[0]
            cy2=blue_bed[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from red marker to blue bed

            inside()
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("d")                                          #blue led off
            ser.close()

            cx1=red_bed[0]
            cy1=red_bed[1]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  blue bed to red bed

            inside()
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("q")                                          #red led off
            ser.close()

            cx2=blue_marker[0]
            cy2=blue_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from red bed to blue marker

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("c")                                          #blue led on
            ser.close()

            cx1=blue_bed[2]
            cy1=blue_bed[3]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from blue marker to blue bed

            inside()
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("d")                                          #blue led off

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
            ser.write("c")                                          #blue led on
            ser.close()

            cx1=yellow_marker[0]
            cy1=yellow_marker[1]
            
            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from blue marker to yellow mark

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("t")                                          #yellow led on
            ser.close()

            cx2=blue_bed[0]
            cy2=blue_bed[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow marker to blue bed
            inside()
            
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("d")                                          #blue led off
            ser.close()

            cx1=yellow_bed[0]
            cy1=yellow_bed[1]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  blue bed to yellow bed
            inside()
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("u")                                          #yellow led off
            ser.close()

            cx2=blue_marker[0]
            cy2=blue_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow bed to blue marker

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("c")                                          #blue led on
            ser.close()

            cx1=blue_bed[2]
            cy1=blue_bed[3]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from blue marker to blue bed
            inside()
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("d")                                          #blue led off

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
            ser.write("e")                                          #yellow led on
            ser.close()

            cx1=red_marker[0]
            cy1=red_marker[1]
            
            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from yellow marker to red mark

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("p")                                          #red led on
            ser.close()

            cx2=yellow_bed[0]
            cy2=yellow_bed[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from red marker to yellow bed
            inside()
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("f")                                          #yellow led off
            ser.close()

            cx1=red_bed[0]
            cy1=red_bed[1]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  yellow bed to red bed
            inside()
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("q")                                          #red led off
            ser.close()

            cx2=yellow_marker[0]
            cy2=yellow_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from red bed to yellow marker

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("e")                                          #yellow led on
            ser.close()

            cx1=yellow_bed[2]
            cy1=yellow_bed[3]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from yellow marker to yellow bed

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("f")                                          #yellow led off
            inside()
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
            ser.write("e")                                          #yellow led on
            ser.close()

            cx1=blue_marker[0]
            cy1=blue_marker[1]
            
            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from yellow marker to blue mark

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("r")                                          #blue led on
            ser.close()

            cx2=yellow_bed[0]
            cy2=yellow_bed[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from blue marker to yellow bed
            inside()
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("f")                                          #yellow led off
            ser.close()

            cx1=blue_bed[0]
            cy1=blue_bed[1]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  yellow bed to blue bed
            inside()
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("s")                                          #blue led off
            ser.close()

            cx2=yellow_marker[0]
            cy2=yellow_marker[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from blue bed to yellow marker

            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("e")                                          #yellow led on
            ser.close()

            cx1=yellow_bed[2]
            cy1=yellow_bed[3]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from yellow marker to yellow bed
            inside()
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("f")                                          #yellow led off

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
            ser.write("r")                                          #blue led on
            ser.close()

            cx2=red_bed[0]
            cy2=red_bed[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from blue marker to red bed
            inside()
            
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("b")                                          #red led off
            ser.close()

            cx1=blue_bed[0]
            cy1=blue_bed[1]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  red bed to blue bed
            inside()
            
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("s")                                          #blue led off
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

            inside()
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
            ser.write("t")                                          #yellow led on
            ser.close()

            cx2=red_bed[0]
            cy2=red_bed[1]

            d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow marker to red bed

            inside()
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("b")                                          #red led off
            ser.close()

            cx1=yellow_bed[0]
            cy1=yellow_bed[1]

            d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  red bed to yellow bed

            inside()
            ser = serial.Serial(3,timeout=1)
            ser.baudrate = 9600
            ser.write("u")                                          #yellow led off
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

            inside()
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

        inside()
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
        inside()
        
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

        inside()
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
        ser.write("c")                                          #blue led on
        ser.close()

        cx1=blue_bed[0]
        cy1=blue_bed[1]
        
        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from blue marker to blue bed
        inside()
        
        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("d")                                          #blue led off
        ser.close()

        cx2=blue_marker[0]
        cy2=blue_marker[1]

        d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from blue bed to blue marker

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("c")                                          #blue led on
        ser.close()

        cx1=blue_bed[2]
        cy1=blue_bed[3]

        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  blue marker to blue bed

        inside()
        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("d")                                          #blue led off
        ser.close()

        cx2=blue_marker[0]
        cy2=blue_marker[1]

        d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from blue bed to blue marker

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("c")                                          #blue led on
        ser.close()

        cx1=blue_bed[4]
        cy1=blue_bed[5]

        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from blue marker to blue bed
        inside()
        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("d")                                          #blue led off

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
        ser.write("e")                                          #yellow led on
        ser.close()

        cx1=yellow_bed[0]
        cy1=yellow_bed[1]
        
        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from yellow marker to yellow bed
        inside()
        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("f")                                          #yellow led off
        ser.close()

        cx2=yellow_marker[0]
        cy2=yellow_marker[1]

        d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow bed to yellow marker

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("e")                                          #yellow led on
        ser.close()

        cx1=yellow_bed[2]
        cy1=yellow_bed[3]

        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from  yellow marker to yellow bed
        inside()
        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("f")                                          #yellow led off
        ser.close()

        cx2=yellow_marker[0]
        cy2=yellow_marker[1]

        d=get_shortestpath(cx1,cy1,cx2,cy2,d)               #path from yellow bed to yellow marker

        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("e")                                          #yellow led on
        ser.close()

        cx1=yellow_bed[4]
        cy1=yellow_bed[5]

        d=get_shortestpath(cx2,cy2,cx1,cy1,d)               #path from yellow marker to yellow bed
        inside()
        ser = serial.Serial(3,timeout=1)
        ser.baudrate = 9600
        ser.write("f")                                          #yellow led off

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
    b1,g1,r1=img[80,280]
    print b1,g1,r1
    b2,g2,r2=img[240,280]
    print b2,g2,r2
    b3,g3,r3=img[440,280]
    print b3,g3,r3
    if(b1<b2):
        if(b3<b1):
            small=b3
        elif(b3>b1):
            small=b1
      
    elif(b1>b2):
        if(b3<b2):
            small=b3
        elif(b3>b2):
            small=b2
            
    if(b1==small):
        cbotx=280
        cboty=80
    elif(b2==small):
        cbotx=280
        cboty=240
    elif(b3==small):
        cbotx=280
        cboty=440
    print b1,g1,r1   
    return cbotx,cboty






'''
*
*Function Name: bot_direction
*
*Input: img->image captured from camera is passed to it and it gives bot coordinates
*Output: d->direction parameter of the bot
*Logic: image is converted to grayscale and then threshed, now it is blured to get
*       contour of the bot, whose centroid is the bot position
*Example Call: c1,c2 = bot_direction(img)   ->where img is image captured
*
'''
def bot_direction(img):
    param1 = [250,250,250]
    param2 = [255,255,255]
    lower = np.array(param1)
    upper = np.array(param2)
    mask = cv2.inRange(img, lower, upper)
    frame= cv2.bitwise_and(img, img, mask=mask)
    blur3 = cv2.medianBlur(frame,11)
    ret,thresh7 = cv2.threshold(blur3,150,255,cv2.THRESH_BINARY_INV)
    gray =cv2.cvtColor(thresh7, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,150,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    n=len(contours)
    for i in range(0,n):
        M = cv2.moments(contours[i])
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        if(cx>200)&(cx<360):
            area=cv2.contourArea(contours[i])
            if(area>60)&(area<100):
                c=i
            cxu=cx
            cyu=cy
    print cx,cy
    if(cy<150):
        if(cy<80)&(cx<280):
            d=3
        elif(cy<80)&(cx>320):
            d=4
        elif(cy>80):
            d=2
        else:
            d=1
    if(cy>150)&(cy<320):
        if(cy<270)&(cx<280):
            d=3
        elif(cy<270)&(cx>300):
            d=4
        elif(cy>270):
            d=2
        else:
            d=1
    if(cy>320)&(cy<480):
        if(cy<440)&(cx<280):
            d=3
        elif(cy<440)&(cx>300):
            d=4
        elif(cy>440):
            d=2
        else:
            d=1
    return d





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
    param1 = [0,80,80]                                 #parameters for yellow colour range
    param2 = [100,255,255]
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
            if(cyx>0)&(cyx<240)&(cyy>0)&(cyy<160):
                cyx=160
                cyy=80
                yellow_marker.append(cyx)
                yellow_marker.append(cyy)
            elif(cyx>0)&(cyx<240)&(cyy>200)&(cyy<320):
                 cyx=160
                 cyy=280
                 yellow_marker.append(cyx)
                 yellow_marker.append(cyy)
            elif(cyx>0)&(cyx<240)&(cyy>320)&(cyy<480):
                 cyx=160
                 cyy=440
                 yellow_marker.append(cyx)
                 yellow_marker.append(cyy)
        else:
            if(cyx>320)&(cyx<640)&(cyy>0)&(cyy<160):
                cyx=400
                cyy=160
                yellow_bed.append(cyx)
                yellow_bed.append(cyy)
            elif(cyx>320)&(cyx<640)&(cyy>200)&(cyy<320):
                 cyx=400
                 cyy=280
                 yellow_bed.append(cyx)
                 yellow_bed.append(cyy)
            elif(cyx>320)&(cyx<640)&(cyy>320)&(cyy<480):
                 cyx=400
                 cyy=440
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
            if(cbx>0)&(cbx<240)&(cby>0)&(cby<160):
                cbx=160
                cby=80
                blue_marker.append(cbx)
                blue_marker.append(cby)
            elif(cbx>0)&(cbx<240)&(cby>200)&(cby<320):
                 cbx=160
                 cby=280
                 blue_marker.append(cbx)
                 blue_marker.append(cby)
            elif(cbx>0)&(cbx<240)&(cby>320)&(cby<480):
                 cbx=160
                 cby=440
                 blue_marker.append(cbx)
                 blue_marker.append(cby)   
        else:
            if(cbx>320)&(cbx<640)&(cby>0)&(cby<160):
                cbx=400
                cby=160
                blue_bed.append(cbx)
                blue_bed.append(cby)
            elif(cbx>320)&(cbx<640)&(cby>200)&(cby<320):
                 cbx=400
                 cby=280
                 blue_bed.append(cbx)
                 blue_bed.append(cby)
            elif(cbx>320)&(cbx<640)&(cby>320)&(cby<480):
                 cbx=400
                 cby=440
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
    param1 = [0,0,150]                                                         #parameters for red colour range
    param2 = [100,100,255]
    lower = np.array(param1)
    upper = np.array(param2)
    mask  = cv2.inRange(img,lower, upper)
    res1   = cv2.bitwise_and(img, img, mask= mask)
    gray = cv2.cvtColor(res1,cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(gray,127,255,cv2.THRESH_TRUNC)
    blur3 = cv2.medianBlur(thresh1,19)
    contours, hierarchy = cv2.findContours(blur3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    l=len(contours)
    red_marker=[]
    red_bed=[]
    for i in range(0,l):
        M1 = cv2.moments(contours[i])                            
        crx = int(M1['m10']/M1['m00'])
        cry = int(M1['m01']/M1['m00'])
        if(crx<200):
            if(crx>0)&(crx<240)&(cry>0)&(cry<160):
                crx=160
                cry=80
                red_marker.append(crx)
                red_marker.append(cry)
            elif(crx>0)&(crx<240)&(cry>200)&(cry<320):
                 crx=160
                 cry=240
                 red_marker.append(crx)
                 red_marker.append(cry)
            elif(crx>0)&(crx<240)&(cry>320)&(cry<480):
                 crx=160
                 cry=440
                 red_marker.append(crx)
                 red_marker.append(cry)   
        else:
            if(crx>320)&(crx<640)&(cry>0)&(cry<160):
                crx=400
                cry=120
                red_bed.append(crx)
                red_bed.append(cry)
            elif(crx>320)&(crx<640)&(cry>200)&(cry<320):
                 crx=400
                 cry=280
                 red_bed.append(crx)
                 red_bed.append(cry)
            elif(crx>320)&(crx<640)&(cry>320)&(cry<480):
                 crx=400
                 cry=440
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
#frame = cv2.imread('sample1.jpg')
img = get_perspective_image(frame)                                   #inside of rectangle is cropped

#####now img is cropped image in 400x400 resolution                                                                     
#####Co-ordinates of all the required points are obtained

#cbotx,cboty = bot_position(img)
cbotx=280
cboty=80
print cbotx,cboty

#d=bot_direction(img)     #direction parameter of the robot initially set to 1:     1->North      2->South    3->East   4->West
d=1
print d

yellow_marker,yellow_bed = yellow_coordinates(img)                      #coordinates of yellow colour
blue_marker,blue_bed = blue_coordinates(img)                            #coordinates of blue colour
red_marker,red_bed = red_coordinates(img)                               #coordinates of red colour

b1=len(blue_bed)
r1=len(red_bed)
y1=len(yellow_bed)
b2=len(blue_marker)
r2=len(red_marker)
y2=len(yellow_marker)

cv2.circle(img,(cbotx,cboty), 5, (255,255,255), -1)

if(y2!=0):
    for i in range(0,y2,2):
        cv2.circle(img,(yellow_marker[i],yellow_marker[i+1]), 5, (255,255,255), -1)
if(y1!=0):
    for i in range(0,y1,2):
        cv2.circle(img,(yellow_bed[i],yellow_bed[i+1]), 5, (255,255,255), -1)
if(b2!=0):
    for i in range(0,b2,2):
        cv2.circle(img,(blue_marker[i],blue_marker[i+1]), 5, (255,255,255), -1)
if(b1!=0):
    for i in range(0,b1,2):
        cv2.circle(img,(blue_bed[i],blue_bed[i+1]), 5, (255,255,255), -1)
if(r2!=0):
    for i in range(0,r2,2):
        cv2.circle(img,(red_marker[i],red_marker[i+1]), 5, (255,255,255), -1)
if(r1!=0):
    for i in range(0,r1,2):
        cv2.circle(img,(red_bed[i],red_bed[i+1]), 5, (255,255,255), -1)




#white points
for i in range(2,12):
    cv2.circle(img,(280,40*i), 5, (255,255,255), -1)
    cv2.circle(img,(160,40*i), 5, (255,255,255), -1)
    cv2.circle(img,(400,40*i), 5, (255,255,255), -1)
for i in range(4,10):
    cv2.circle(img,(40*i,80), 5, (255,255,255), -1)
for i in range(4,10):
    cv2.circle(img,(40*i,200), 5, (255,255,255), -1)
for i in range(4,10):
    cv2.circle(img,(40*i,320), 5, (255,255,255), -1)
for i in range(4,10):
    cv2.circle(img,(40*i,440), 5, (255,255,255), -1)
cv2.circle(img,(320,40), 5,(255,255,255), -1)
cv2.circle(img,(320,80), 5,(255,255,255), -1)
cv2.circle(img,(320,200), 5,(255,255,255), -1)
cv2.circle(img,(320,240), 5,(255,255,255), -1)
cv2.circle(img,(320,360), 5,(255,255,255), -1)
cv2.circle(img,(320,440), 5,(255,255,255), -1)




for  i in range(0,10):
    cv2.circle(img,(120,40*i), 5, (0,0,0), -1)

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

cv2.rectangle(blur,(250,20),(350,460),(255,255,255),-1)

################################################
#obstacles
cv2.circle(blur,(200,160), 5, (0,0,0), -1)
cv2.circle(blur,(200,120), 5, (0,0,0), -1)
cv2.circle(blur,(200,240), 5, (0,0,0), -1)
cv2.circle(blur,(200,280), 5, (0,0,0), -1)
cv2.circle(blur,(200,360), 5, (0,0,0), -1)
cv2.circle(blur,(200,400), 5, (0,0,0), -1)

cv2.circle(blur,(240,160), 5, (0,0,0), -1)
cv2.circle(blur,(240,120), 5, (0,0,0), -1)
cv2.circle(blur,(240,240), 5, (0,0,0), -1)
cv2.circle(blur,(240,280), 5, (0,0,0), -1)
cv2.circle(blur,(240,360), 5, (0,0,0), -1)
cv2.circle(blur,(240,400), 5, (0,0,0), -1)

cv2.circle(blur,(320,160), 5, (0,0,0), -1)
cv2.circle(blur,(320,120), 5, (0,0,0), -1)
cv2.circle(blur,(320,240), 5, (0,0,0), -1)
cv2.circle(blur,(320,280), 5, (0,0,0), -1)
cv2.circle(blur,(320,360), 5, (0,0,0), -1)
cv2.circle(blur,(320,400), 5, (0,0,0), -1)

cv2.circle(blur,(360,160), 5, (0,0,0), -1)
cv2.circle(blur,(360,120), 5, (0,0,0), -1)
cv2.circle(blur,(360,240), 5, (0,0,0), -1)
cv2.circle(blur,(360,280), 5, (0,0,0), -1)
cv2.circle(blur,(360,360), 5, (0,0,0), -1)
cv2.circle(blur,(360,400), 5, (0,0,0), -1)



####functions are called with appropiate start and end points......as per the original configuration


if(cboty==240)&(d==1)|(cboty==440):
    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600
    ser.write("g")
    time.sleep(0.5)
    ser.write("5")
    time.sleep(0.5)
    ser.close()
elif(cboty==240)&(d==2):
    ser = serial.Serial(3,timeout=1)
    ser.baudrate = 9600
    ser.write("2")
    time.sleep(0.2)
    ser.write("5")
    time.sleep(1)
    ser.close()    

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
#cv2.imshow('image1',blue3)
cv2.imshow('blur',blur)
cv2.imshow('image',img)

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
