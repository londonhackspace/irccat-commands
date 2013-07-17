#!/bin/bash

file=/usr/share/irccat/.robotarm.txt
equipment=robotarm
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

