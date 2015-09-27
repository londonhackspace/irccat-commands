#!/usr/bin/env python

import requests
from lxml import objectify, html
from datetime import datetime
import rfc822
import re

def chunker(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i + n]

def parse_urldate(url):
    matches = re.match(r'https?://dc4420.org/(\d{4}/\d{2}/\d{2})', url)
    if not matches:
        raise ValueError('Unexpected post URL')
    return datetime.strptime(matches.group(1), '%Y/%m/%d')

def parse_pubdate(pubdate):
    ts = rfc822.mktime_tz(rfc822.parsedate_tz(pubdate))
    return datetime.fromtimestamp(ts)

resp = requests.get('http://dc4420.org/feed.xml')
rss = objectify.fromstring(resp.content)
items = list(rss.channel.item)

talks = [i for i in items if 'talk' in list(i.category)]
pubdates = [parse_pubdate(t.pubDate.text) for t in talks]
startdates = [parse_pubdate(t.eventStart.text) for t in talks]

now = datetime.utcnow()
#now = datetime(2015, 7, 1)
future_talks = [t for d, t in sorted(zip(startdates, talks)) if d >= now]
if not future_talks:
    print "No talks yet. Email talks@dc4420.org if you'd like to give one."

else:
    first = future_talks[0]
    print "Talk summary for %s (more details at https://dc4420.org/):" % startdates[0].strftime("%a %d %B %Y")

    desc = html.fragment_fromstring(first.description.text, create_parent='div')
    sel = desc.cssselect('h2, h2+h3+p')
    for title, speaker in chunker(sel, 2):
        speaker, _, _ = speaker.text_content().partition(',')
        title = title.text_content()
        print ' * %s: %s' % (speaker, title)

