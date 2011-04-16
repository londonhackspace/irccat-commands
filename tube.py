#!/usr/bin/env python

import sys
import httplib, urllib, json

class TflLines():
	lines = [
		'bakerloo',
		'central',
		'circle',
		'district',
		'docklands',
		'hammersmithcity',
		'jubilee',
		'metropolitan',
		'northern',
		'piccadilly',
		'overground',
		'victoria',
		'waterloocity']

	@staticmethod
	def checkExist(item):
		if item in TflLines.lines:
			return True
		else:
			return False

class TubeStatus():
	
	def __init__(self):
		self.conn = httplib.HTTPConnection('api.tubeupdates.com')
		self.result = None

	def getStatus(self,line):
		params = urllib.urlencode({'method' : 'get.status','lines' : line})
		self.conn.request("GET","/?" + params)
		response = self.conn.getresponse()
		if response.status == 200:
			data = response.read();
			self.result = json.loads(data)
		self.conn.close()

	def printStatus(self):
		if (self.result != None):
			status_string = "There is "
			status_string = status_string + self.result['response']['lines'][0]['status']
			status_string = status_string + " on the "
			status_string = status_string + self.result['response']['lines'][0]['name'] + " line"
			status_string = status_string + " (data from tubeupdates.com)"
			print status_string

if __name__ == '__main__':
	if (len(sys.argv) > 5):
		line = sys.argv[5]
		if(TflLines.checkExist(line)):
			ts = TubeStatus()
			ts.getStatus(line)
			ts.printStatus()
		else:
			if (line == 'list'):
				list = "List of available lines: ["
				for line in TflLines.lines:
					list = list + line + " "
				list = list + "]"
				print list
			else:
				print "That's not a line (?tube list for a list of available lines)"
	else:
		print "Give me a line to check... (?tube list to show a list of available lines)"
