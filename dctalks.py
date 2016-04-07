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

def get_future_events():

    resp = requests.get('http://dc4420.org/feed.xml')
    rss = objectify.fromstring(resp.content)
    items = list(rss.channel.item)

    events = [i for i in items if 'talk' in list(i.category)]
    pubdates = [parse_pubdate(t.pubDate.text) for t in events]
    startdates = [parse_pubdate(t.eventStart.text) for t in events]

    now = datetime.utcnow()
    #now = datetime(2015, 7, 1)
    future_events = [(d, t) for d, t in sorted(zip(startdates, events)) if d >= now]

    return future_events

def talk_getter(event):
    desc = html.fragment_fromstring(event.description.text, create_parent='div')
    sel = desc.cssselect('h2, h2+h3+p')
    for title, speaker in chunker(sel, 2):
        speaker, _, _ = speaker.text_content().partition(',')
        title = title.text_content()
        # ??? is often used as a placeholder
        if title != "???":
            yield speaker, title


if __name__ == '__main__':
    events = get_future_events()

    if not events:
        print "No talks yet. Email talks@dc4420.org if you'd like to give one."

    else:
        start, event = events[0]
        print "Talk summary for %s (more details at https://dc4420.org/):" % start.strftime("%a %d %B %Y")
        for speaker, title in talk_getter(event):
            print ' * %s: %s' % (speaker.replace('\n', ' '), title.replace('\n', ' '))

