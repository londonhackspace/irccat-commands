#!/usr/bin/env python

from random import choice

if __name__ == '__main__':
    outcomes = ['NO CARRIER', 'CONNECT 9600', 'CONNECT 28800', '+++ATH0', '%^S)!@%   j\\\\']
    print "{0}".format(choice(outcomes))
