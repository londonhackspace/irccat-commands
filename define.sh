#!/bin/bash

_1=$1
_2=$2
_3=$3
_4=$4
shift; shift; shift; shift
/opt/irccat/irccat-commands/wolfram.py "$_1" "$_2" "$_3" "$_4" "define $@"
