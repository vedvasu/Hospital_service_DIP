import numpy
import cv2
img = cv2.imread('.jpg')
i = 769
j = 769
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
while (gray[354,i]>20):    #finding the line of bullet shot
    if(i==0):
        break
    i=i-1
while (gray[368,j]>20):
    if(i==0):
        break
    j=j-1
w=j-293*(j-i)/14      #where the shot cuts the line at height=75px
#print "w=",w
def check(img1,img2):     #funtion for comparing colours of two pixels
    b1,g1,r1=img1
    b2,g2,r2=img2
    if(b1==b2 and g1==g2 and r1==r2):
        return 1
k=170
while(k>0):                     # comparing the colour of the intersection point with the balloon colour
    if (check(img[k,int(j+(k-368)*(j-i)/14)+1,:],img[75,35,:]) or w<20):
        print "L"
        break
    if (check(img[k,int(j+(k-368)*(j-i)/14)+1,:],img[75,105,:]) or check(img[k,int(j+(k-368)*(j-i)/14)+1,:],img[75,121,:])):
        print "M"
        break
    if (check(img[k,int(j+(k-368)*(j-i)/14)+1,:],img[75,175,:])):
        print "N"
        break
    if (check(img[k,int(j+(k-368)*(j-i)/14)+1,:],img[75,245,:]) or check(img[k,int(j+(k-368)*(j-i)/14)+1,:],img[75,226,:])):
        print "O"
        break
    if (check(img[k,int(j+(k-368)*(j-i)/14)+1,:],img[75,315,:])):
        print "P"
        break
    if (check(img[k,int(j+(k-368)*(j-i)/14)+1,:],img[75,385,:])):
        print "Q"
        break
    if (check(img[k,int(j+(k-368)*(j-i)/14)+1,:],img[75,455,:])):
        print "R"
        break
    if (check(img[k,int(j+(k-368)*(j-i)/14)+1,:],img[75,525,:])):
        print "S"
        break
    if (check(img[k,int(j+(k-368)*(j-i)/14)+1,:],img[75,595,:])):
        print "T"
        break
    if (check(img[k,int(j+(k-368)*(j-i)/14)+1,:],img[75,665,:])):
        print "U"
        break
    if (check(img[k,int(j+(k-368)*(j-i)/14)+1,:],img[75,735,:])):
        print "V"
        break
    k=k-1
#print int(j+(k-368)*(j-i)/14)+1



