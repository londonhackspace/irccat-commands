#! /usr/bin/python

import sys
import string

if len(sys.argv) > 5:
  input_string = ' '.join(sys.argv[5:])
else:
  input_string = 'aesthetic'

# See https://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms
for c in range(0x21, 0x7f):
    input_string = input_string.replace(chr(c), unichr(c - 0x21 + 0xff01))

input_string = input_string.replace(' ', u'\u3000')

print(unicode(input_string).encode('utf-8'))
