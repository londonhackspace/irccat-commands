#!/usr/bin/env python
import nextevent

dates = [
  (2011,  7, 27),
  (2013, 11, 27),
]

start, end = nextevent.get(dates, '20:00')
nextevent.printmsg('Next general meeting', 'beer', start)
