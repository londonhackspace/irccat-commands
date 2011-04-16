#!/bin/bash
set - $(curl -s 'http://london.hackspace.org.uk/webcam_stats.php'|sed 's/:/ /g')

while [ $1 ]; do
  echo -n "$2 on $1"
  shift
  shift
  [ $1 ] && echo -n ', '
done
echo

