#!/usr/bin/env python
import json, urllib2

docks = (539, 96, 588)

for dock in docks:
    dockurl = "http://api.bike-stats.co.uk/service/rest/bikestat/%i?format=json" % (dock)
    dockstatus = urllib2.urlopen(dockurl)
    dock = json.load(dockstatus)
    dockstatus.close()
    print 'Location:', dock["dockStation"]["name"]
    print 'Bikes Available:', dock["dockStation"]["bikesAvailable"]
    print 'Empty Slots:', dock["dockStation"]["emptySlots"]
    print '\n'
