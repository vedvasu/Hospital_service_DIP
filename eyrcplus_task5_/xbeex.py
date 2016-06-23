import serial
import sys



def go(i):
    ser = serial.Serial(5,timeout=1) 
    print ser,
    print
    print i
    ser.baudrate = 9600
    ser.write(i)
    ser.close()

if __name__=="__main__":
    while(1):
        i=sys.argv[0]
        go(i);
    
