#!/bin/bash

STATS=$(curl -sk https://london.hackspace.org.uk/member_stats.php)
COUNT=$(echo $STATS|cut -d' ' -f1|cut -d: -f2)
TIMESTAMP=$(echo $STATS|cut -d' ' -f3|cut -d: -f2)
LAST_TXN=$(date -d@$TIMESTAMP '+%e %B')
echo "London Hackspace has $COUNT paying members (last payment $LAST_TXN). See some at https://london.hackspace.org.uk/members/"
