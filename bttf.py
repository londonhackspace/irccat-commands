#!/usr/bin/env python
import nextevent

dates = [
  (2015, 10, 22),  # because it's after midnight
]

start, end = nextevent.get(dates, '00:29')  # 16:29 PDT (-7), in BST (+1)
nextevent.printmsg('The Future', 'hoverboards', start)
