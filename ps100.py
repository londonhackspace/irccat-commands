#!/usr/bin/env python
import nextevent

dates = [
  (2014,  3, 13),
]

try:
    start, end = nextevent.get(dates, '12:00')
    nextevent.printmsg("Pub Standards 100", 'party poppers and beer', start)
except TypeError:
    print "Pub Standards 100 was amazing."
