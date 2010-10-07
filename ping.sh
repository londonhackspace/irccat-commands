#!/bin/bash

shift; shift; shift; shift

if [ $# != 1 ]; then
  echo Pong!
  exit
fi

ping -c1 $1 2>/dev/null 1>/dev/null
if [ "$?" == '0' ]; then
  echo $1 is alive
else
  echo $1 is not alive
fi
