#!/usr/bin/env python
from datetime import datetime, timedelta, date, time
import sys

class EventInProgress(Exception):
  pass

def get(nextdate, starttime='19:00', endtime='23:00'):
  '''
  If nextdate is a list, it's assumed to be a list of date/datetime tuples.
  
  If it's a function, it should return the next meeting on or after the
  date passed in.

  This can either be a single date, or a tuple of (start, end) datetimes.
  In the former case, starttime/endtime can be strings or datetime.times.
  In the latter case, they will be ignored.
  '''
  if not isinstance(starttime, time):
    starttime = datetime.strptime(starttime, '%H:%M').time()
  if not isinstance(endtime, time):
    endtime = datetime.strptime(endtime, '%H:%M').time()

  if isinstance(nextdate, list):
    # provide a basic implementation that will return the next
    # from a sorted list of start date/datetime tuples
    dates = []
    
    for d in nextdate:
      if len(d) == 3:
        d += (starttime.hour, starttime.minute, starttime.second)
      dates.append(d)

    def _nextdate(d):
      d = d.year, d.month, d.day, d.hour, d.minute, d.second
      future = [f for f in dates if f > d]
      # FIXME: take endtime into account
      if not future:
        return None
      start = datetime(*min(future))
      end = datetime.combine(start, endtime)
      return start, end

    nextdate = _nextdate

  now = datetime.now()
  d = nextdate(now)
  if not d:
    return None
  elif isinstance(d, tuple):
    start, end = d
  else:
    start, end = datetime.combine(d, starttime), datetime.combine(d, endtime)

  if start > now:
    return start, end
  elif end > now:
    raise EventInProgress

def date_suffix(day):
  if 4 <= day <= 20 or 24 <= day <= 30:
    return '%dth' % day
  else:
    return '%d%s' % (day, ['st', 'nd', 'rd'][day % 10 - 1])

def date_nice(dt):
  date = dt.strftime('%A %%s %B') % date_suffix(dt.day)

  if dt.year != datetime.now().date().year:
    date += ' %s' % dt.year

  return date

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


