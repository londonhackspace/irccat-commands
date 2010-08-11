#!/bin/bash

file=/usr/share/irccat/.kegerator

shift; shift; shift; shift

if [ "$1" == '' ]; then
  echo "Kegerator status: `cat $file`"
else
  echo $*>$file
fi
