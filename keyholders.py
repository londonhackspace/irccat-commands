#!/usr/bin/python
import urllib2, re

url = "http://wiki.hackspace.org.uk/w/index.php?title=Keyholders&printable=yes"
response = urllib2.urlopen(url)
data = response.read()

match = re.search('Current.*?<ul>(.*?)</ul>', data, re.DOTALL)
people = match.group(1)

# Woo, evil!
peopleList = re.findall('<li>\s*(?:<a.*?>)?\s*(.*?)\s*(?:</a>.*?)?\s</li>', people, re.DOTALL);

print 'Current Keyholders: ' + ', '.join(peopleList)
