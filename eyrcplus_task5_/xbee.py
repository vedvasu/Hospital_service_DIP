import serial
import numpy as np
import cv2
import time 
ser = serial.Serial(5,timeout=1) 
print ser
ser.baudrate = 9600

while(1):
    chutiyapa = raw_input("mc input dalo:")
    
    print (chutiyapa)
    ser.write(chutiyapa)
    time.sleep(1.2)

ser.close()
