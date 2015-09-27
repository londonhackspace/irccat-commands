#!/bin/bash

file=/opt/irccat/irccat-data/stratasys.txt
equipment=Stratasys
editor=$1

shift; shift; shift; shift

/opt/irccat/irccat-commands/.equipment.sh $file $equipment $editor $*

