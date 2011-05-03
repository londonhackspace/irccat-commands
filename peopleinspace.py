#!/usr/bin/env python
import lxml.html
import urllib2

site = urllib2.urlopen('http://www.howmanypeopleareinspacerightnow.com')

root = lxml.html.parse(site).getroot()

content_node = root.xpath('//div[@class="content"]')

num_node    = content_node[0].xpath('//h2')
num_people  = num_node[0].text_content()

text_node   = content_node[0].xpath('//p')
text        = text_node[2].text_content().lower()

print "There are currently %s people in space, %s." % (num_people, text)
