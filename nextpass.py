#!/usr/bin/env python
from lhsephem import getbody, lhs, compass
import sys, math
from pytz import timezone, utc

args = sys.argv[5:]

if args:
  body = ' '.join(args)
else:
  sys.exit(1)

sat = getbody(body)

lhs.horizon = '30'

sat.compute(lhs)

rt, ra, tt, ta, st, sa = lhs.next_pass(sat)

london = timezone('Europe/London')
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
