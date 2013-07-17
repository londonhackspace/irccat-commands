#!/bin/bash

file=/usr/share/irccat/.447.txt
equipment=447
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

