#!/bin/bash
echo $(

set - $(curl -sk 'https://london.hackspace.org.uk/webcam_stats.php'|sed 's/:/ /g')
COUNT=`python -c 'import sys;import random;sys.stdout.write(str(random.randint(0,200)))'`

while [ $1 ]; do
  echo -n "$2 on $1"
  shift
  shift
  [ $1 ] && echo -n ', '
done
echo ", $COUNT on potatocam"
echo

)
