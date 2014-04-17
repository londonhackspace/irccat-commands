#!/usr/bin/env python

import random
import sys
import inflect


complaints = [
  u'%s plural_verb(is) Too Damn High',
  u'Only occupikeys like %s',
  u'%s plural_verb(causes) cancer',
  u'%s plural_verb(takes) up too much space',
  u'%s plural_verb(takes) up too much air',
  u'Nobody emailed the list about %s',
  u'%s should be banned',
  u'Noisebridge allows %s',
  u"People just can't be trusted with %s",
  u"%s plural_verb(wasn't) my idea",
  u'%s just plural_verb(needs) the rules to be enforced harder',
  u'Nobody understands %s',
  u'%s plural_verb(was) BORN FREE',
  u'Nobody listens to me about %s',
  u'Everyone just trolls about %s',
  u'%s plural_verb(is) a technical solution to a social problem',
  u'The silent majority hates %s',
  u'%s should only be available to gold members',
  u'%s only plural_verb(benefits) the elite',
  u'%s plural_verb(was) created by the cabal',
  u'I have the right not to look at %s',
  u'%s plural_verb(is) a conspiracy by the technological elite',
  u'%s plural_verb(is) destabilising the hackspace',
  u'%s plural_verb(is) off topic',
  u'%s plural_verb(is) morally tainted',
  u'Richard Stallman LOVES %s',
  u'Richard Stallman HATES %s',
  u'%s plural_verb(is) an embarrassment to the international hacker community',
  u'%s is peddled by M\xfcnchausen lovies',
]

thing = ' '.join(sys.argv[5:])

if thing:
  
  if 'cabal' in thing.lower():
      print "THERE IS NO IRC CABAL"
      sys.exit(0)

  p = inflect.engine()

  p.num(1)
  try:
    # if we can coerce the word to singular, it's probably plural
    if ' and ' in thing or p.singular_noun(thing):
      # NB breaks "doing this and that", and "the answer to the ultimate question of life, the universe, and everything"
      p.num(3)
  except Exception, e:
    try:
      spurious_singulars = ['thi']
      singulars = [p.singular_noun(w) for w in thing.split(' ')]
      singulars = [s for s in singulars if s not in spurious_singulars]
      if any(singulars):
        p.num(3)
    except:
      pass

  complaint = random.choice(complaints)
  if complaint.startswith('%s'):
    thing = thing.capitalize()
  else:
    thing = thing.lower()

  print p.inflect(complaint % thing).encode('utf-8')
