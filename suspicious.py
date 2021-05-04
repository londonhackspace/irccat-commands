#!/usr/bin/python3

import random

suspicious = [
    'http://i.imgur.com/cgxBjhz.jpg',
    'http://goo.gl/KrrNCQ',
    'http://goo.gl/AgyDB0',
    'http://goo.gl/s4UpVu',
    'http://goo.gl/wOjkwH',
    'http://goo.gl/ewD2tO',
    u'http://hack.rs/\u0ca0_\u0ca0.jpg',
]
print ( suspicious[random.randrange(len(suspicious))].encode('utf-8') )

