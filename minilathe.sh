#!/bin/bash

file=/usr/share/irccat/.minilathe.txt
equipment=minilathe
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

