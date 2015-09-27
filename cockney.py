#!/usr/bin/env python
import requests
import lxml.html
import sys
import codecs
import difflib
from collections import defaultdict

sys.stdout = codecs.getwriter('utf8')(sys.stdout)

if len(sys.argv) < 6:
  sys.exit()

term = ' '.join(sys.argv[5:])

response = requests.get('http://www.aldertons.com/english-.htm')
# http://abceda.com/cockney.html
# http://www.freelang.net/dictionary/docs/html_cockney_english.php
# http://www.freelang.net/dictionary/docs/html_english_cockney.php
# add http://www.cockneyrhymingslang.co.uk/english/A ?

content = response.content.decode('cp1252')
root = lxml.html.document_fromstring(content)

cells = root.xpath('(//table)[2]//td[position() = 1 or position() = 2]')
cells = [c.text_content().strip() for c in cells]
pairs = zip(*[iter(cells)]*2)

pairs += [
  # (English, Cockney)

  # Some clearly apocryphal (prune), but in Ronnie Barker sketch:
  #   https://www.youtube.com/watch?v=4RwyPDPlFA8
  ('shoes', 'how-de-doos'),
  ('dirty', 'two-thirty'),
  ('quid', 'saucepan lid'),
  ('drawers', 'early doors'),
  ('pub', 'rub-a-dub'),
  ('drink', 'tumble down the sink'),
  ('pissed (drunk)', 'Mozart and Liszt'),
  ('tune', 'stewed prune'),
  ('trouble', 'froth and bubble'),
  ('fire', 'Jeremiah'),
  ('chair', 'Lionel Blair'),

  ('C**t', 'berk'),
  ('C**t', 'Berkeley Hunt'),
  ('C**t', 'James Blunt'),
  ('cafe', 'Colonel Gaddafi'),

  # http://news.bbc.co.uk/1/hi/england/london/8217499.stm
  # http://www.huffingtonpost.co.uk/2012/07/23/london-2012-cockney-atm-machines-installed_n_1695066.html
  ('PIN', 'Huckleberry Finn'),
  ('screen', 'Charlie Sheen'),
  ('receipt', 'Fleet Street'),
  ('twenty', 'horn of plenty'),
  ('card', 'bladder of lard'),
]

defns = defaultdict(list)
for en, crs in pairs:
  crs = crs.replace('-', ' ')
  crs = crs.lower()
  defns[crs].append(en)

term = term.replace('-', ' ')
term = term.lower()

matches = difflib.get_close_matches(term, defns, 1, 0.2)
# NB need to cover abbreviations (e.g. "trouble" for "trouble and strife", currently matches "toby ale")
if matches:
  ens = defns[matches[0]]
  
  ens_list, ens_last = ', '.join(ens[:-1]), ens[-1]
  if ens_list:
    ens_text = '%s or %s' % (ens_list, ens_last)
  else:
    ens_text = ens_last

  print '%s is cockney rhyming slang for %s' % (matches[0], ens_text)


