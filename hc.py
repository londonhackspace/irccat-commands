#!/usr/bin/env python
import nextevent

dates = [
  (2012,  8, 31),
]

start, end = nextevent.get(dates, '8:00')
nextevent.printmsg("Electromagnetic Field", 'hacking', start)
