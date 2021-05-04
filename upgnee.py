#!/usr/bin/python3
from datetime import timedelta
import math

if sys.argv[2] != 'null':
    print ('upword is private message only')
    sys.exit()


with open("/proc/uptime", "r") as f:
   seconds = int(float(f.readline().split()[0]) / 60 / 60 /24)

st = "GN" + "E"*seconds
print (st)
