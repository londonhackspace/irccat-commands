#!/usr/bin/env python

import sys, re, codecs
from urllib import urlencode
from urllib2 import urlopen, Request
import simplejson as json
import ConfigParser

args = sys.argv[5:]
if not args:
  sys.exit()

config = ConfigParser.ConfigParser()
config.read((
    '.babel.conf',
    sys.path[0] + '/.babel.conf',
    '/etc/babel.conf'
))

apikey = config.get('babel', 'key')

if '|' in args[0]:
  langpair = args.pop(0)
else:
  langpair = '|en'

text = ' '.join(args)
if re.match(r'[.\- ]+', text) and text:
  import subprocess
  proc = subprocess.Popen('/usr/games/morse -ds -- %s' % text, shell=True, stdout=subprocess.PIPE)
  text = ' '.join(proc.communicate()[0].splitlines())

if langpair.split('|')[1] == 'morse' and text:
  import subprocess
  proc = subprocess.Popen('/usr/games/morse -s -- %s' % text, shell=True, stdout=subprocess.PIPE)
  text = ''.join(proc.communicate()[0].splitlines())
  print text
  sys.exit()


def translate_api(langpair, text):
  # Doesn't work with Latin yet (as that's alpha)
  sl, pipe, tl = langpair.partition('|')
  params = {
      'key': apikey,
      'q': text,
      'source': sl,
      'target': tl,
  }
  qs = urlencode(params)
  url = 'https://www.googleapis.com/language/translate/v2?' + qs
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

def translate_web(langpair, text):
  sl, pipe, tl = langpair.partition('|')

  def _translate_web(text, sl, tl):

    params = {
      'client': 't',
      'text': text,
      'sl': sl,
      'tl': tl,
      #'hl': 'en',
      'sc': 1, # suggest
      #'multires': 1,
    }
    qs = urlencode(params)
    headers = {
      'Referer': 'http://translate.google.com?hl=en',
      'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686)' # From urllib2 docs
                    ' Gecko/20071127 Firefox/2.0.0.11',
    }
    req = Request('http://translate.google.com/translate_a/t?', qs, headers)
    res = urlopen(req).read()
    #print res
    res = res.replace(',,',',null,')
    res = res.replace(',,',',null,')
    res = res.replace(',]',',null]')
    #print res
    res = json.loads(res)

    lines, senses, lang, parsing, analysis, alternates = res[:6]
    #print res
    u1, didyoumean, u2, score = res[6:11]
    text = ''.join(tt for tt, st, u3, standalone in lines)
    if analysis:
      # I think u3 might be popularity
      t = [(tt, sp) for tt, alts, sp, u2, u3, wfrom, wto, line in analysis]
      text = ''.join('%s%s' % (' ' if sp == 1 else '', tt) for tt, sp in t)
      text = text.lstrip(' ')

    return text, lang, score, didyoumean

  textxl, lang, score, didyoumean = _translate_web(text, sl, tl)

  if textxl == text:
    textrot13 = codecs.encode(text, 'rot13')
    textrot13xl, langrot13, scorerot13, didyoumeanrot13 = _translate_web(textrot13, sl, tl)
    if scorerot13 < score:
      textxl, lang, didyoumean = textrot13xl, 'rot13, %s' % langrot13, didyoumeanrot13

  if not sl and lang != 'en':
    msg = '%s (%s)' % (textxl, lang.title())
  else:
    msg = textxl

  if didyoumean:
    html, text = didyoumean[:2]
    #html = html.decode('unicode-escape')
    msg = '%s (Did you mean %s?)' % (msg, text)

  print msg.encode('utf-8')


if False:
    translate_api(langpair, text)

else:
    translate_web(langpair, text)

#match = re.search('"estimatedResultCount":"(.*?)"', page)
#if match:
#  count = int(match.group(1))
#  print locale.format('%d', count, True)
