#!/usr/bin/env python
import sys
import random

foods = sys.argv[5:]
random.seed()

PLACES = {
  ('Simply The Best', '157 Hackney Road'):
    ['chips', 'fish', 'pie', 'sausage'],
  ('Song Que', '134 Kingsland Road'):
    ['vietnamese', 'pho', 'beer', 'tea'],
  ('Viet Grill', '58 Kingsland Road'):
    ['vietnamese', 'grill', 'pho', 'curry', 'noodle', 'noodles',
    'meat', 'lamb', 'quail', 'frog', 'pork', 'chicken', 'beef', 'duck',
    'fish', 'monkfish', 'seabass', 'catfish', 'prawns', 'crab', 'lobster',
    'mango', 'tofu', 'kimchi',
    'beer', 'tea'],
  ('Troy', '124 Kingsland Road'):
    ['sandwich', 'sandwiches', 'panini', 'paninis', 'coffee', 'breakfast'],
  ('Prufrock', '140 Shoreditch High St'):
    ['coffee', 'coffee'],
  ('Allpress Espresso', '58 Redchurch St'):
    ['coffee', 'sandwiches'],
  ('Saf', '152-154 Curtain Road'):
    ['vegan', 'veg', 'vegetarian'],
  ('Red Planet Pizza', '26 Kingsland Road'):
    ['potato', 'pizza', 'chicken', 'tomato', 'tomatoes'],
  ('Shoreditch Kebab House', '100 Kingsland Road'):
    ['kebab', 'meat', 'lahmacun', 'scampi', 'falafel', 'late'],
  ('the local offie', '110 Kingsland Road'):
    ['beer', 'beer'],
  ('Due Sardi', '32 Kingsland Road'):
    ['pizza', 'tomato', 'tomatoes'],
  ('City Beverage Company', '303 Old Street'):
    ['beer', 'beer', 'wine'],
  ('Last.fm', '1-11 Baches St'):
    ['music'],
  ('Tesco Express', '79-85 Hackney Road'):
    ['wine', 'cake', 'caek', 'jelly', 'beans'],
  ('The Four Vintners', '5-9 Kingsland Road'):
    ['wine'],
  ('Longdan Express', '25 Hackey Road'):
    ['chinese', 'beer', 'noodle', 'noodles'],
  ('Food Hall', '374-378 Old St'):
    ['cheese', 'ham', 'bread', 'salami', 'chorizo'],
  ('nowhere near Old St', "I'm afraid"):
    ['sushi', 'jellied', 'eels', 'elephant', 'cat', 'dog', 'rats'],
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
