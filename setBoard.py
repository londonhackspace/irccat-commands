#!/usr/bin/env python

import sys, time, re, urllib, urllib2

args = sys.argv
message = " ".join(args[1::])

#Shorten message to 21 chars or less
message = message[:162]

'\xc2\xa3'
if message == '' or re.match(u'^[\xc2\xa3 -~]+$', message):
    message = message
else:
    print 'Standard ASCII only please'
    sys.exit(0)

if message == '':
  print "Board cleared"
else:
  print "Displayed on board"

# Send to boarded
message = urllib.quote(message)
urllib2.urlopen("http://127.0.0.1:8020/%s" % message)
