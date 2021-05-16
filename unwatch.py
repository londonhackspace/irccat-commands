#!/usr/bin/env python

import sys
import pickle

itemid = sys.argv[5]

picklefile = '/usr/share/irccat/.watches.pck'

def get_watches():
  f = open(picklefile, 'rb')
  watches = pickle.load(f)
  f.close()
  return watches

def save_watches(watches):
  f = open(picklefile, 'wb')
  pickle.dump(watches, f)
  f.close()

if itemid is None:
  sys.exit()

try:
  watches = get_watches()
except:
  watches = {}

if itemid not in watches:
  print ('Item not being watched')
  sys.exit()

del watches[itemid]

save_watches(watches)
