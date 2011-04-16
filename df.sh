#!/bin/bash

df -h|grep '^/dev/md0[[:blank:]]'|sed 's/ \+/\t/g'|cut -f4
