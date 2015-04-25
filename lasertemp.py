#! /usr/bin/python
import sys, time, re, urllib, urllib2

f = open("/home/solexious/coolbot/waterTemp", "r")
number = f.read()
tube = int(number) / 100.0
message = urllib.quote('Lasercutter:%.2fDEG' % (tube))
#urllib2.urlopen("http://127.0.0.1:8020/%s?restoreAfter=5" % message)
f = open("/home/solexious/coolbot/roomTemp", "r")
number = f.read()
room = int(number) / 100.0
f = open("/home/solexious/coolbot/outflowTemp", "r")
number = f.read()
outflow = int(number) / 100.0
print 'Laser cutter temperature: Cooling water: %.2f degrees, Room: %.2f degrees, Outflow: %.2f degrees' % (tube, room, outflow)
