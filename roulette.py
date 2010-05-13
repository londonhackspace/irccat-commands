#!/usr/bin/env python

import pickle
import random

file = open("/usr/share/irccat/pickle.pck", "r") # read mode
chamber = pickle.load(file)

#chamber = [1,0,0,0,0,0]
#print chamber

for i in 0,1,2,3,4,5:
    #print i
    if(chamber[i]==0):
        print '*CLICK*'
        chamber[i] = 2
        break
    elif(chamber[i]==1):
        print 'BANG! You are dead!'
        chosen = random.randint(0,5)
        print 'I will load a bullet in chamber', chosen, 'and spin the barrel'
        spin = random.randint(0,30)
        chosen = chosen + (spin - (6 * (spin // 6)))
        if (chosen>5):
            chosen = chosen - 6
        for i in (0,1,2,3,4,5):
            if(i==chosen):
                chamber[i] = 1
            else:
                chamber[i] = 0 
        #print 'now in', chosen
        break

file = open("/usr/share/irccat/pickle.pck", "w") # write mode
pickle.dump(chamber, file)
file.close()
