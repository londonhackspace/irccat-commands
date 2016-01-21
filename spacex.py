#!/usr/bin/env python
import nextevent

dates = [
  (2015,  1,  6, 11, 20), # Dragon, scrubbed
  (2015,  1, 10,  9, 47), # Dragon
  (2015,  2,  8, 23, 10), # DSCOVR, scrubbed
  (2015,  2, 10, 23,  5), # DSCOVR
  (2015,  2, 17, 12,  0), # Eutelsat
  (2015,  3,  2,  3, 50),
  (2015,  6, 28, 15, 21),
  (2015, 12, 22,  1, 29), # ORBCOMM-2
]

start, end = nextevent.get(dates)
nextevent.printmsg('Next SpaceX launch', 'liftoff', start)
