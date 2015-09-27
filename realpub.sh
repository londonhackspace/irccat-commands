#!/bin/bash

#PUBDAY="friday"
PUBDAY=`date +%A`
KNOCKOFF="1800"

echo $(($(date -d "$PUBDAY $KNOCKOFF" +%s%N) - $(date +%s%N))) nanoseconds until real pub o\'clock
