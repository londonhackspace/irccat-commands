#!/usr/bin/env python

import urllib, sys, re
from lxml import etree


word = ' '.join(sys.argv[5:]).lower()

f = urllib.urlopen('http://kill-or-cure.heroku.com/a-z/%s' % word[0])

foundterm = False
msg = causetitle = preventtitle = None

ns = ''
for ev, el in etree.iterparse(f, events=['start-ns', 'end']):
    if ev == 'start-ns':
        prefix, ns = el
        continue

    if el.tag == '{%s}h2' % ns:
        if foundterm:
            break

        classes = el.get('class').split(' ')
        if 'termHeading' in classes:
            term = el.findtext('{%s}em' % ns)
            if term.lower() == word:
                foundterm = True
                result, = set(['both', 'cause', 'prevent']) & set(classes)
                msg = etree.tostring(el, method='text')
                msg = re.sub(r'\s+', ' ', msg).strip('# ')


    elif foundterm and el.tag == ('{%s}ul' % ns):
        if el.get('class') == 'cause':
            causetitle = el.findtext('{%s}li/{%s}a' % (ns, ns))
            
        elif el.get('class') == 'prevent':
            preventtitle = el.findtext('{%s}li/{%s}a' % (ns, ns))
        
        elif el.get('class') == 'pagination':
            break

else:
    sys.exit(1)


if msg:
    msg = msg[0].upper() + msg[1:]
    titles = ['"%s"' % t for t in [causetitle, preventtitle] if t]
    if titles:
        print '%s (%s)' % (msg, ' vs '.join(titles))
    else:
        print msg
