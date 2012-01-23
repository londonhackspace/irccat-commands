#!/usr/bin/env python
from datetime import timedelta
import nextevent

def next_meet(d):
  return d + timedelta(days=(1 - d.weekday()) % 7)

try:
  start, end = nextevent.get(next_meet, '19:30', '22:30')
except nextevent.EventInProgress:
  print 'The weekly meeting is currently under way! Quick! Run to the space!'
else:
  nextevent.printmsg('Next weekly meeting', 'beer', start)


