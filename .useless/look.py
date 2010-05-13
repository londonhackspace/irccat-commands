#!/usr/bin/env python
from os import path
import random

tea = path.exists('/tmp/tea')

adjs = ['little', 'twisted', None, None]
random.shuffle(adjs)
phrase = adjs[0:2] + ['space of'] + adjs[2:4] + ['hackers']
phrase = ' '.join(filter(lambda p: p, phrase))

print 'You are in a %s, all different' % phrase

if tea:
  print 'There is a nice, hot cup of Advanced Tea Substitute here.'

