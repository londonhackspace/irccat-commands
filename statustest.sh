#!/bin/bash

file=/opt/irccat/irccat-data/test.txt
equipment=Testings
editor=$1

shift; shift; shift; shift

/opt/irccat/irccat-commands/.equipment.sh $file $equipment $editor $*

