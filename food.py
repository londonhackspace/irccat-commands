#!/usr/bin/env python
import sys
import random

foods = sys.argv[5:]
random.seed()

PLACES = {
  ('Bumsmiths', '31 Coate St'):
    ['burgers', 'burger', 'pulled pork', 'slaw', 'coleslaw'],
  ('Simply The Best', '157 Hackney Road'):
    ['chips', 'fish', 'pie', 'sausage'],
  ('Tesco Express', '79-85 Hackney Road'):
    ['wine', 'cake', 'caek', 'jelly', 'beans', 'horsemeat', 'horses', 'horse'],
  ('Longdan Express', '25 Hackey Road'):
    ['chinese', 'beer', 'noodle', 'noodles'],
  ('Hot Pot', 'Hackney Rd, nr Columbia Rd'):
    ['italian','cafe'],
  ('Ridley Road Market', 'Dalston'):
    ['bushmeat', 'buffalo', 'kangaroo', 'pygmy', 'crocodile'],
  ('nowhere near Hackney Road', "I'm afraid"):
    ['sushi', 'jellied', 'eels', 'elephant', 'cat', 'dog', 'rat', 'rats', 'cockroaches', 'cockroach'],
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
  if not any(foods):
    msg = ''
  else:
    msg = 'Nothing found. '
  msg += 'Why not try %s, %s?' % (place, addr)

else:
  bestscore = sorted(totals.values())[-1]
  candidates = [place for place, score in totals.items() if score == bestscore]
  place, addr = random.choice(candidates)
  msg = 'I suggest %s, %s' % (place, addr)

print msg
