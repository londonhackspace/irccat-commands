#!/usr/bin/env python
import json, urllib2

docks = [539, 96]
results = []

for dock in docks:
    dockurl = "http://api.bike-stats.co.uk/service/rest/bikestat/%i?format=json" % (dock)
    dockstatus = urllib2.urlopen(dockurl)
    dock = json.load(dockstatus)
    dockstatus.close()
    dockname = dock["dockStation"]["name"].split(',')[0]
    bikesavail = int(dock["dockStation"]["bikesAvailable"])
    emptyslots = int(dock["dockStation"]["emptySlots"])
    dockinfo = '%s: %i (%i empty)' % (dockname, bikesavail, emptyslots)
    results.append(dockinfo)

    if (bikesavail <= 1) and (588 not in docks):
        docks.append(588)

print ", ".join(map(str, results))
