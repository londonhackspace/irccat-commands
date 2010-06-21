#!/bin/bash

file=/usr/share/irccat/.makerbot.txt

shift; shift; shift; shift

if [ "$1" == '' ]; then
  if [ "`cat $file`" != 'working' ]; then
    echo "Makerbot status: `cat $file`"
  else
    now=`date +%s`
    borked=`stat -c %Z $file`
    diff=`expr \( $now - $borked \) / 60 / 60 / 24`
  
    if [ "$diff" == '1' ]; then
      days=day
    else
      days=days
    fi
    echo It has been $diff $days since the last incident.
  fi
else
  echo $*>$file
fi
