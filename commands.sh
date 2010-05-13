#!/bin/bash
if [ "$2" != '' ]; then
    echo "$1, I have pm'd you the list of available commands."
fi

COMMANDS=`ls -m /usr/share/irccat | sed -r -e 's/[a-z0-9]+\.(pyc|pck),\s+//g' | sed -r -e 's/\.[a-z0-9]+//g'`
echo -en "@$1 The available commands are:\n$COMMANDS" | nc -q0 localhost 12345

