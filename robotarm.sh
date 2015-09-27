#!/bin/bash


equipment=robotarm
file=/opt/irccat/irccat-data/robotarm.txt
editor=$1

shift; shift; shift; shift

/opt/irccat/irccat-commands/.equipment.sh $file $equipment $editor $*

