#!/bin/bash

file=/usr/share/irccat/.dishwasher.txt
equipment=dishwasher
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

