#!/bin/bash

basedir=/opt/irccat/irccat-data
equipment=$1
editor=$2
file="$basedir/$equipment.status"
shift; shift; shift; shift; shift


if [ "$1" == '' ]; then
  if [ "`tail -1 "$file"`" != 'working' ]; then
    echo "$equipment status: `tail -1 "$file"` (`tail -2 "$file" | head -1 | sed -e 's/  / /g' -e 's/Changed at //g'`)"
  else
    now=`date +%s`
    borked=`stat -c %Y "$file"`
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
  echo "Changed at " $(date) " by " $editor >>"$file"
  echo "$@">>"$file"
fi
