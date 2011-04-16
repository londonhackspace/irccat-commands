#!/usr/bin/env python
import urllib
from datetime import datetime
from pytz import timezone, UTC
from operator import itemgetter
from collections import defaultdict

ics = urllib.urlopen('http://www.google.com/calendar/ical/gc1bopmh3c5n0ogvlo6ceujlkc%40group.calendar.google.com/public/basic.ics')

# Naive (non-recursive) parser for http://www.ietf.org/rfc/rfc2445.txt

events = []
state = None

for line in ics:
    line = line.rstrip('\r\n')
    k, c, v = line.partition(':')
    if k == 'BEGIN':
        state = v

    if state == 'VEVENT':
        if k == 'BEGIN':
            event = defaultdict(lambda: None)
        elif k == 'DTSTART':
            if k == 'DTSTART':
                try:
                    zone = UTC
                    dt = datetime.strptime(v, '%Y%m%dT%H%M%SZ')
                except ValueError:
                    zone = timezone('Europe/London')
                    dt = datetime.strptime(v, '%Y%m%d')
            else:
                k, s, tz = k.partition(';TZID=')
                dt = datetime.strptime(v, '%Y%m%dT%H%M%S')
                zone = timezone(tz)

            event['start'] = zone.localize(dt) # Throws if ambiguous

        elif k == 'SUMMARY':
            event['name'] = v

        elif k == 'DESCRIPTION':
            event['desc'] = v

        elif k == 'END':
            events.append(event)
            state = None

now = datetime.utcnow().replace(tzinfo=UTC)
events = filter(lambda e: e['start'] and e['start'] > now, events)
events = sorted(events, key=itemgetter('start'))
for e in events[:1]:
    print '%s (%s)' % (
        e['name'],
        e['start'].strftime('%d/%m/%Y %H:%M'),
    )
