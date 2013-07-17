#!/usr/bin/env python
import nextevent

dates = [
  (2011,  1, 25),
  (2011,  2, 22),
  (2011,  3, 22),
  (2011,  4, 20),
  (2011,  5, 24),
  (2011,  6, 21),
  (2011,  7, 19),
  (2011,  8, 23),
  (2011,  9, 20),
  (2011, 10, 18),
  (2011, 11, 15),
  (2011, 12, 13),
  (2012,  1, 24),
  (2012,  2, 21),
  (2012,  3, 20),
  (2012,  4, 24),
  (2012,  5, 22),
  (2012,  6, 19),
  (2012,  7, 17),
  (2012,  8, 21),
  (2012,  9, 18),
  (2012, 10, 23),
  (2012, 11, 20),
  (2012, 12, 11),
  (2013,  1, 29),
  (2013,  2, 26),
  (2013,  3, 26),
  (2013,  4, 23),
  (2013,  5, 28),
  (2013,  6, 25),
  (2013,  7, 30),
  (2013,  8, 27),
  (2013,  9, 24),
  (2013, 10, 29),
  (2013, 11, 26),
  (2013, 12, 17),
]

start, end = nextevent.get(dates, '19:30')
nextevent.printmsg('Next monthly meeting', 'beer', start)
