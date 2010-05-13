#!/bin/bash

echo -en "Flashing beacons!\r\n"

# TODO: check the last movement time and don't flash if the space has been empty an hour

for i in {1..5}
do
    curl http://localhost:8000/_/255,255,255?restoreAfter=1 &> /dev/null
    curl http://localhost:8000/_/0,0,0?restoreAfter=1 &> /dev/null
done

#echo -en "Beacon sequence complete.\r\n"
