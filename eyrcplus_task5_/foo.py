import xbeex
import os

while(True):
    i=raw_input();
    if (i!='q'):
        print i
        os.system("xbeex.py "+i)
    else:
        break

