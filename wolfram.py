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

def find_id_node(root):
    node = root.xpath("/queryresult/pod[@id='Input']/subpod/plaintext")
    return node[0].text

def find_non_id_node(root):
    node = root.xpath("/queryresult/pod[@id!='Input']/subpod/plaintext")
    return node[0].text

API_KEY = 'VX9PUR-8KE9RK9A75'

user = sys.argv[1]

query = ' '.join(sys.argv[5:])
query = urllib.quote(query)

response = requests.get('http://api.wolframalpha.com/v2/query?appid=%s&input=%s&format=plaintext' % (API_KEY, query))
root = etree.fromstring(response.content)

if root.xpath("/queryresult")[0].attrib['success'] == 'true':
    if False: # overspecific and often wrong
        possible_questions = ('Input interpretation', 'Input')
        question = find_node(root, possible_questions)

        possible_answers = ('Current result', 'Response', 'Result', 'Results', 'IP address registrant', 'Definitions')
        answer = find_node(root, possible_answers)
    else:
        question = find_id_node(root)
        answer = find_non_id_node(root)

    answer = answer.replace('\n', ', ')

    response = "%s: %s = %s" % (user, question, answer)
    print response.encode('utf8')
