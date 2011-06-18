#! /usr/bin/python

""" Repeats either individual or all rules to the user """
# SamLR 18-05 feel free to do what you like with this

from sys import argv
from time import sleep
import socket
rules = ("Do not be on fire",
         "Don't use power tools without briefing",
         "Don't defeat/hack safety features",
         "If in doubt: ask",
         "If something is broken, fix it",
         "If you're doing something major, ask the mailing list",
         "Members may store things in the space but it must be in a box; one box per member",
         "Large items are allowed but must be cleared with the list first and labelled",
         "Please don't donate crap",
         "If you don't want something hacked label it as such",
         "If something looks expensive check before hacking",
         "Workareas must be clean before you leave, tools must be returned",
         "Put dirty crockery in the dishwasher before you leave", 
         "Items left in workareas are fair game",
         "Made a mess? clean it up",
         "If an item needs to be thrown put it in the 3 week box",
         "Large items (that won't fit in the box) should be checked with the list before disposal",
         "Check with the list before throwing useful items",)

if argv[-1]=='34':
    print "If you can think of it, the internet has porn of it"
if argv[-1]=='help' or argv[-1]=='?':
    print "use ?rules <n> for a specific rule or ?rules to be PM'd all the rules"
elif argv[-1].isdigit(): 
    print "Rule %i: %s"%(int(argv[-1]), rules[int(argv[-1])])
else:
    print argv[1], "I have PM'd you a list of the hackspace rules"
    # open a socket to localhost to allow the pm to be sent
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 12345))
    start = '@%s The rules of the hackspace: \n'% argv[1]
    s.send(start)
    n_rules = len(rules) - 1
    for i in range(len(rules)):
        msg = "%i of %i: %s \n"%(i, n_rules, rules[i])
        s.send(msg)
        sleep(0.1)
    s.close()


