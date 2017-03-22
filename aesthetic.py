#! /usr/bin/python

import sys
import string

if len(sys.argv) > 5:
  input_string = ' '.join(sys.argv[5:])
else:
  input_string = 'aesthetic'

for c in string.ascii_letters+string.digits:
    input_string = input_string.replace(c, unichr(ord(c)+65248))

print(unicode(input_string).encode('utf-8'))
