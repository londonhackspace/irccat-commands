#!/bin/sh

if [ $5 = "set" ];
then
        echo "setting word to $6"
        echo $6 > /usr/share/irccat/wordday.txt
else
    word=`cat /usr/share/irccat/wordday.txt`
    echo "Todays word is: $word"
fi
