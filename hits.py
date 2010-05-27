#!/usr/bin/env python

import urllib, sys, re, locale

locale.setlocale(locale.LC_ALL, '')

search = urllib.quote(' '.join(sys.argv[5:]))
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=' + search
page = urllib.urlopen(url).read()

match = re.search('"estimatedResultCount":"(.*?)"', page)
if match:
  count = int(match.group(1))
  print locale.format('%d', count, True)

