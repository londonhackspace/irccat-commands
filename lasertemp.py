#! /usr/bin/python
import sys, time, re, urllib, urllib2

f = open("/home/solexious/coolbot/waterTemp", "r")
number = f.read()
hours = int(number) / 100.0
print 'Laser cutter temperature: %.2f degrees' % (hours)
message = urllib.quote('Lasercutter:%.2fDEG' % (hours))
urllib2.urlopen("http://127.0.0.1:8020/%s?restoreAfter=5" % message)
