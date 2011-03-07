#!/bin/bash

PEOPLE=`/var/www/cacti/scripts/lhs_spacensus.sh | grep -E -o '[0-9]+'`
if [ "$PEOPLE" != '' ]; then
  echo "Approximately $PEOPLE people are in the space."
fi
