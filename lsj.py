#!/usr/bin/env python

from urllib import urlencode
import urllib2
from lxml import etree
from lxml.cssselect import CSSSelector
import sys

BASE_URL='http://www.perseus.tufts.edu/hopper/'

def browse(url, params=None):
  if params is not None:
    params = urlencode(params)
  page = urllib2.urlopen(BASE_URL + url, params)
  return etree.HTML(page.read())

# etree doesn't see the Content-type header
def get_text(el, real_encoding='utf-8'):
  return etree.tostring(el, encoding='iso-8859-1', method='text').decode(real_encoding)

find_lemma = CSSSelector('.lemma_header')
find_greek = CSSSelector('.greek')
find_defn = CSSSelector('.lemma_definition')

params = dict(
  l = sys.argv[5],
  la = 'greek',
)

results = browse('morph', params)
lemma = find_lemma(results)
if lemma:
  greek = find_greek(lemma[0])
  defn = find_defn(lemma[0])
  print '%s: %s' % (
    get_text(greek[0]).strip().encode('utf-8'),
    get_text(defn[0]).strip().encode('utf-8'),
  )

