#!/usr/bin/python3

import random
import sys

'''
##########

Hackspace excuses

##########
'''

reasons = [
    "Work got in the way",
    "I wasn't expecting it to arrive yet",
    "I forgot about it",
    "I'm a trustee",
    "I'm not allow to ship stuff to work",
    "I told someone in the space about it and they said it was ok",
    "I slept in",
    "I'm not in the country at the moment",
    "Extended work hours",
    "I was too tired",
    "I fell asleep",
    "I lost track of time",
    "Someone could make X with it",
    "I've been ill",
    "We had an emergency.",
    "I had to get the last train",
    "The delivery was late",
    "It was a last minute thing",
    "I had already paid the driver",
    "It was entirely ad-hoc and unplanned",
    "It would have been a shame to let it go to waste",
    "We had to act fast in order to get it",
    "I was in a hurry/rush",
    "It's too cumbersome to move around on public transport",
    "It's going to benefit the whole space",
    "I got knocked off my bike again",
    "It's fundamental to my personality",
    "I was BORN FREE",
    "It's actually about ethics in games journalism",
]

if len(sys.argv) > 5:
    term = " ".join(sys.argv[5:])

    for reason in reasons:
        if term.lower() in reason.lower():
            msg = "BINGO! {0}!".format(reason)
            print (msg)
            break
else:
    reason = random.choice(reasons)
    print (reason)
