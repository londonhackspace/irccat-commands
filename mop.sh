#!/bin/bash

file=/usr/share/irccat/.mop.txt
equipment=Mop
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

