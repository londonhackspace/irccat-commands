#!/usr/bin/env python
from urllib import urlopen
import json

def getnextbuses(stop):

    f = urlopen('http://countdown.tfl.gov.uk/stopBoard/%s' % stop)
    d = json.load(f)

    next = {}

    for bus in d['arrivals']:
        if bus['routeId'] not in next and not bus['isCancelled']:
            next[bus['routeId']] = bus
    return next

west = getnextbuses('76309')
east = getnextbuses('48630')

def wait_key(bus):
    wait, _, unit = bus['estimatedWait'].partition(' ')
    if wait == 'due':
        wait = 0
    elif unit == 'min':
        wait = int(wait)
    return wait, bus['routeId']

west = sorted(west.values(), key=wait_key)
east = sorted(east.values(), key=wait_key)

westmsg = ', '.join('%s in %s' % (b['routeId'], b['estimatedWait'].replace(' ', '')) for b in west)
eastmsg = ', '.join('%s in %s' % (b['routeId'], b['estimatedWait'].replace(' ', '')) for b in east)

print ('Going west: %s; Going east: %s' % (westmsg, eastmsg))
