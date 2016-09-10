#! /usr/bin/python

import re
import sys
import random

try:
    n,d = re.match(r'(\d*)d(\d+)', sys.argv[5]).groups()
    if n == '':
        n = '1'
    n,d = map(int, (n,d))
except (ValueError,AttributeError, IndexError):
    n,d = 1,6

if n > 100:
    print "%d! Why can't I hold all these dice?" % n
else:
    print "Rolling %dd%d: %d" % (n,d,sum(random.randint(1,d) for i in xrange(n)))
