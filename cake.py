#!/usr/bin/env python
import sys
import codecs
import random
import requests

from lxml import html

sys.stdout = codecs.getwriter('utf8')(sys.stdout)

response = requests.get('http://en.wikipedia.org/wiki/List_of_cakes')
root = html.document_fromstring(response.content)

# Some things are inexplicably in italics
elements = root.xpath('//tr/td[1]/a|//tr/td[1]/i/a')

thing = random.choice(elements)
print "WHY DON'T YOU EAT A %s: http://en.wikipedia.org%s" % (thing.text.strip().upper(), thing.attrib['href'])
