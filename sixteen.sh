#!/bin/bash
echo `date`: $* >> /usr/share/irccat/.notify.log
user=$1
shift;shift;shift;shift;
if [ ! -z "$1" ] ; then
	/usr/share/irccat/setSixteen.py hamming.lan.london.hackspace.org.uk "$user on IRC said: $*"
else
	/usr/share/irccat/setSixteen.py hamming.lan.london.hackspace.org.uk ""
fi
