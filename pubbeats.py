#!/usr/bin/python

from time import localtime, timezone
import sys

pubtime = 770 #in beats

def itime():

    h, m, s = localtime()[3:6]
    beats = ((h * 3600) + (m * 60) + s + timezone) / 86.4
    if beats > 1000:
        beats -= 1000
    elif beats < 0:
        beats += 1000
    return beats

def pub():
    timeleft = pubtime - itime()
    print("@{0:0.3f} beats left until pub o'clock".format(timeleft))

if __name__ == "__main__":
    pub()
