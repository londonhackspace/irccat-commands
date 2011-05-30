#!/usr/bin/env python
from lhsephem import fromtle, lhs
import sys

args = sys.argv[5:]

if args:
  body = ' '.join(args)
else:
  sys.exit(1)

aliases = {
  'iss': 'ISS (ZARYA)',
}
if body in aliases:
  body = aliases[body]

url = 'http://celestrak.com/NORAD/elements/stations.txt'
sat = fromtle(url, body)

sat.compute(lhs)
msg = 'Height %dkm, distance %dkm %dkm/s, magnitude %s' % (
  sat.elevation / 1000, sat.range / 1000, sat.range_velocity, sat.mag
)

if sat.eclipsed:
  msg += ', eclipsed'

print msg
