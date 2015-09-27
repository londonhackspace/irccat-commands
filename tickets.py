#!/usr/bin/env python
import requests

stats = requests.get('https://www.emfcamp.org/stats')
stats = [fv.split(':') for fv in stats.content.split(' ')]
stats = dict((f, int(v)) for f, v in stats)
print 'EMF tickets sold: %s' % (stats['full_unpaid'] + stats['full_bought'])

