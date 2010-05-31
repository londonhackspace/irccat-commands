#!/bin/bash

if [ "$5" != '' ]; then
  whois $5|grep phone\:|head -1|sed 's/phone\:\s*//'
fi
