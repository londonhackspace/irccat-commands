#!/bin/bash

DAY=`date +%F`
KNOCKOFF="2158"

echo $(($(date -d "$DAY $KNOCKOFF" +%s%N) - $(date +%s%N))) nanoseconds til blast off.
