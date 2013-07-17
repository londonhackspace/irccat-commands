#!/bin/bash

file=/usr/share/irccat/.acnode.txt
equipment=ACNode
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

