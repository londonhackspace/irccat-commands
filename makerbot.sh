#!/bin/bash

file=/usr/share/irccat/.makerbot.txt
equipment=Makerbot
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

