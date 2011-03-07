#!/bin/bash
a=`/usr/share/irccat/hits.py $1 $2 $3 $4 $5`
b=`/usr/share/irccat/hits.py $1 $2 $3 $4 $6`
if [ "$a" != '' -a "$b" != '' ]; then
  echo $a vs. $b
fi
