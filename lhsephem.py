#!/usr/bin/env python
import ephem
from urllib import urlopen

def xchunk(l, n):
  for i in xrange(0, len(l), n):
    yield l[i:i+n]

def chunk(l, n):
  return [l[i:i+n] for i in range(0, len(l), n)]

TLES = {}

# For more see http://celestrak.com/NORAD/elements/
def fromtle(url, body):
  if url not in TLES:
    f = urlopen(url)
    TLES[url] = chunk(f.readlines(), 3)

  for tle in TLES[url]:
    if tle[0].strip().lower() == body.lower():
      return ephem.readtle(*tle)

  else:
    raise KeyError('%s not found in %s' % (body, url))

lhs = ephem.Observer()
lhs.lat = '51.5322'
lhs.long = '-0.0606'
# base from http://www.daftlogic.com/sandbox-google-maps-find-altitude.htm
lhs.elevation = 22 # +- 2m
