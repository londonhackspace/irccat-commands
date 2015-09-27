#!/bin/bash
cd `dirname $0`
shift; shift; shift; shift
/usr/local/bin/phantomjs summon.js $*
