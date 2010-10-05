#!/usr/bin/env python
import datetime
import sys

dates = [
  (2010, 8, 25),
  (2010, 9, 29),
  (2010, 10, 27),
  (2010, 11, 24),
  (2010, 12, 15),
]

meets = [datetime.datetime(y, m, d, 19, 30) for y, m, d in dates]

now = datetime.datetime.now()
future = [m for m in meets if m > now]
if not future:
  sys.exit(1)

next = min(future)
next_delta = next - now

def date_suffix(day):
  if 4 <= day <= 20 or 24 <= day <= 30:
    return 'th'
  else:
    return ['st', 'nd', 'rd'][day % 10 - 1]


when = next.strftime('%A %d%%s %B') % date_suffix(next.day)
until = '%d hours' % (next_delta.seconds / 3600)
if next_delta.days > 0:
  until = '%d days, %s' % (next_delta.days, until)

print 'Next monthly meeting: %s (%s until beer!)' % (when, until)

