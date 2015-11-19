#!/usr/bin/env python
import nextevent

dates = [(year, 12, 25) for year in range(2011, 2031)]

start, end = nextevent.get(dates, '00:00')
nextevent.printmsg('Christmas day', 'presents', start)
