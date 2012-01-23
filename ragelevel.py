#!/usr/bin/env python
import sys
import os
import urllib, urllib2
import time

#print 'Ragelevel is disabled for 4.2 minutes'
#os.quit()

#store current rage level in /tmp/ragelevel
#store last rage change in /tmp/rageChangeTime

levelText = ['peaceful', 'low', 'elevated', 'critical']

if sys.argv[3].startswith('#'):
    print 'Please use /msg for ragelevel'
    sys.exit(1)

if(len(sys.argv) <= 5):

    f = open('/tmp/ragelevel', 'r')

    level = f.read()
    level.strip()
    
    #last time the status was changed
    lastTime = os.stat("/tmp/ragelevel").st_mtime
    expiryTime =  ((lastTime + 300) - time.time()) / 60

    if(int(level) > 0) and expiryTime > 0:
        expString = "and it expires in %s minutes" % round(expiryTime, 1)
    else:
        expString = ""



    print "Current IRC rage level is", levelText[int(level)] , expString
    f.close()


else:
    levelIndex = -1
    level = sys.argv[5]
    level.strip()
    if(len(level) > 1):
        #a word was put in, find it in levelText
        count = 0
        try:
            levelIndex = levelText.index(level)
        except ValueError:
            print "Thats not a valid level, try 'peaceful', 'low', 'elevated', or 'critical'"
            sys.exit()
    else:
        levelIndex = int(level)

    f = open("/tmp/ragelevel",'w')
    f.write(str(levelIndex))
    f.close()
    #send a message to the board
    message = urllib.quote("$rage" + str(levelIndex))
    urllib2.urlopen("http://127.0.0.1:8020/%s" % message)
    
    print "Setting Rage Level to", levelText[levelIndex]


