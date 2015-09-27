#!/bin/bash

PUBDAY=`Thursday`
KNOCKOFF="1900"

echo $(($(date -d "$PUBDAY $KNOCKOFF" +%s%N) - $(date +%s%N))) nanoseconds until Naked Thursday begins.
