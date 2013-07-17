#!/bin/bash

file=/usr/share/irccat/.test.txt
equipment=Testings
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

