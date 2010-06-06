#!/bin/bash

echo -en "Flashing beacons!\r\n"

/usr/share/irccat/setBoard.py "Beacon: $1" &> /dev/null

for i in {1..5}
do
    curl http://localhost:8000/_/255,255,255?restoreAfter=1 &> /dev/null
    curl http://localhost:8000/_/0,0,0?restoreAfter=1 &> /dev/null
done

/usr/share/irccat/setBoard.py "" &> /dev/null
