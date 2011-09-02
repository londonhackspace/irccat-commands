#!/usr/bin/env python
from urllib import urlopen
import json

f = urlopen('http://countdown.tfl.gov.uk/stopBoard/47125')
d = json.load(f)

next = {}

for bus in d['arrivals']:
  if bus['routeId'] not in next and not bus['isCancelled']:
    next[bus['routeId']] = bus

print ', '.join('%s: %s' % (b['routeId'], b['estimatedWait']) for b in next.values())

