#!/bin/bash

file=/usr/share/irccat/.stratasys.txt
equipment=Stratasys
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

