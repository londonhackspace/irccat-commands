#!/usr/bin/env python

import urllib
url = 'http://news.bbc.co.uk/1/shared/election2010/results/default.stm'
f = urllib.urlopen(url)
html = f.read().replace('\n', ' ')

progressre  = '<span class="results-declared">(.*?)</span>'
resultre    = '<tr class=\"party-%s\">(.*?)</tr>'
wonre       = '<td class="seats-won"><strong>(\d+)</strong></td>'
swingre     = '<div id="swing-o-meter">.*?<p>(.*?)</p>'
swingpcre   = '<strong>(.*?)&#37;</strong>'
swingfromre = '<span class="from".*?>(.*?)</span>'
swingtore   = '<span class="to".*?>(.*?)</span>'

parties = {
  'LAB': 'Labour',
  'CON': 'Tory',
  'LD':  'Lib Dem',
}

