#!/bin/bash
# count the active connections to the webcams

streams()
{
  echo -n $1
  echo -n " stream"
  if [ $1 != 1 ] ; then echo -n s ; fi
  echo -n " $2"
}


set $(host $(hostname))
streams $(netstat -n | grep ${4}:8001 | wc -l) "on main webcam, " 
streams $(netstat -n | grep ${4}:8002 | wc -l) "on robot webcam." 
echo


