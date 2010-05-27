#!/usr/bin/env python

import urllib, sys

print 'http://maps.google.com/maps?q=' + urllib.quote(' '.join(sys.argv[5:]))
