#!/usr/bin/env python
import nextevent

dates = [
  (2012, 02, 10),
  (2013, 02, 8),
  (2014, 02, 10),
]

start, end = nextevent.get(dates, '19:30')
nextevent.printmsg('Next Birthday','beer', start)
