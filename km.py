#!/usr/bin/env python
import nextevent

dates = [
  (2013,  8, 12),
]

start, end = nextevent.get(dates, '12:00')
nextevent.printmsg('Next Kernel launch', 'unrelenting bullshit', start)

