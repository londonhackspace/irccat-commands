#!/bin/bash
NAME=$5
if [ "$NAME" == '' ]; then
    NAME=$1;
fi

echo "Hey $NAME, http://hack.rs/stfu.jpg"
