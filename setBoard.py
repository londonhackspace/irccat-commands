#!/usr/bin/env python

import serial, sys, time, re, urllib, urllib2

args = sys.argv
message = " ".join(args[1::])

#Shorten message to 21 chars or less
message = message[:162]

if message == '' or re.match('^[ -~]+$', message):
    message = message
else:
    print 'Standard ASCII only please'
    port.close()
    sys.exit(0)

if message == '':
  print "Board cleared"
else:
  print "Displayed on board"

# Send to boarded
message = urllib.quote(message)
urllib2.urlopen("http://127.0.0.1:8020/%s" % message)
