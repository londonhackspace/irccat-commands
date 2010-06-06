#!/usr/bin/env python

import serial, sys, time, re

try:
    port = serial.Serial("/dev/ttyUSB1", 9600, timeout=1)
except:
    print "Could not connect to arduino"
    sys.exit(0)

args = sys.argv
message = " ".join(args[5::])

#Shorten message to 21 chars or less
message = message[:21]

if message == '' or re.match('^[ -~]+$', message):
    message = message
else:
    print 'Alphanumeric only please'
    port.close()
    sys.exit(0)

print "'%s' displayed on board" % message

#Add | if short
if len(message) < 21:
    message = message + "|"

#Send to arduino
port.write(message)
port.close()
