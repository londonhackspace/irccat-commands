#!/usr/bin/env python

import serial, sys, time, re

try:
    port = serial.Serial("/dev/ttyUSB1", 9600, timeout=1)
except:
    print "Could not connect to arduino"
    #port.close() //don't need to close if it couldnt open
    sys.exit(0)

args = sys.argv
message = " ".join(args[5::])

#Shorten message to 21 chars or less
message = message[:21]

if re.match('^[a-zA-Z0-9 ]+$', message):
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
time.sleep(2)
port.write(message)
time.sleep(1)
port.close()
