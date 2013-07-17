#!/usr/bin/env python
import nextevent

dates = [
  (2013, 5, 5),
]

start, end = nextevent.get(dates, '10:00')
nextevent.printmsg("Boat thingy", 'booze', start)
