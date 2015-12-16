#!/bin/bash
val[0]="no more than usually"
val[1]="slightly"
val[2]="slightly more"
val[3]="a bit"
val[4]="quite a bit"
val[5]="more than averagely"
val[6]="quite"
val[7]="overly"
val[8]="stupidly"
val[9]="dangerously"
val[10]="proper"
val[11]="SO"
val[12]="MUCH"
val[13]="WOW VERY"
res=`curl --silent cloud.tfl.gov.uk/TrackerNet/LineStatus`
#ct=`echo $res | grep -o "Delays\|Suspended" | wc -l`
ct=`echo "$res" | grep '<LineStatus\ ' | grep -ic 'MINOR\|MAJOR\|SUSPENDED\|DELAY'`
echo "the tubes are" ${val[$ct]} "fucked"
