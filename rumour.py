#!/usr/bin/python

import sys
import random

noun = 'they'

if len(sys.argv) > 5:
    noun = ' '.join(sys.argv[5:])

rumours = [
    "I heard {0} couldn't be trusted."
]

rumour = random.choice(rumours)
print rumour.format(noun)

sys.exit()
