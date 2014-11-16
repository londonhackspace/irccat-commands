#!/bin/bash
echo `date`: $* >> /usr/share/irccat/.notify.log
user=$1
shift;shift;shift;shift;
/usr/share/irccat/setSixteen.py hamming.lan.london.hackspace.org.uk "$user on IRC said: $*"
