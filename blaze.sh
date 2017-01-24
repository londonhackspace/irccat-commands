#!/bin/bash
PUBDAY=`date +%A`KNOCKOFF="1620"
echo $(($(date -d "$PUBDAY $KNOCKOFF" +%s%N) - $(date +%s%N))) nanoseconds until blaze o\'clock
