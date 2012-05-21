#!/bin/bash
URL=$5
if [ "$URL" == '' ]; then
    echo "Please pass a URL"
    exit
fi
curl -s http://tinyurl.com/create.php?url=${URL} | grep "Open in the" | awk -F"http://tinyurl.com/" '{print "http://tinyurl.com/" $2}'|sed 's/Open.*$//'
