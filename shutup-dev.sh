#!/bin/bash

TIME=$5

if [[ ! $TIME ]]; then
    TIME=10
fi

if echo  "$TIME"  | egrep "[^0-9]" > /dev/null; then
    echo "NOT A NUMBER. (I AM A FREE MAN)"
    exit
fi

if [ $TIME -lt 0 ]; then
    echo "Nice try wise guy."
    exit
fi

if [ $TIME -gt 600 ]; then
    echo "I'm not sleeping beauty, try a shorter time."
    exit
fi

echo "Shutting up for $TIME seconds..."
sleep $TIME
