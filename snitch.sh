#!/bin/bash

MSG_COUNT=5

cd /usr/share/irccat
tail -n $MSG_COUNT .notify.log \
| sed "s/^/@$1 /" \
| nc -q0 localhost 12345

echo $1, I have PM\'d the last $MSG_COUNT board messages to you
