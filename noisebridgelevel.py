#!/usr/bin/env python2.7

import datetime
import random
import sys
import pickle

save_file = "/opt/irccat/irccat-data/noisebridgelevel.dat"
min = 1000
max = 5000

def load(path):
    try:
        with open(path, "r") as f:
            return pickle.load(f)
    except:
        return None

def save(path, data):
    with open(path, "w") as f:
        pickle.dump(data, f)


timestamp = load(save_file)
now = datetime.datetime.now()

save(save_file, now)

if not timestamp:
    num = random.randint(min, max)
else:
    diff = (now - timestamp).total_seconds()
    num = int(3600 * 100 / float(diff))

msg = 'The Hackspace is currently measuring {0} nanonoisebridges and rising.'.format(num)
print(msg)
