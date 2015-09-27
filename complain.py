#!/usr/bin/env python

import random
import sys
import inflect


complaints = [
  u'%s plural_verb(is) Too Damn High',
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
  u'%s plural_verb(was) banned by the fun police',
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
  u'%s plural_verb(is) peddled by M\xfcnchausen lovies',
  u'%s plural_verb(is) unexcellent',
  u'%s plural_verb(is) on the rise',
  u'%s plural_verb(brings) smelly hackers to the space',
# nobody's ever used this complaint  u'%s secretly plural_verb(hates) the Computer',
  u'%s plural_verb(is) what the Failing List is all about',
  u'%s plural_verb(is) a very serious concern and must be addressed urgently',
  u'%s plural_verb(is) not a permitted activity',
  u'%s plural_verb(requires) an official trustee-backed request',
  u'%s plural_verb(isn\'t) in the interest of the Hackspace\'s shareholders',
  u'How the hell plural_verb(was) %s allowed past the moderators?',
  u'%s should just get in the fucking sea',
  u'%s plural_verb(needs) people to show some respect instead of just abusing us',
]

thing = ' '.join(sys.argv[5:]).decode('utf-8')

def spurious_singular(word):
    word = word.lower()
    if word.endswith('u') or word.endswith('nes'):
        # cactus, virus, darkness, etc.
        return True
    if word in ['thi', 'stratasy']:
        return True
    return False

if thing:
  
  if 'cabal' in thing.lower():
      print "THERE IS NO IRC CABAL"
      sys.exit(0)

  p = inflect.engine()


  p.num(1)
  try:
    # if we can coerce the word to singular, it's probably plural
    if ' and ' in thing or p.singular_noun(thing):
      if not spurious_singular(p.singular_noun(thing)):
        # NB breaks "doing this and that", and "the answer to the ultimate question of life, the universe, and everything"
        p.num(3)
  except Exception, e:
    try:
      singulars = [p.singular_noun(w) for w in thing.split(' ')]
      singulars = [s for s in singulars if not spurious_singular(s)]
      if any(singulars):
        p.num(3)
    except:
      pass

  complaint = random.choice(complaints)
  if thing.lower() == thing:
    if complaint.startswith('%s'):
      thing = thing[0].upper() + thing[1:]

  print p.inflect(complaint % thing).encode('utf-8')

