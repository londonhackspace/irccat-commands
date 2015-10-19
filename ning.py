#!/usr/bin/python
import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print 'MORNING!'
if now.hour > 17:
    print 'EVENING!'

