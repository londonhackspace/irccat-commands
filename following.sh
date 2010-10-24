#!/bin/bash

shift; shift; shift; shift

curl -s twitter.com/$1|grep 'id="follower_count"'|sed -e 's/^.*id="follower_count".*>\([^>]*\)<\/span>/\1/'
