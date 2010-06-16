#!/usr/bin/env python

import datetime

print '%s September 1993' % ((datetime.datetime.now() - datetime.datetime(1993, 9, 1)).days + 1)
