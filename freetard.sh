#!/bin/bash

if [ "$2" != 'null' ]; then
    echo "$1, I have pm'd you a list of free services."
fi

STATUSES="free shell account - https://blinkenshell.org/wiki/Start\n
bloody cheap vps (19USD/year) - http://alienvps.com/vps-hosting/\n
your mum (blame aden)\n"

echo -en "@$1 $STATUSES" | nc -q0 localhost 12345


