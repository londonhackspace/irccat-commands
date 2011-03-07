#!/usr/bin/env python

import sys
import pickle

itemid = sys.argv[5]
name = ' '.join(sys.argv[6:])

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

if itemid is None or name is None:
  sys.exit()

try:
  watches = get_watches()
except:
  watches = {}

if itemid in watches:
  print 'Item already being watched'
  sys.exit()

watches[itemid] = { 'name': name }

save_watches(watches)
