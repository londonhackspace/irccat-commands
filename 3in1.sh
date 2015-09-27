#!/bin/bash

file=/opt/irccat/irccat-data/3in1.txt
equipment=3in1
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

