#! /usr/bin/python

#f = open("/home/solexious/coolbot/totalTime", "r")
#seconds = int(f.read())

#hours = seconds / 3600
#minutes = (seconds % 3600) / 60
#seconds = (seconds % 3600) % 60

#print '%dh:%dm:%ds of lasing have occurred. Approximately %d hours until the tube dies.' % (hours, minutes, seconds, 700 - hours)

import time, datetime, urllib2, json

# solexious: russ posted on the ml about the new cutter being open for use on the 24/12/2014

start = datetime.datetime(2016, 12, 4)
start = int(time.mktime(start.timetuple()))

#solexious: 399h:56m:57s of lasing have occurred. was on the 18th of august

#coolbot = (399 * 3600) + (56 * 60) + 57
#start = start + coolbot

# the lasercutter is toolid 5
url = "http://acserver.london.hackspace.org.uk/api/get_tool_runtime_since/5/" + str(start)

ret = urllib2.urlopen(url).read()
ret = json.loads(ret)[0]

print "Laser tube hours: " + ret['verbose']

