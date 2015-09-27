#!/usr/bin/env python
import socket
import time
import os

if not os.path.exists("/tmp/lastyarnol"):
    p = open("/tmp/lastyarnold","w")
    p.write("0\r\n")
    p.close()

f = open ("/tmp/lastyarnold", "r")

t = float(f.readline())
f.close()
if time.time() - t > 300:
	f = open("/tmp/lastyarnold", "w")
	f.write(str(time.time()))
	f.close()
else:
	print "give it a minute mate"
	exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.sendto("TRIGGER\nfixed/yarnold.wav\n",('<broadcast>', 50002))
s.close()
print "Hello Mr Yarnold"
