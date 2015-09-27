#!/bin/bash

file=/usr/share/irccat/.trailermast.txt
equipment=Mast
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

