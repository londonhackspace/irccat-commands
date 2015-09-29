#!/bin/bash

#PUBDAY="friday"
PUBDAY=`date +%A`
KNOCKOFF="1730"

echo $(($(date -d "$PUBDAY $KNOCKOFF" +%s%N) - $(date +%s%N))) nanoseconds until pub o\'clock
