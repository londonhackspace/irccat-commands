#!/usr/bin/env python
import nextevent

dates = [
  (2012,  7, 21),
]

start, end = nextevent.get(dates, '9:00')
nextevent.printmsg("Jonty's torch run", 'lols', start)
