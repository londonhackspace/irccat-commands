#!/usr/bin/python

import sys
import requests
from icalendar import Calendar
from datetime import datetime

try:
    response = requests.get('http://london.pubstandards.com/next.ics', timeout=2)
except requests.exceptions.Timeout:
    print "Oh no %s, I can't see the pubstandards website! Is it down? Somebody shout at cackhanded for me." % sys.argv[1]
    sys.exit(0)

cal = Calendar.from_ical(response.content)

for component in cal.walk():
    if component.name == "VEVENT":

        name = component.get('summary')
        start = component.get('dtstart').dt
        end = component.get('dtend').dt

        if start > datetime.now():

            offset = start - datetime.now()
            hours = int(offset.seconds / 3600)
            minutes = int(offset.seconds / 60)

            timestr = []
            datestr = 'TODAY!'

            if offset.days > 0:
                daystr = '%s day' % offset.days
                
                if offset.days > 1:
                    daystr += 's'
                timestr.append(daystr)

                if 4 <= start.day <= 20 or 24 <= start.day <= 30:
                    suffix = "th"
                else:
                    suffix = ["st", "nd", "rd"][start.day % 10 - 1]

                datestr = 'on ' + start.strftime('%B %d') + suffix + '.'

            if hours > 0:
                hourstr = '%s hour' % hours
                
                if hours > 1:
                    hourstr += 's'
                timestr.append(hourstr)

            if offset.days == 0 and hours < 6:
                minutestr = '%s minute' % (minutes % 60)

                if minutes != 1:
                    minutestr += 's'
                timestr.append(minutestr)

            print "The next pub standards is %s Only %s until beer!" % (
                datestr,
                ', '.join(timestr),
            )
            break

        elif datetime.now() > start and end > datetime.now():
            print "PUB STANDARDS IS ON RIGHT NOW, WHY ARE YOU NOT IN THE PUB?!"
            break
