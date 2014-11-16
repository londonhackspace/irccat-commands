#!/bin/bash
echo `date`: $* >> /usr/share/irccat/.notify.log
user=$1
shift;shift;shift;shift;
/usr/share/irccat/setBoard.py hamming.lan.london.hackspace.org.uk "$user on IRC said : $*" >/dev/null
/usr/share/irccat/setBoard.py wilson.lan.london.hackspace.org.uk "$user on IRC said : $*" >/dev/null
echo Displayed on boards
