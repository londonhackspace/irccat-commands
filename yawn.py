#!/usr/bin/python33
import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print '...ning... zzz...'
else:
    print '...yaaaaaaaawwwwwwnnn...'

