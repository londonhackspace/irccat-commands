#!/bin/bash
PEOPLE=`/var/www/cacti/scripts/lhs_spacensus.sh | grep -E -o '[0-9]+'`
echo "Approximately $PEOPLE people are in the space.  (Graphs: http://bit.ly/g5bxbQ)"
