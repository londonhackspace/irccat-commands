#!/usr/bin/python
import sys
from socket import *

bits = ""
if len(sys.argv) < 5:
    bits = "000"
else:
    if "g" in sys.argv[5]:
        bits += "1"
    else:
        bits += "0"
    if "o" in sys.argv[5] or "a" in sys.argv[5]:
        bits += "1"
    else:
        bits += "0"
    if "r" in sys.argv[5]:
        bits += "1"
    else:
        bits += "0"

sock = socket(AF_INET, SOCK_DGRAM)
sock.sendto(bits, ("127.0.0.1", 9009))
