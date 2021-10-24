#!/bin/bash
echo `date`: $* >> /usr/share/irccat/.notify.log
user=$1
shift;shift;shift;shift;
# Include user as anti-trolling measure (per trustees)
/usr/share/irccat/setBoard.py holonyak.lan.london.hackspace.org.uk "<$user> $*" >/dev/null
/usr/share/irccat/setBoard.py wilson.lan.london.hackspace.org.uk "<$user> $*" >/dev/null
echo Displayed on boards
fi
