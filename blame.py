#!/usr/bin/env python

from random import choice
from sys import argv

if __name__ == '__main__':
    if len(argv) > 5:
        thing2blame = ' '.join(argv[5:])
        print ("DAMMIT, {0}!".format(thing2blame))
    else:
        people2blame = ['nobody\'s fault, shit happens', 'fabio', 'tomwyatt', 'detonate', 'jontyw', 'tgreer', 'hipster', 'oni', 'zippo', 'chixor', 'ME! MWAHAHAH', 'the Computer. Do you secretly hate the Computer, citizen?']
        person = choice(people2blame)
        print ("It was {0}".format(person))
