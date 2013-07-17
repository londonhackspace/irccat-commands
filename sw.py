#!/usr/bin/env python
import nextevent

dates = [
  (2013, 5, 12),
]

start, end = nextevent.get(dates, '12:00')
nextevent.printmsg("Spacewarming party", 'beer', start)
