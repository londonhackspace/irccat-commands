#!/usr/bin/env python
import nextevent

dates = [
  (2011, 11, 30),
  (2011, 12, 28),
  (2012,  1, 25),
  (2012,  2, 29),
  (2012,  3, 28),
  (2012,  4, 25),
]

start, end = nextevent.get(dates, '19:30')
nextevent.printmsg('Next Science Museum lates','beer', start)
