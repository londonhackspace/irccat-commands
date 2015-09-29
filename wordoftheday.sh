#!/bin/sh

shift; shift; shift; shift

if [ "$1" != '' ];
then
        echo "setting word to $1"
        echo $1 > /usr/share/irccat/.wordoftheday.txt
else
    word=`cat /usr/share/irccat/.wordoftheday.txt`
    echo "Todays word is: $word"
fi
