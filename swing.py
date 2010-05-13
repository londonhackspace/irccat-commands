#!/usr/bin/env python

import re, bbcvotes

swingpc, swingfrom, swingto  = ['unknown'] * 3

m = re.search(bbcvotes.swingre, bbcvotes.html)
if m:
  swing = m.group(1)
  m = re.search(bbcvotes.swingpcre, swing)
  if m:
    swingpc = '%s%%' % m.group(1)

  m = re.search(bbcvotes.swingfromre, swing)
  if m:
    swingfrom = m.group(1)
  try:
    swingfrom = bbcvotes.parties[swingfrom]
  except:
    pass

  m = re.search(bbcvotes.swingtore, swing)
  if m:
    swingto = m.group(1)
  try:
    swingto = bbcvotes.parties[swingto]
  except:
    pass

print '%s swing from %s to %s' % (swingpc, swingfrom, swingto)

