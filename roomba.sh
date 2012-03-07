#!/bin/bash

# print a random string, using 'fortune'
# note : 
# if you clone this for another subject, create a directory with the subject's name
# and place files in it in /usr/games/fortune format : a file containing strings with
# a % char separating them, and a .dat file continaing an index.
# If you add entries or create a new string file, update the .dat with
#  strfile <infile> <infile>.dat

subject=roomba
dir=/usr/share/irccat/$subject

/usr/games/fortune $dir

