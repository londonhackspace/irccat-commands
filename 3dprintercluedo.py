#!/usr/bin/python
import random

names = ['hipster', 'ian', 'zippo', 'dean', 'billy', 'glen']
reasons = ['screwdriver', 'calibration', 'hammer', 'PLA', 'liquid nitrogen', 'length of wood', 'soldering iron', 'club mate bottle']
locations = ['quiet room', 'workshop', 'classroom', 'main room', 'carpark', 'foyer']

print "it was %s in the %s with the %s" % (random.choice(names), random.choice(locations), random.choice(reasons))
