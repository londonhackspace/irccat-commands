#!/bin/bash

if [ "$5" != '' ]; then
  whois $5|grep 'phone\:\|+[0-9]'|head -1|sed 's/phone\:\s*//'|sed 's/\(+[^+]*\)+/\1/'|sed 's/^ *\([^ ]*\) *$/\1/'
fi
