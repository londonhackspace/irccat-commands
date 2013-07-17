#!/usr/bin/env python
import nextevent

dates = [
  (2012,  9, 12),
]

start, end = nextevent.get(dates, '18:00')
nextevent.printmsg("iPhone 5 Announcement", 'snark', start)
