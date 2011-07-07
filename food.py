#!/usr/bin/env python
import sys
import random

foods = sys.argv[5:]
random.seed()

PLACES = {
    ('Simply The Best', '157 Hackney Road'):
        ['chips', 'fish', 'pie', 'sausage'],
    ('Song Que', '134 Kingsland Road'):
        ['vietnamese', 'pho', 'beer'],
    ('Troy', '124 Kingsland Road'):
        ['sandwiches', 'paninis', 'coffee'],
    ('Prufrock', '140 Shoreditch High St'):
        ['coffee', 'coffee'],
}

def foodscore(food, foods):
  def match(f):
    return f.upper() == food.upper()

  return len(filter(match, foods))

totals = dict.fromkeys(PLACES, 0)

for food in foods:
  places = [(place, foodscore(food, foods)) for place, foods in PLACES.items()]

  if not any(places):
    continue # unrecognised food

  for place, score in places:
    totals[place] += score

if not any(totals.values()):
  place, addr = random.choice(PLACES.keys())
  msg = 'Nothing found. Why not try %s, %s?' % (place, addr)

else:
  bestscore = sorted(totals.values())[-1]
  candidates = [place for place, score in totals.items() if score == bestscore]
  place, addr = random.choice(candidates)
  msg = '%s, %s' % (place, addr)

print msg
