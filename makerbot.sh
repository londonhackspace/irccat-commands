#!/bin/bash

file=/usr/share/irccat/.makerbot.txt
equipment=Makerbot

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $*

