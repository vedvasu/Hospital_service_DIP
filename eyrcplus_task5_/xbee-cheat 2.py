import serial
import numpy as np
import cv2
import time 
#creating the serial object ser for connecting to the serial port
#if your com port is com21 put 20 as the com port number
ser = serial.Serial(2,timeout=1) 

#printing ser object attributes: baudrate, open, close etc
print ser

#for changing attributes just try following
ser.baudrate = 9600

#for sending data from ser

ser.write("6")
time.sleep(1.7)
ser.write("5")


ser.write("8")
time.sleep(1.5)
ser.write("5")

ser.write("6")
time.sleep(0.7)
ser.write("5")


ser.write("8")
time.sleep(1.7)
ser.write("5")


ser.write("6")
time.sleep(0.7)
ser.write("5")

ser.write("8")
time.sleep(1.5)
ser.write("5")


ser.write("4")
time.sleep(1.5)
ser.write("5")


ser.write("c")########################



ser.write("8")
time.sleep(2)
ser.write("5")


ser.write("a")########################

ser.write("4")
time.sleep(1.6)
ser.write("5")

ser.write("8")
time.sleep(0.7)
ser.write("5")


ser.write("6")
time.sleep(0.7)
ser.write("5")


ser.write("8")
time.sleep(1.8)
ser.write("5")

ser.write("4")
time.sleep(0.8)
ser.write("5")


ser.write("8")
time.sleep(1.3)
ser.write("5")


ser.write("6")
time.sleep(0.7)
ser.write("5")


ser.write("8")
time.sleep(2.5)
ser.write("5")



ser.write("b")########################




ser.write("6")
time.sleep(1.5)
ser.write("5")





ser.write("8")
time.sleep(0.7)
ser.write("5")

ser.write("4")
time.sleep(0.85)
ser.write("5")

ser.write("8")
time.sleep(2)
ser.write("5")


ser.write("8")
time.sleep(2.5)
ser.write("5")

ser.write("4")
time.sleep(0.9)
ser.write("5")

ser.write("8")
time.sleep(1.3)
ser.write("5")



ser.write("d")########################


ser.write("6")
time.sleep(1.4)
ser.write("5")


ser.write("8")
time.sleep(2.5)
ser.write("5")
time.sleep(0.5)

ser.write("8")
time.sleep(2)
ser.write("5")


ser.write("e")########################


ser.write("4")
time.sleep(1.6)
ser.write("5")

ser.write("8")
time.sleep(2)
ser.write("5")


ser.write("8")
time.sleep(2.2)
ser.write("5")

ser.write("4")
time.sleep(0.8)
ser.write("5")


ser.write("8")
time.sleep(1.9)
ser.write("5")


ser.write("6")
time.sleep(0.75)
ser.write("5")

ser.write("8")
time.sleep(0.3)
ser.write("5")


ser.write("f")########################

ser.write("7")########################
time.sleep(6)
set.write(5)

ser.close()
