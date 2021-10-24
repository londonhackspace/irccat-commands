#!/usr/bin/python3

import sys, time, re, urllib, urllib.parse, urllib.request

args = sys.argv
host = args[1]
message = " ".join(args[2:])

#Shorten message to 21 chars or less
message = message[:162]

if message == '' or re.match(u'^[\xc2\xa3 -~]+$', message):
    message = message
else:
    print ('Standard ASCII only please')
    sys.exit(0)

if message == '':
  print ("Board cleared")
else:
  print ("Displayed on board")

# Send to boarded
message = urllib.parse.quote(message)
url = "http://%s:8020/%s" % (host, message)
urllib.request.urlopen(url)
