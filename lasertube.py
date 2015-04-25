#! /usr/bin/python

f = open("/home/solexious/coolbot/totalTime", "r")
seconds = int(f.read())

hours = seconds / 3600
minutes = (seconds % 3600) / 60
seconds = (seconds % 3600) % 60

print '%dh:%dm:%ds of lasing have occurred. Approximately %d hours until the tube dies.' % (hours, minutes, seconds, 700 - hours)
