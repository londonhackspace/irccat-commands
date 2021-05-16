#!/usr/bin/env python
import sys
import random

foods = sys.argv[5:]
random.seed()

PLACES = {
  ('Bunsmiths', '31 Coate St'):
    ['burgers', 'burger', 'pulled pork', 'slaw', 'coleslaw'],
  ('Hurwundeki', '298-299 Cambridge Heath Road'):
    ['korean', 'bibimbap', 'kimchi', 'noodle', 'noodles', 'udon', 'pancake', 'pancakes',
     'dumpling', 'dumplings', 'bulgogi', 'haircut', 'haircuts'],
  ('Mother Kelly\'s', '251 Paradise Row'):
    ['beer'] * 3 + ['cheese', 'ham'],
  ('Redchurch Brewery', '275 Poyser St'):
    ['beer'] * 2,
  ('Japanese Canteen', '255 Paradise Row'):
    ['sushi', 'noodle', 'noodles', 'ramen', 'donburi', 'fried chicken', 'chicken',
     'bibimbap', 'kimchi', 'sashimi'],
  ('Ra\xc3\xadzes', '460 Hackney Road'):
    ['meat', 'rodizio', 'grill', 'brasilian', 'brazilian', 'brasil', 'brazil', 'fish'],
  ('Cafe Maloka', '62, Broadway Market'):
    ['vegetarian', 'vegan', 'coffee', 'cake', 'caek', 'tea', 'salad'],
  ('Billy\'s Cafe'):
    ['chips', 'egg', 'bacon', 'beans', 'sausage', 'spam', 'fry-up',
     'full english', 'english breakfast', 'breakfast', 'toast'],
  ('Broadway Fish Bar', '8 Broadway Market'):
    ['chips', 'fish', 'pie'],
  ('Tesco Express', '79-85 Hackney Road'):
    ['wine', 'cake', 'caek', 'jelly', 'beans', 'horsemeat', 'horses', 'horse'],
  ('Ridley Road Market', 'Dalston'):
    ['bushmeat', 'buffalo', 'kangaroo', 'pygmy', 'crocodile'],
  ('Franco Manca', 'Broadway Market'):
    ['pizza', 'pizza', 'sourdough'],
  ('Hackney Coffee Co', '499 Hackney Road'):
    ['coffee'] * 3,
  ('nowhere near Hackney Road', "I'm afraid"):
    ['jellied', 'eels', 'elephant', 'cat', 'dog', 'rat', 'rats', 'cockroaches', 'cockroach'],
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
  place, addr = shuffle(choice(list(PLACES.keys()))
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

print (msg)
