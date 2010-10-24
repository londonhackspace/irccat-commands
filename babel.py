#!/usr/bin/env python

import sys, re
from urllib import urlencode
from urllib2 import urlopen, Request
import simplejson as json

args = sys.argv[5:]
if not args:
  sys.exit()

if '|' in args[0]:
  langpair = args.pop(0)
else:
  langpair = '|en'

if False:
  # Doesn't work with Latin yet (as that's alpha)
  params = {
    'v': '1.0',
    'q': ' '.join(args),
    'langpair': langpair,
  }
  qs = urlencode(params)
  url = 'http://ajax.googleapis.com/ajax/services/language/translate?' + qs
  res = json.loads(urlopen(url).read())
  #print res
  data = res.get('responseData')
  if data:
    text = data.get('translatedText', '')
    lang = data.get('detectedSourceLanguage')
    if True and lang and lang != 'en':
      print '%s (%s)' % (text, lang.title())
    else:
      print text
  else:
    err = res.get('responseDetails')
    if err:
      print 'Error: %s' % res['responseDetails']
    else:
      print 'API failure'

else:
  sl, pipe, tl = langpair.partition('|')
  params = {
    'client': 't',
    'text': ' '.join(args),
    'sl': sl,
    'tl': tl,
  }
  qs = urlencode(params)
  headers = {
    'Referer': 'http://translate.google.com?hl=en',
    'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686)' # From urllib2 docs
                  ' Gecko/20071127 Firefox/2.0.0.11',
  }
  req = Request('http://translate.google.co.uk/translate_a/t?', qs, headers)
  res = urlopen(req).read()
  #print res
  res = json.loads(res.replace(',,',',null,'))
  phrases, senses, lang = res
  text = ''.join(tt for tt, st, dunno in phrases)
  if True and not sl and lang != 'en':
    print '%s (%s)' % (text, lang.title())
  else:
    print text



#match = re.search('"estimatedResultCount":"(.*?)"', page)
#if match:
#  count = int(match.group(1))
#  print locale.format('%d', count, True)

