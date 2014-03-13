#!/usr/bin/env python
from lhsephem import fromtle, lhs
import sys

args = sys.argv[5:]

if args:
  body = ' '.join(args)
else:
  sys.exit(1)

sources = {
    'norad': 'http://celestrak.com/NORAD/elements/stations.txt',
    'kepler': 'http://mstl.atl.calpoly.edu/~ops/keps/kepler.txt',
}

bodies = {
  'iss': ('norad', 'ISS (ZARYA)'),
  'kicksat': ('kepler', 'KickSat'),
}
source, alias = bodies[body]

sat = fromtle(sources[source], alias)

sat.compute(lhs)
msg = 'Height %dkm, distance %dkm %skm/s, magnitude %s' % (
  round(sat.elevation / 1000), round(sat.range / 1000),
  round(sat.range_velocity / 1000, 2), sat.mag
)

if sat.eclipsed:
  msg += ', eclipsed'

print msg
