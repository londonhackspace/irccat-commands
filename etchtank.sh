#!/bin/bash

file=/usr/share/irccat/.etchtank.txt
equipment=etchtank
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

