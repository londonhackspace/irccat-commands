#!/usr/bin/env python
import nextevent

dates = [
  (2011,  8,  2),
  (2013,  8,  13),
]

start, end = nextevent.get(dates, '17:00')
nextevent.printmsg('Next beer festival', 'beer', start)

