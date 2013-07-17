#!/usr/bin/env python
from xml.dom.minidom import parseString
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
from sys import argv, exit, stderr
from os.path import expanduser

VERSION = '0.3'
URL = 'http://closure.ath.cx/cliweather'

place = ' '.join(argv[5:])
if not place:
    place = 'E2 9DY'

api = 'http://www.google.com/ig/api?%s' % urlencode({'weather': place})

dom = parseString(urlopen(api).read())

items = [ 'city'
        , 'condition'
        , 'temp_f'
        , 'temp_c'
        , 'humidity'
        , 'wind_condition' ]
info = {}
try:
    for item in items:
        info[item] = dom.getElementsByTagName(item)[0].getAttribute('data')
except IndexError:
    stderr.write('Invalid Area\n')
    exit(1)

#print('City: %s' % info['city'])
msg = u'%s%s\xb0C/%s\xb0F, %s, %s' % (
    info['condition'] and '%s ' % info['condition'] or '',
    info['temp_c'], info['temp_f'],
    info['humidity'],
    info['wind_condition'],
)
print msg.encode('utf-8')
