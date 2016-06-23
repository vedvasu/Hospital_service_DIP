import serial
import numpy as np
import cv2
import time 
ser = serial.Serial(3,timeout=1) 
print ser
ser.baudrate = 9600

##ser.write("6")
##time.sleep(1.5)
##ser.write("5")
##time.sleep(0.2)
##
##ser.write("8")
##time.sleep(1.5)
##ser.write("5")
##time.sleep(0.2)
####
##ser.write("6")
##time.sleep(0.65)
##ser.write("5")
##time.sleep(0.2)
##
##ser.write("8")
##time.sleep(1.7)
##ser.write("5")
##time.sleep(0.2)
####
##ser.write("6")
##time.sleep(0.7)
##ser.write("5")
##time.sleep(0.2)
##
##ser.write("8")
##time.sleep(1.5)
##ser.write("5")
##time.sleep(0.2)
##
##ser.write("4")
##time.sleep(1.5)
##ser.write("5")
##time.sleep(0.2)

#reached yellow provision
ser.write("c")########################
time.sleep(3)

ser.write("a")########################
time.sleep(3)
ser.write("8")
time.sleep(2)
ser.write("5")
time.sleep(0.2)

#reached red provision
ser.write("a")########################
time.sleep(3)

ser.write("4")
time.sleep(1.5)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(0.6)
ser.write("5")
time.sleep(0.2)

ser.write("6")
time.sleep(0.7)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(1.8)
ser.write("5")
time.sleep(0.2)

ser.write("4")
time.sleep(0.8)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(1.8)
ser.write("5")
time.sleep(0.2)

ser.write("6")
time.sleep(0.7)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(2.5)
ser.write("5")
time.sleep(0.2)

#reached red cupbord
ser.write("b")########################
time.sleep(3)


ser.write("6")
time.sleep(1.4)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(0.7)
ser.write("5")
time.sleep(0.2)

ser.write("4")
time.sleep(0.75)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(2)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(2.5)
ser.write("5")
time.sleep(0.2)

ser.write("4")
time.sleep(0.9)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(1.2)
ser.write("5")
time.sleep(0.2)


#reached yellow cupbord
ser.write("d")########################
time.sleep(3)


ser.write("6")
time.sleep(1.5)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(3)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(2)
ser.write("5")
time.sleep(0.2)


#reached blue provision
ser.write("e")########################
time.sleep(3)

ser.write("4")
time.sleep(1.6)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(2)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(2)
ser.write("5")
time.sleep(0.2)

ser.write("4")
time.sleep(0.8)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(2)
ser.write("5")
time.sleep(0.2)

ser.write("6")
time.sleep(0.7)
ser.write("5")
time.sleep(0.2)

ser.write("8")
time.sleep(0.5)
ser.write("5")
time.sleep(0.2)


#reached blue cupboard
ser.write("f")########################
time.sleep(3)

###buzzer
ser.write("7")########################
time.sleep(6)

ser.write("9")

ser.close()
