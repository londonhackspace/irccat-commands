#!/bin/bash

file=/usr/share/irccat/.printer.txt
equipment=Printer

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $*

