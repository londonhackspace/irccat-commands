#!/bin/bash

file=/usr/share/irccat/.layzor.txt

shift; shift; shift; shift

if [ "$1" == '' ]; then
  if [ "`cat $file`" != 'working' ]; then
    #echo "http://wiki.hackspace.org.uk/wiki/Equipment/LaserCutter"
    echo "Layzor status: `cat $file`"
  else
    now=`date +%s`
    borked=`stat -c %Y $file`
    # Round up
    diff=`expr \( $now - $borked + 86399 \) / 60 / 60 / 24`
  
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
