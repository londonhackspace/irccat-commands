#!/usr/bin/env python
from urllib import urlopen, urlencode
import json
from time import strptime, strftime
from datetime import datetime, timedelta

params = {
  'q': """
    select * from upcoming.events
    where location='London'
    and search_text='substandards'
  """,
  'format': 'json',
}
url = 'http://query.yahooapis.com/v1/public/yql?%s' % urlencode(params)
f = urlopen(url).read()
x = json.loads(f)
events = x['query']['results']['event']

def dayordinal(day):
  if 4 <= day <= 20 or 24 <= day <= 30:
    suffix = 'th'
  else:
    suffix = ['st', 'nd', 'rd'][day % 10 - 1]
  return '%d%s' % (day, suffix)

def untilmsg(until):
  hours, seconds = divmod(until.seconds, 3600)
  days = until.days
  d_s = '' if days == 1 else 's'
  h_s = '' if hours == 1 else 's'
  if hours == 0:
    return '%s day%s until beer!' % (days, d_s)
  elif days == 0:
    return 'Only %s hour%s until beer!' % (hours, h_s)
  else:
    return '%s day%s, %s hour%s until beer!' % (days, d_s, hours, h_s)


if not isinstance(events, list):
  e = events
  start = datetime.strptime(e['utc_start'], '%Y-%m-%d %H:%M:%S %Z')
  now = datetime.utcnow()
  until = start - now
  if until >= timedelta():
    print '%s: %s %s %s at %s, %s (%s)' % (
      e['name'],
      start.strftime('%A'),
      dayordinal(start.day),
      start.strftime('%B'),
      e['venue_name'],
      e['venue_zip'],
      untilmsg(until),
    )
