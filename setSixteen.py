#!/usr/bin/env python
#
# Do not delete this, it's needed for ?sixteen
#

import sys, time, re, urllib, urllib2

args = sys.argv
host = args[1]
message = " ".join(args[2:])

#Shorten message to 21 chars or less
message = message[:162]

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
urllib2.urlopen("http://%s:8022/%s" % (host, message))
