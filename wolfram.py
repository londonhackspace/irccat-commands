#!/usr/bin/env python
import sys
import requests
import urllib
from lxml import etree

def find_node(root, possible_attribs):
    for attr in possible_attribs:
        node = root.xpath("/queryresult/pod[@title='%s']/subpod/plaintext" % attr)
        if node:
            return node[0].text

    return None


API_KEY = 'VX9PUR-8KE9RK9A75'

user = sys.argv[1]

query = ' '.join(sys.argv[5:])
query = urllib.quote(query)

response = requests.get('http://api.wolframalpha.com/v2/query?appid=%s&input=%s&format=plaintext' % (API_KEY, query))
root = etree.fromstring(response.content)

if root.xpath("/queryresult")[0].attrib['success'] == 'true':
    possible_questions = ('Input interpretation', 'Input')
    question = find_node(root, possible_questions)

    possible_answers = ('Current result', 'Response', 'Result')
    answer = find_node(root, possible_answers)

    print "%s: %s = %s" % (user, question, answer)
else:
    print "%s: Sorry, I don't understand the question" % user
