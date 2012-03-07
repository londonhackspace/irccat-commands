#!/bin/bash

if [ "$2" != 'null' ]; then
    echo "$1, I have pm'd you the status of ALL the machines."
fi

STATUSES=`
/usr/share/irccat/layzor.sh
/usr/share/irccat/3in1.sh
/usr/share/irccat/makerbot.sh
/usr/share/irccat/stratasys.sh
/usr/share/irccat/printer.sh
/usr/share/irccat/knitter.sh
/usr/share/irccat/mop.sh
/usr/share/irccat/dishwasher.sh
/usr/share/irccat/roomba.sh
`

echo -en "@$1 $STATUSES" | nc -q0 localhost 12345


