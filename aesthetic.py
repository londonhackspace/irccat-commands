#! /usr/bin/python

import sys

if len(sys.argv) > 5:
  string = ' '.join(sys.argv[5:])
else:
  string = 'aesthetic'

print ' '.join(string.upper())
