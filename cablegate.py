#!/usr/bin/python3
import urllib
import os
import sys
import argparse
from lxml import etree
from lxml import html
import StringIO, webbrowser
import HTMLParser
import traceback
import random
import time, re, urllib, urllib2

#url = "http://www.moveflat.com/london-flat/flatshare-flatmate/london-areas/property/Box/"
#sock = urllib.urlopen(url)
#htmlSource = sock.read()    
#sock.close()

parser = argparse.ArgumentParser(description='Parse Cablegate Files')
parser.add_argument('-d', dest='directory', nargs=1, required=True, help="Cablegate Directory") 
parser.add_argument('-l', dest='year', nargs=1, required=True, help="Year YYYY Format") 

args = parser.parse_args()
cable_files = []

try:

	for dirname, dirnames, filenames in os.walk(args.directory[0] + "/cable/" + args.year[0]):
		#for subdirname in dirnames:
		#	print os.path.join(dirname, subdirname)
		for filename in filenames:
			#print os.path.join(dirname, filename)
			cable_files.append(os.path.join(dirname, filename))

except Exception, err:
	print "An Error Occurred! "
	traceback.print_exc()
	sys.exit()

final_items = []

for fname in cable_files:
	try:
		f = open(fname,'r+')
		
		source = f.read()
		
		result = html.fromstring(source)
		
		f.close()
	
		details = result.find_class("cable")[0]
		
		cable = result.findall(".body/div/div/code")[1]	# use xpath relative
		
		#print html.tostring(details)
		
		cable_string = html.tostring(cable)
		
		rawitems = cable_string.split("<a")
		

		for item in rawitems:
			#tidy the items
			item = item[item.find("</a>")+4:]
			
			item = item.strip("END SUMMARY")
			
			item= HTMLParser.HTMLParser().unescape(item)
			
			subitems = item.split("\n\n")
			for sitem in subitems:

				titem = ""
				subsubitems = sitem.split("\n")
				for ssitem in subsubitems:	
					if not( ssitem == " " or "--------" in ssitem or "</code>" in ssitem or "<pre>" in ssitem or ssitem.upper() == ssitem) and len(ssitem) > 1:
						titem += ssitem
				if len(titem) > 100 and not "Classified By:" in titem and not "CLASSIFIED BY:" in titem and titem.upper() != titem and not "SUBJECT:" in titem:
					final_items.append(titem)
						
		
		
			
	except Exception, err:
		#print "Error"
		#traceback.print_exc()
		pass


random.seed()
premsg = final_items[ random.randint(0, len(final_items) -1 ) ]
pitems = premsg.split(".")
final_items = []
for pitem in pitems:
	if len(pitem) > 10:
		final_items.append(pitem)
premsg = final_items[random.randint(0, len(final_items) -1 )]	
premsg = "<^(,__,)~~" +  premsg [:140] + "..."
if len(premsg) > 0:
	print premsg
	
message = urllib.quote(premsg)
urllib2.urlopen("http://127.0.0.1:8020/%s" % message)


	
#print "FINAL ITEMS"
#for item in final_items:
#	print "***"
#	print item
