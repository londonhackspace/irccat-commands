#!/bin/bash

if [ "$5" != '' ]; then
  whois $5|grep -i 'phone\:\|+[0-9]\|\([0-9]\{3,\}\) \{3,\}'|head -1|sed 's/.*phone\:\s*//i'|sed 's/\(+[^+]*\)+/\1/'|sed 's/^ *\([^ ]*\) *$/\1/'
fi
