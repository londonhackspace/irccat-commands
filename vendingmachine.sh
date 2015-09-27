#!/bin/bash

file=/usr/share/irccat/.vendingmachine.txt
equipment=Vendingmachine
editor=$1

shift; shift; shift; shift

/usr/share/irccat/.equipment.sh $file $equipment $editor $*

