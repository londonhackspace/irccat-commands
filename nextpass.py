#!/usr/bin/env python
from lhsephem import getbody, lhs, compass
import sys, math
from pytz import timezone, utc

def print_nextpass(sat, loc):
    sat.compute(loc)

    rt, ra, tt, ta, st, sa = loc.next_pass(sat)

    london = timezone('Europe/London')
    if not all([rt, tt, st]):
        print dir(sat)
        # I don't understand how this can happen, but it does for
        # ['ISS (ZARYA)', '1 25544U 98067A   14122.59948867 -.00006135  00000-0 -10042-3 0  2019', '2 25544  51.6474 325.5221 0002530 329.3158 128.9928 15.49779978884252']
        # at 2014/5/2 17:51:17
        # I also don't really understand why nextpass varies based on the date you pass in
        return

    rt, tt, st = [d.datetime().replace(tzinfo=utc) for d in [rt, tt, st]]
    rt, tt, st = [d.astimezone(london) for d in [rt, tt, st]]

    def reldt(curr, prev=None):

      if prev and curr.date() == prev.date():
        return curr.strftime('%H:%M:%S')

      return curr.strftime('%d/%m/%Y %H:%M:%S')


    msg = u'%s rise %s %s, transit %s alt %d\xb0, set %s %s %s' % (
      rt.strftime('%d/%m/%Y'),
      reldt(rt, rt), compass(ra),
      reldt(tt, rt), round(ta / (2 * math.pi) * 360),
      reldt(st, tt), rt.strftime('%Z'), compass(sa),
    )
    print msg.encode('utf-8')


args = sys.argv[5:]

if args:
  body = ' '.join(args)
else:
  sys.exit(1)

sat = getbody(body)
lhs.horizon = '30'
print_nextpass(sat, lhs)

#for i in range(30):
#    lhs.date = '2014/5/2 17:51:%s' % i
#    print_nextpass(sat, lhs)

