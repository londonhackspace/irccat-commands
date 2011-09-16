#!/bin/bash

COUNT=$(curl -sk https://london.hackspace.org.uk/member_stats.php|cut -d' ' -f1|cut -d: -f2)
echo "London Hackspace currently has $COUNT paying members."
