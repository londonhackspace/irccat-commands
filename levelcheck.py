#!/usr/bin/python

import yaml
import sys

f = open("/opt/irccat/irccat-commands/elite.yaml", 'r')
levels = yaml.load(f)
f.close

# print levels

if len(sys.argv) > 5:
  searchfor = sys.argv[5]
else:
  searchfor = sys.argv[1]

memberlevel = '(slightly spheric) Cubic Zirconia'

for l, v in levels.iteritems():
  if searchfor.lower() in [x.lower() for x in v['members']]:
    memberlevel = v['name']

print searchfor + ": " + memberlevel + " membership"
