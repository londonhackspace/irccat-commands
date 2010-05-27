#!/bin/bash

file=/usr/share/irccat/makerbot.txt

if [ "`cat $file`" == 'broken' ]; then
  diff=0
else
  now=`date +%s`
  borked=`stat -c %Z $file`
  #echo $now/$borked
  diff=`expr \( $now - $borked \) / 60 / 60 / 24`
fi

if [ "$diff" == '1' ]; then
  days=day
else
  days=days
fi
echo It has been $diff $days since the last incident.
