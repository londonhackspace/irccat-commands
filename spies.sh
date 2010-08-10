#!/bin/bash
# count the active connections to the webcams

summary=""

streams()
{
  summary="${summary} $1 stream"
  if [ $1 != 1 ] ; then summary="${summary}s" ; fi
  summary="${summary} $2"
}


set $(host $(hostname))
streams $(netstat -n | grep ${4}:8001 | grep -c ESTABLISH ) "on main webcam," 
streams $(netstat -n | grep ${4}:8002 | grep -c ESTABLISH ) "on robot webcam.\n" 

echo -en $summary


