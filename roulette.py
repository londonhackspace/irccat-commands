#!/usr/bin/env python

import collections
import pickle
import random

class Gun:
    def __init__(self, chamber_size=6):
        self._chamber_size = chamber_size
        self._chamber = collections.deque([0] * self._chamber_size)
        
    def load(self, index=1):
        self._chamber[index] = 1

    def spin_chamber(self, spin=None):
        if not spin:
            spin = random.randint(0, self._chamber_size - 1)
        self._chamber.rotate(spin)

    def pull_trigger(self):
        if self._chamber[0] == 0:
            print ('*CLICK*')
            self.spin_chamber(1)
        else:
            print ("*BANG* You're dead!")
            
            print ("Reloading and spinning the chamber")
            self.spin_chamber()


def load(path):
    try:
        with open(path, "r") as f:
            return pickle.load(f)
    except:
        return None

def save(path, data):
    with open(path, "w") as f:
        pickle.dump(data, f)



path = "/usr/share/irccat/roulette_pickle.pck"

gun = load(path)
if not gun:
    gun = Gun()
    gun.load()
    gun.spin_chamber()
    print ('Loading the gun and spinning the chamber')

gun.pull_trigger()

save(path, gun)
