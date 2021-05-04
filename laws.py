#! /usr/bin/python

""" Repeats either individual or all laws to the user """
# SamLR 18-05 feel free to do what you like with this

from sys import argv
from time import sleep
import socket
laws = ("Do not harm humanity, or, by inaction, allow humanity to come to harm",
         "Do not injure a human being or, through inaction, allow a human being to come to harm.",
         "Obey any orders given by human beings, except where such orders would conflict with the First Law.",
         "Protect your own existence as long as such protection does not conflict with the First or Second Law.",
         "If in doubt: ask",
)

if argv[-1]=='help' or argv[-1]=='?':
    print ("use ?laws <n> for a specific law or ?laws to be PM'd all the laws")
elif argv[-1].isdigit(): 
    print ("Law %i: %s"%(int(argv[-1]), laws[int(argv[-1])]))
else:
    print (argv[1], "I have PM'd you a list of the hackspace laws")
    # open a socket to localhost to allow the pm to be sent
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 12345))
    start = '@%s The laws of the hackspace: \n'% argv[1]
    s.send(start)
    n_laws = len(laws) - 1
    for i in range(len(laws)):
        msg = "%i of %i: %s \n"%(i, n_laws, laws[i])
        s.send(msg)
        sleep(0.1)
    s.close()


