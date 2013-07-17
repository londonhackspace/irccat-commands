#!/usr/bin/env python
import nextevent

dates = [
  (2012,  12, 25),
]

start, end = nextevent.get(dates, '17:15')
nextevent.printmsg('Next Dr Who', 'teh fear', start)
