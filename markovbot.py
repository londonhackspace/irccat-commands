#!/usr/bin/python
from random import choice

f = open  ("/usr/share/irccat/.markovbot.txt", "r")
ds = {}
for line in f:
	words = line.split(" ")
	for i,w in enumerate(words):
		w = w.strip()
		if i > 0:
			try:
				p = ds[w]
				p.append(words[i-1])
				ds[w] = p
			except:
				ds[w] = [words[i-1]]

start = choice(ds.keys())
phrase = ""
w = start
wlist = []
for i in range(100):
    try:
        wlist.append(w)
        w = choice(ds[w])
    except:
        break
wlist.reverse()

print " ".join(wlist)
