#!/usr/bin/env python
from datetime import timedelta
import nextevent

def next_meet(d):
  return d + timedelta(days=(4 - d.weekday()) % 7)

try:
  start, end = nextevent.get(next_meet, '18:00', '23:00')
except nextevent.EventInProgress:
  print 'Friday drinking is currently under way! Quick! Run to the pub!'
else:
  nextevent.printmsg('Next Friday drinking', 'beer', start)


