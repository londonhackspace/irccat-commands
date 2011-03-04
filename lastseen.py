#!/usr/bin/env python
import sys, os, pickle

PICKLEFILE = '/usr/share/irccat/.lastseen.pickle'

try:
    name = sys.argv[5]

except:
    print "You must specify a name to look up"
    sys.exit(0)

lastseen = {}
if os.path.exists(PICKLEFILE):
    lastseen = pickle.load(open(PICKLEFILE))

try:
    print "%s last opened the hackspace door on %s" % (name, lastseen[name.lower()])

except:
    print "%s has not opened the door since I started logging." % name
