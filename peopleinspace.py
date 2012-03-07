#!/usr/bin/env python
import urllib2, lxml.html, sys, codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)

request = urllib2.Request('http://en.wikipedia.org/wiki/Template:People_currently_in_space')
request.add_header('User-Agent', 'Zomg, 1.0')

opener = urllib2.build_opener()
site = opener.open(request).read()

# To get around a bug in lxml
import StringIO
site = StringIO.StringIO(site)

root = lxml.html.parse(site).getroot()

amount = 0
strings = []

rows = root.xpath('//table[starts-with(@class, "nowraplinks collapsible autocollapse")]/tr')

for row in rows:
    orbiter = row.xpath('./th[@class="navbox-group"]')

    if orbiter:
        astronauts = row.xpath('.//td[starts-with(@class, "navbox-list navbox-")]/div//a')
 
        strings.append('%s on the %s' % (len(astronauts), orbiter[0].text_content()))
        amount += len(astronauts)


print "There are currently %s people in space! (%s)" % (amount, ', '.join(strings))
