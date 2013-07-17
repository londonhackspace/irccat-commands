#!/bin/bash

file=/usr/share/irccat/.donkey.txt
equipment=Donkey_Saw
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

