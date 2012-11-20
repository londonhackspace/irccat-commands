#!/bin/bash
XML=$(wget -q -O- "http://api.bike-stats.co.uk/service/rest/bikestat/539?format=xml")
AVAIL=$(echo $XML | sed "s/.*<bikesAvailable>\(.*\)<\/bikesAvailable>.*/\1/")
FREE=$(echo $XML | sed "s/.*<emptySlots>\(.*\)<\/emptySlots>.*/\1/")
echo "Boris bikes available: ${AVAIL} Slots free: ${FREE}"
