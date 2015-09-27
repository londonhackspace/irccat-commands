#!/usr/bin/env python

from random import choice

if __name__ == '__main__':
    rages = ['Nothing', 'Sleepers', 'The Stratasys', 'The vending machine', 'The Silent Majority', 'The smell', 'The state of the toilet']
    target = choice(rages)
    print "Today's topic of rage: {0}".format(target)
