#!/usr/bin/env python
import string, sys
print("\x01ACTION "+filter(lambda x: x in string.printable[:-5]," ".join(sys.argv[5:]))+"\x01")
