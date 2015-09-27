#!/usr/bin/python

from datetime import datetime, timedelta

start = datetime.now().replace(month=12, day=25, hour=0, minute=0, second=0, microsecond=0)
if start + timedelta(days=1) < datetime.now():
    start = start.replace(year=start.year + 1)
end = start + timedelta(days=1)

offset = start - datetime.now()
hours = int(offset.seconds / 3600)
minutes = int(offset.seconds / 60)

timestr = []
datestr = 'TODAY!'

if start <= datetime.now() <= end:
    print "CHRISTMAS IS RIGHT NOW, WHY ARE YOU NOT OPENING PRESENTS?!"

else:

    if offset.days > 0:
        daystr = '%s day' % offset.days
        
        if offset.days > 1:
            daystr += 's'
        timestr.append(daystr)

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

    print "Christmas is %s Only %s until presents!" % (
        datestr,
        ', '.join(timestr),
    )

