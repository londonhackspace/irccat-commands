#!/bin/bash

file=/usr/share/irccat/.clubmate.txt
equipment='Club Mate'
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh "$file" "$equipment" "$editor" $*

