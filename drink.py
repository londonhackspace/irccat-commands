#!/usr/bin/env python
import random
import mmap
import re

def readwordlist(filename):
    f = open(filename)
    # faster than .read()
    data = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    word_pattern = r'([dD].*[kK])(?=\n)'
    word_re = re.compile(r'\n' + word_pattern)
    wordlist = word_re.findall(data)
    m = re.match(r'^' + word_pattern, data)
    if m:
        wordlist.insert(0, m.group(1))
    return wordlist

if __name__ == '__main__':
    wordlist = readwordlist('/usr/share/dict/british-english-insane')
    print random.choice(wordlist).decode('utf-8').upper().encode('utf-8')

