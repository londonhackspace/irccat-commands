#!/bin/bash

shift; shift; shift; shift

if [[ "$@" == '' ]]; then
    exit
fi

visited=$(curl -sL https://github.com/pubstandards/pubstandards-london/raw/master/ps_data.json|grep '"location"'|cut -d: -f2|cut -d\" -f2|grep -i "$*"|head -1)
if [[ "$visited" != '' ]]; then
    echo "We've visited $visited"
else
    echo "We haven't been anywhere like that yet"
fi

