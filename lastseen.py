#!/usr/bin/env python
import sys, os, pickle, datetime, difflib

def dayordinal(day):
  if 4 <= day <= 20 or 24 <= day <= 30:
    suffix = 'th'
  else:
    suffix = ['st', 'nd', 'rd'][day % 10 - 1]
  return '%d%s' % (day, suffix)

def untilmsg(until):
    hours, seconds = divmod(until.seconds, 3600)
    days = until.days
    d_s = '' if days == 1 else 's'
    h_s = '' if hours == 1 else 's'
    if hours == 0:
        return '%s day%s' % (days, d_s)
    elif days == 0:
        return '%s hour%s' % (hours, h_s)
    else:
        return '%s day%s, %s hour%s' % (days, d_s, hours, h_s)


PICKLEFILE = '/usr/share/irccat/.lastseen.pickle'

name = ''.join(sys.argv[5:])

if not name:
    print "You must specify a name to look up"
    sys.exit(0)

lastseen = {}
if os.path.exists(PICKLEFILE):
    lastseen = pickle.load(open(PICKLEFILE))


try:
    d = lastseen[name.lower()]

except KeyError:

    matches = difflib.get_close_matches(name.lower(), lastseen.keys(), 1)

    if matches:
        print "I have never seen someone called %s open the door. Did you mean %s?" % (name, matches[0])
    else:
        print "%s has not opened the door since I started logging." % name

else:
    print "%s last opened the hackspace door on %s %s %s (%s ago)" % (
        name,
        d.strftime('%A'),
        dayordinal(d.day),
        d.strftime('%B %Y %H:%M'),
        untilmsg(datetime.datetime.now() - d),
    )
