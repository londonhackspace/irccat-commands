#!/bin/bash

if [ "$5" != '' ]; then
  whois $5|grep 'phone\:\|+[0-9]\|\([0-9]\{3,\}\) \{3,\}'|head -1|sed 's/phone\:\s*//'|sed 's/\(+[^+]*\)+/\1/'|sed 's/^ *\([^ ]*\) *$/\1/'
else
  echo 020 7613 5391
fi
