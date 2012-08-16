#!/usr/bin/env python
import nextevent

dates = [
  (2014,  3, 13),
]

start, end = nextevent.get(dates, '18:00')
nextevent.printmsg("Pub Standards 100", 'beer', start)
