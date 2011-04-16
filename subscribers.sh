#!/bin/bash

curl -s http://london.hackspace.org.uk/member_stats.php|cut -d' ' -f1|cut -d: -f2
