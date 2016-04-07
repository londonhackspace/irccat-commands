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
  (2014,  1, 28),
  (2014,  2, 25),
  (2014,  3, 25),
  (2014,  4, 29),
  (2014,  5, 27),
  (2014,  6, 24),
  (2014,  7, 29),
  (2014,  8, 26),
  (2014,  9, 30),
  (2014, 10, 28),
  (2014, 11, 25),
  (2014, 12, 15),
  (2015,  1, 27),
  (2015,  2, 24),
  (2015,  3, 31),
  (2015,  4, 28),
  (2015,  5, 26),
  (2015,  6, 30),
  (2015,  7, 28),
  (2015,  8, 25),
  (2015,  9, 29),
  (2015, 10, 27),
  (2015, 11, 24),
  (2016,  1, 26),
  (2016,  2, 23),
  (2016,  3, 29),
  (2016,  4, 26),
  (2016,  5, 31),
  (2016,  6, 28),
  (2016,  7, 26),
  (2016,  8, 30),
  (2016,  9, 27),
  (2016, 10, 25),
  (2016, 11, 29),
]

if __name__ == '__main__':

    from dctalks import get_future_events, talk_getter
    from nextevent import date_nice, untilmsg

    start, end = nextevent.get(dates, '19:30')
    events = get_future_events()

    msg = "No talks yet! Email talks@dc4420.org if you'd like to give one."
    msg = "No talks yet!"
    if events:
        start, event = events[0]
        talks = list(talk_getter(event))
        if len(talks) == 1:
            msg = "One talk so far. Email talks@dc4420.org if you'd like to give the other."
            msg = "One talk so far!"

        elif len(talks) > 1:
            msg = "Type ?dctalks for a list of talks."

    print 'Next monthly meeting: %s (%s until beer!). %s' % (
      date_nice(start),
      untilmsg(start),
      msg,
    )

