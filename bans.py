#!/usr/bin/env python
from lxml import html
import requests
import sys
import time

search = ' '.join(sys.argv[5:]).strip()
if not search:
    sys.exit(1)

url = "https://wiki.london.hackspace.org.uk/view/Grievance_Procedure/Bans_Issued"

result = requests.get(url)
result = html.fromstring(result.content)
headings = result.xpath("//table[1]/tr/th//text()")
entries = result.xpath("//tr/td//text()")

bans = {}
count = 1
for item in entries:
    if count == 1 and item.strip() not in bans:  # Ignore any subsequent (old) bans
        currentKey = item.strip()
        bans[currentKey] = []
    else:
        bans[currentKey].append(item.strip())
    if count == len(headings):
        count = 1
    else:
        count += 1

name = [key for key, value in bans.items() if search.lower() in key.lower()]
if name:
    name = name[0]
    now = time.time()
    expires = int(time.mktime(time.strptime(bans[name][2], '%Y/%m/%d')))

    if expires > now:
        print("%s is banned for %s due to %s. Expires: %s" % (name, bans[name][0], bans[name][3], bans[name][2]))
    else:
        print("%s was banned for %s due to %s. Expired: %s" % (name, bans[name][0], bans[name][3], bans[name][2]))

else:
    print("Couldn't find a ban for: %s" % search)
