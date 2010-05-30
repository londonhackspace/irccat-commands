#!/usr/bin/env python

import re, bbcvotes

results = {}
for pcode, pname in bbcvotes.parties.items():
  result = re.search(bbcvotes.resultre % pcode, bbcvotes.html)
  reswon = 'unknown'
  if result:
    won = re.search(bbcvotes.wonre, result.group(1))
    if won:
      reswon = won.group(1)

  results[pname] = reswon

progress = []
m = re.search(bbcvotes.progressre, bbcvotes.html)
if m:
  progress = int(m.group(1))
  progress = ['With %s seats remaining,' % (650 - progress)]

results = ['%s: %s' % (pname, result) for pname, result in results.items()]
print ' '.join(progress + results)

