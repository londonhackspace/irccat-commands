#!/usr/bin/python3
import sys

import math

if sys.argv[2] not in ['null', '#london-hack-space-dev']:
    print 'upword is private message/dev channel only'
    sys.exit()

word = sys.argv[5]
word = word.decode('utf-8')

vowel = None
for c,l in enumerate(word[:-1]):
    if l.lower() in ['a', 'i', 'u', 'e', 'o']:
        vowel = c

if vowel is None:
    try:
        vowel = word.index('y')
    except Exception:
        try:
            vowel = word.index('w')
        except Exception:
            vowel = len(word) - 1

with open("/proc/uptime", "r") as f:
   seconds = int(float(f.readline().split()[0]) / 60 / 60 /24)


st = word[:vowel] +  word[vowel:vowel+1] * seconds +  word[vowel+1:]

print st.encode('utf-8')

