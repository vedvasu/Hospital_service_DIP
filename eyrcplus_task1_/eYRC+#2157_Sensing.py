
############################################
## Import OpenCV
import numpy as np
import cv2

#### Processing
####### other helper functions
def masking(frame1):
    param1 = [50,200,200]
    param2 = [255,255,255]
    hsv = cv2.cvtColor(frame1,cv2.COLOR_BGR2HSV)
    lower = np.array(param1)    ## Convert the parameters into a form that OpenCV can understand
    upper = np.array(param2)
    mask  = cv2.inRange(hsv, lower, upper)           ## Detecting
    res1   = cv2.bitwise_and(frame1, frame1, mask= mask)
    return res1

def roll_image(res1):       
    h,w,c = res1.shape
    img1= res1[:,:(w/3),:]                          ##ROLLING
    return img1

def cont_image(img1):
    gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(gray,80,250,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    i=0
    for i in range(0,2):
        cv2.drawContours(img1,contours,i,(0,255,0),3)
        M = cv2.moments(contours[i])                 ##### Finding contour
        cx2 = int(M['m10']/M['m00'])
        cy2 = int(M['m01']/M['m00'])
        if i==0:
            cx1=cx2
            cy1=cy2
        cv2.circle(img1,(cx1,cy1), 5, (0,0,255), -1)
    return cx1,cy1,cx2,cy2

def math_image(cx1,cy1,cx2,cy2):
    x=cx2-cx1
    y=cy2-cy1
    res=((600-cx2)*y/x)+cy2            ##### MATHMATICS of detect ball in straight 
    k=(res/60)+1                        ###### to find ball number
    return k
    

############# END OF HELPER FUNCTION #################################


############
def play(frame):
    '''
    img-- a single test image as input argument
    ball_number  -- returns the single integer specifying the target that was 
    hit  eg. 1, 5, etc
    '''

    res=masking(frame)
    img2=roll_image(res)
    cx1,cy1,cx2,cy2=cont_image(img2)
    ball_number=math_image(cx1,cy1,cx2,cy2)
    return ball_number

   
    
if __name__ == "__main__":
    #checking output for single image
    img= cv2.imread('test_images/1.jpg')
    ball_number = play(img)
    print ball_number, " number ball at target range"
    #checking output for all images
    num_list = []
    for file_number in range(1,9):
        file_name = "test_images/"+str(file_number)+".jpg"
        pic= cv2.imread(file_name)
        ball_number=play(pic)
        num_list.append(ball_number)
    print num_list 
