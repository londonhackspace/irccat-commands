#!/bin/bash
shift; shift; shift; shift
DISPLAY=:0 phantomjs /usr/share/irccat/summon.js $*
