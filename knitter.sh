#!/bin/bash

file=/usr/share/irccat/.knitter.txt
equipment=Gnotter
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

