#!/bin/bash

file=$1
equipment=$2
editor=$3
shift; shift; shift

if [ "$1" == '' ]; then
  if [ "`tail -1 $file`" != 'working' ]; then
    echo "$equipment status: `tail -1 $file`"
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
    echo $equipment working: it has been $diff $days since the last incident.
  fi
else
  # yeah I know this accumulates indefinitely. I think a little history 
  # is a good idea. When it gets too much, someone can fix it.
  echo "Changed at " $(date) " by " $editor >>$file
  echo $*>>$file
fi
