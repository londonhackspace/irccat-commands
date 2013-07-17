#!/usr/bin/env python
import socket
s=socket.socket()
s.connect(("towel.blinkenlights.nl",666))
d=''
while len(d)<20:
    d+=s.recv(2048)
s.close()
print(d.splitlines()[4])
