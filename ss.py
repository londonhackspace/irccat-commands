#!/usr/bin/env python
from datetime import date
import nextevent

dates = {
  (2012,  2,  2): ('Recrudescence', 'Bricklayers Arms', 'W1T 1QS'),
  (2012,  3,  1): ('Warmongers', 'Gunmakers', 'EC1R 5ET'),
  (2012,  3, 29): ('Blue Marlin', 'The Fellow', 'N1 9AA'),
  (2012, 10,  4): ('Kernel Panic', 'The Old Fountain', 'EC1V 9NU'),
  (2012, 11, 29): ('Shipping Forecast', 'The Ship Tavern', 'WC2A 3HP'),
  (2014,  6, 19): ('Calendar', 'Bricklayers Arms', 'W1T 1QS'),
  (2014,  7, 31): ('Parklife', 'Regents Park', 'NW1 4NR'),
  (2015,  2, 26): ('How Do I Even', 'Cask Pub & Kitchen', 'SW1V 2EE'),
  (2015, 12, 15): ('Decimalisation', 'UNKNOWN', 'London'),
}

def next_meet(fromd):
  fromd = fromd.year, fromd.month, fromd.day
  future = [d for d in dates if d >= fromd]
  if not future:
    return None
  return date(*min(future))

start, end = nextevent.get(next_meet, '18:00')

name, venue, postcode = dates[(start.year, start.month, start.day)]

print 'Substandards %s: %s at %s, %s (%s until beer!)' % (
  name,
  nextevent.date_nice(start),
  venue,
  postcode,
  nextevent.untilmsg(start),
)

