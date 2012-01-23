#!/usr/bin/env python
from datetime import datetime, timedelta, date, time
import sys

class EventInProgress(Exception):
  pass

def get(nextdate, starttime='19:00', endtime='23:00'):
  '''
  If nextdate is a list, it's assumed to be a list of date tuples.
  
  If it's a function, it should return the next meeting on or after the
  date passed in.

  This can either be a single date, or a tuple of (start, end) datetimes.
  In the former case, starttime/endtime can be strings or datetime.times.
  In the latter case, they will be ignored.
  '''

  if isinstance(nextdate, list):

    dates = nextdate

    def fromlist(d):
      d = d.year, d.month, d.day
      future = [f for f in dates if f >= d]
      if not future:
        return None
      return date(*min(future))

    nextdate = fromlist

  now = datetime.now()

  if not isinstance(starttime, time):
    starttime = datetime.strptime(starttime, '%H:%M').time()
  if not isinstance(endtime, time):
    endtime = datetime.strptime(endtime, '%H:%M').time()

  d = nextdate(now.date())
  if not d:
    return None
  elif not isinstance(d, tuple):
    start, end = datetime.combine(d, starttime), datetime.combine(d, endtime)
  else:
    start, end = d

  if start > now:
    return start, end
  elif end > now:
    raise EventInProgress

  d = nextdate(start.date() + timedelta(days=1))
  if not d:
    return None
  elif not isinstance(d, tuple):
    start, end = datetime.combine(d, starttime), datetime.combine(d, endtime)
  else:
    start, end = d

  return start, end

def date_suffix(day):
  if 4 <= day <= 20 or 24 <= day <= 30:
    return '%dth' % day
  else:
    return '%d%s' % (day, ['st', 'nd', 'rd'][day % 10 - 1])

def date_nice(dt):
  return dt.strftime('%A %%s %B') % date_suffix(dt.day)

def pluralise(fmt, n):
  return fmt % (n, int(n) != 1 and 's' or '')

def untilmsg(next):
  until = next - datetime.now()
  hours, seconds = divmod(until.seconds, 3600)
  days = until.days
  if days == 0:
    if hours == 0:
      return pluralise('Only %d minute%s', seconds / 60)
    return pluralise('Only %d hour%s', hours)
  return '%s, %s' % (pluralise('%d day%s', days), pluralise('%d hour%s', hours))

def printmsg(name, what, next):
  '''
  Format friendly message of when the next event is.

  NB No account is taken of timezones.
  '''

  print '%s: %s (%s until %s!)' % (
    name,
    date_nice(next),
    untilmsg(next),
    what,
  )


