import serial
import numpy as np
import cv2
import time 
ser = serial.Serial(2,timeout=1) 

print ser

ser.baudrate = 9600

ser.write("a")
time.sleep(2)
ser.write("b")
time.sleep(2)
ser.write("c")
time.sleep(2)
ser.write("d")
time.sleep(2)
ser.write("e")
time.sleep(2)
ser.write("f")
time.sleep(2)


##ser.write("p")
##time.sleep(1)
##ser.write("q")
##time.sleep(1)
##ser.write("r")
##time.sleep(5)
##ser.write("s")
##time.sleep(1)
##ser.write("t")
##time.sleep(1)
##ser.write("u")
##time.sleep(1)





ser.close()
