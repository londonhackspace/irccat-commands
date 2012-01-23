#!/usr/bin/env python
import nextevent

dates = [
  (2012,  1, 16),
  (2012,  1, 23),
  (2012,  1, 30),
]

start, end = nextevent.get(dates, '20:00')
nextevent.printmsg('Next Gadget Geeks', 'trolling', start)
