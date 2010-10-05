#!/usr/bin/env python
from datetime import date, datetime, timedelta

def monthly_meeting(start):
  month_start = date(start.year, start.month, 1)
  wednesday_distance = (3 - month_start.isoweekday()) % 7
  third_wednesday = 1 + wednesday_distance + 7 * 2
  return datetime(start.year, start.month, third_wednesday, 19, 00)

start = datetime.now()
meeting = monthly_meeting(start)
if meeting < start:
  start += timedelta(31)
  meeting = monthly_meeting(start)

meeting_delta = meeting - datetime.now()

def date_suffix(day):
  if 4 <= day <= 20 or 24 <= day <= 30:
    return 'th'
  else:
    return ['st', 'nd', 'rd'][day % 10 - 1]


when = meeting.strftime('%A %d%%s %B') % date_suffix(meeting.day)
  
until = '%d hours' % (meeting_delta.seconds / 3600)
if meeting_delta.days > 0:
  until = '%d days, %s' % (meeting_delta.days, until)

print 'Next monthly meeting: %s (%s until hacking!)' % (when, until)
