#!/bin/bash

COLOUR=$5

if [[ ! $COLOUR ]]; then
    COLOUR='ffffff'
fi

curl -s http://localhost:8000/_/$COLOUR -o /dev/null && echo "Lights are now $COLOUR"
