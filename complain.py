#!/usr/bin/env python

import random
import sys
import inflect

p = inflect.engine()


complaints = [
  '%s plural_verb(is) Too Damn High',
  'Only occupikeys like %s',
  '%s plural_verb(causes) cancer',
  '%s plural_verb(takes) up too much space',
  '%s plural_verb(takes) up too much air',
  'Nobody emailed the list about %s',
  '%s should be banned',
  'Noisebridge allows %s',
  "People just can't be trusted with %s",
  "%s plural_verb(wasn't) my idea",
  '%s just plural_verb(needs) the rules to be enforced harder',
  'Nobody understands %s',
  '%s plural_verb(was) BORN FREE',
  'Nobody listens to me about %s',
  'Everyone just trolls about %s',
  '%s plural_verb(is) a technical solution to a social problem',
  'The silent majority hates %s',
  '%s should only be available to gold members',
  '%s only plural_verb(benefits) the elite',
  '%s plural_verb(was) created by the cabal',
  'I have the right not to look at %s',
  '%s plural_verb(is) a conspiracy by the technological elite',
]

thing = ' '.join(sys.argv[5:])

if thing:
  p.num(1)
  try:
    if ' and ' in thing or p.singular_noun(thing):
      # NB breaks "saving [him and her]", and "the answer to the ultimate question of life, the universe, and everything"
      p.num(3)
  except Exception, e:
    try:
      singulars = [p.singular_noun(w) for w in thing.split(' ')]
      if any(singulars):
        p.num(3)
    except:
      pass

  print p.inflect(random.choice(complaints) % thing).capitalize()
