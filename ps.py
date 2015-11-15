#!/opt/irccat/irccat-commands/ps-venv/bin/python

import sys
from subprocess import Popen, PIPE
from icalendar import Calendar
from datetime import datetime

stdout, stderr = Popen(['php', '/opt/irccat/irccat-commands/calendar.php'], stdout=PIPE, stderr=PIPE).communicate()

cal = Calendar.from_ical(stdout)

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

            if offset.days == 0 and datetime.now().day != start.day:
                datestr = 'TOMORROW!'

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
