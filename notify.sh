#!/bin/bash
echo `date`: $* >> /usr/share/irccat/.notify.log
user=$1
# start padski
H=$(date +%H)
if (( 0 <= 10#$H && 10#$H < 6 )); then
    echo Board is disabled atm, stop it Stephan.
else
# end padski
shift;shift;shift;shift;
# Include user as anti-trolling measure (per trustees)
/usr/share/irccat/setBoard.py hamming.lan.london.hackspace.org.uk "<$user> $*" >/dev/null
/usr/share/irccat/setBoard.py wilson.lan.london.hackspace.org.uk "<$user> $*" >/dev/null
echo Displayed on boards
fi
