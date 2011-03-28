#!/usr/bin/env python

import urllib
import htmllib
import formatter
import sys
import json
import re

def getjson(base, args):
  
  url = base + urllib.urlencode(args)
  f = urllib.urlopen(url)
  d = json.loads(f.read())
  return d

def unescapehtml(s):
  f = formatter.NullFormatter()
  p = htmllib.HTMLParser(f)
  p.save_bgn()
  p.feed(tidy(s))
  return p.save_end()

def tidy(output):
  return re.sub('<br/?>', '\n', re.sub('\r', '', output))



if len(sys.argv) < 6 or sys.argv[5] is None:
  print 'verb: to state the meaning of'
  sys.exit()

term = ' '.join(sys.argv[5:])
if term == 'trolling':
  print 'Muz'
  sys.exit()
elif term == 'define':
  print '++Error out of cheese please redo from start++'
  sys.exit()
args = {'term': term}

define = getjson('http://www.urbandictionary.com/iphone/search/define?', args)
#related = getjson('http://www.urbandictionary.com/iphone/search/related?', args)

try:
  sense = define['list'][0]

  defn = sense['definition']
  ex = sense['example']
except KeyError:
  sys.exit()


firstline = unescapehtml(defn).splitlines()[0]
if len(firstline) > 200:
  firstline = firstline[0:200] + '...'
print "%s: %s" % (term, firstline)
#print tidy(ex)




