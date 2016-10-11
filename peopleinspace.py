#!/usr/bin/env python
import sys
import codecs
import json
import urllib2

sys.stdout = codecs.getwriter('utf8')(sys.stdout)

request = urllib2.Request('http://www.howmanypeopleareinspacerightnow.com/space.json')
request.add_header('User-Agent', 'Zomg, 1.0')
opener = urllib2.build_opener()
response = opener.open(request).read()

data = json.loads(response)
people = [person['name'] for person in data['people']]

print "There are currently %s people in space! (%s)" % (data['number'], ', '.join(people))
