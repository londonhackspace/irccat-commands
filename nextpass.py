#!/usr/bin/env python
from lhsephem import fromtle, lhs
import sys, math
from pytz import timezone, utc

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

lhs.horizon = '30'

sat.compute(lhs)

rt, ra, tt, ta, st, sa = lhs.next_pass(sat)

london = timezone('Europe/London')
rt, tt, st = map(lambda d: d.datetime().replace(tzinfo=utc), (rt, tt, st))
rt, tt, st = map(lambda d: d.astimezone(london), (rt, tt, st))

def reldt(curr, prev=None):
  
  if prev and curr.date() == prev.date():
    return curr.strftime('%H:%M:%S')

  return curr.strftime('%d/%m/%Y %H:%M:%S')


def compass(angle):
  bearings = [
    'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
    'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW',
  ]
  sect = int(round(angle / (2 * math.pi) * len(bearings))) % len(bearings)
  return bearings[sect]


msg = u'%s rise %s %s, transit %s alt %d\xb0, set %s %s %s' % (
  rt.strftime('%d/%m/%Y'),
  reldt(rt, rt), compass(ra),
  reldt(tt, rt), round(ta / (2 * math.pi) * 360),
  reldt(st, tt), rt.strftime('%Z'), compass(sa),
)
print msg.encode('utf-8')
