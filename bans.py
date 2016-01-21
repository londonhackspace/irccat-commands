#!/usr/bin/env python
from lxml import html
import requests
import sys
import re

search = sys.argv[1]

url = "https://wiki.london.hackspace.org.uk/view/Grievance_Procedure/Bans_Issued"

result = requests.get(url)
result = html.fromstring(result.content)
headings = result.xpath("//table[1]/tr/th//text()")
entries = result.xpath("//tr/td//text()")

bans = {}
count = 1
for item in entries:
    if count == 1:
        currentKey = item
        bans[currentKey] = []

    else:
        bans[currentKey].append(item.rstrip('\n'))

    if count == len(headings):
        count = 1
    else:
        count += 1

name = [key for key, value in bans.items() if re.search(search, key, re.I)]

if name:
    name = name[0]
    print("%s was banned for %s due to %s. Expires: %s" % (name, bans[name][0], bans[name][3], bans[name][2]))
else:
    print("Couldn't find a ban for: %s" % search)
