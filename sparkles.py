#!/usr/bin/python3
import sys
import subprocess
import pipes 

argv = sys.argv[1:]

quoted = [pipes.quote(arg) for arg in argv]

quoted.insert(0,"/home/eb4890/sparkles/sparkles.py")
#argv.insert(len(argv), "&")

#print argv
subprocess.Popen(" ".join(quoted) +  "&", shell=True)
