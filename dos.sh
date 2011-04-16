#!/bin/bash

cd /usr/local/bin/Scripts
./beconns.pl|grep RESP | cut -c14-28|sort|uniq -c|sort -n |tail -1|tr -s ' '
