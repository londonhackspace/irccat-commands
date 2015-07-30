#!/usr/bin/env python

import requests
import re
import sys
from htmllaundry import strip_markup

DEBUG=False

if sys.argv[1:] == ['-d']:
    DEBUG = True

response = requests.get('http://dc4420.org')

matches = re.search('<blockquote>(.*?)</blockquote>', response.content, re.DOTALL | re.IGNORECASE)

SEARCHING = 0
FOUND_SPEAKER = 1
FOUND_TITLE = 2

states = ['SEARCHING', 'FOUND_SPEAKER', 'FOUND_TITLE']

state = SEARCHING
speaker = None
title = None

print "Talk summary for the next DC4420: (Full synopses available at http://dc4420.org)"

for line in matches.group(1).splitlines():
    line = line.strip()
    if not line:
        continue
    if DEBUG:
        print states[state], line

    if state == FOUND_SPEAKER:
        speaker = line.strip()
        state = SEARCHING
        continue

    if 'Speaker' in line or 'speaker' in line:
        state = FOUND_SPEAKER
        continue

    if state == FOUND_TITLE:
        title = line.strip()
        state = SEARCHING
        continue

    if 'Title' in line or 'Talk Subject' in line:
        state = FOUND_TITLE
        continue

    if speaker and title:
        print ' * ', strip_markup(speaker), ': ', strip_markup(title)

        speaker = None
        title = None

