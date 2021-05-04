#!/usr/bin/env python
# requires Debian package wbritish-insane
import random
import mmap
import re

def findpattern(data, pattern):
    word_re = re.compile(r'\n' + pattern)
    wordlist = word_re.findall(data)
    m = re.match(r'^' + pattern, data)
    if m:
        wordlist.insert(0, m.group(1))
    return wordlist

def filterwordlist(filename):
    f = open(filename)
    # faster than .read()
    data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    wordlist = ['drrk']
    wordlist += findpattern(data, r'([dD].*[kK])(?=\n)')
    wordlist += findpattern(data, r'([^aeiou]+ink)(?=\n)')
    wordlist .remove('drink')
    return wordlist

if __name__ == '__main__':
    wordlist = filterwordlist('/usr/share/dict/british-english-insane')
    print (random.choice(wordlist).decode('utf-8').upper().encode('utf-8'))

