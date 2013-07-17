#!/bin/bash

file=/usr/share/irccat/.lift.txt
equipment=lift
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

