#!/usr/bin/env python
import json, urllib2

docks = (539, 96, 588)

for dock in docks:
    dockurl = "http://api.bike-stats.co.uk/service/rest/bikestat/%i?format=json" % (dock)
    dockstatus = urllib2.urlopen(dockurl)
    dock = json.load(dockstatus)
    dockstatus.close()
    print dock["dockStation"]["name"], '-- Bikes Available:', dock["dockStation"]["bikesAvailable"], '-- Empty Slots:', dock["dockStation"]["emptySlots"]
