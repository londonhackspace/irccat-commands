#!/usr/bin/env python2.7

import datetime
import random
import sys
import pickle

save_file = "/opt/irccat/irccat-data/noisebridgelevel.pickle"
random_min = 1000
random_max = 5000
halflife = 60 * 60 * 24 * 7

now = datetime.datetime.now()

try:
    with open(save_file, "r") as f:
        value, timestamp = pickle.load(f)
except IOError:
    value, timestamp = 0, now

diff = (now - timestamp).total_seconds()

new_value = int(value * 0.5 ** (diff / halflife) + random.randint(random_min,random_max))

with open(save_file, "w") as f:
    pickle.dump((new_value, now), f)

msg = 'The Hackspace is currently measuring {0} nanonoisebridges and rising.'.format(new_value)
print(msg)
