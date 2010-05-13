#!/usr/bin/env python
import sys, subprocess

dirn = sys.argv[5].lower()

dirns = [
  'left', 'right',
  'north', 'south', 'east', 'west',
  'aft', 'fore', 'starboard', 'port',
]

if dirn == 'west':
  print 'In the open air'
elif dirn in dirns:
  look = '/usr/share/irccat/look.sh'
  p = subprocess.Popen(look, stdout=subprocess.PIPE)
  print p.communicate()[0]
