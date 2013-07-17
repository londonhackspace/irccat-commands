#!/usr/bin/env python
import nextevent

dates = [
  (2012,  4, 1),
]

start, end = nextevent.get(dates, '01:00')
nextevent.printmsg("Wenlock Arms Closing", 'CLOSED FOR EVER', start)
