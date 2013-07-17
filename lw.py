#!/usr/bin/env python
import nextevent

dates = [
  (2013,  3,  1),
]

start, end = nextevent.get(dates, '20:00')
nextevent.printmsg("Last Wenlock", 'tears', start)
