#!/usr/bin/python3
import json
import urllib

def get_urlencoded_thing(fetch_url, param):
    query = urllib.urlencode(param)
    url = fetch_url % query
    search_response = urllib.urlopen(url)
    search_results = search_response.read()
    return json.loads(search_results)

def get_google_result(searchfor):
    results = get_urlencoded_thing(
        'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s',
        {'q': searchfor})

    data = results['responseData']
    return data['results'][0]['unescapedUrl']

def get_boilerpipe_result(url):
    results = get_urlencoded_thing(
        'http://boilerpipe-web.appspot.com/extract?extractor=ArticleExtractor&output=json&%s',
        {'url': url})
    return results['response']['content']

import sys
url = get_google_result(' '.join(sys.argv[5:]))
text = get_boilerpipe_result(url)

ends = ['.', '?']

lines = text.splitlines()
for line in lines:
    line = line.strip()

    for end in ends:
        endpoint = line.find(end)

        if endpoint != -1:
            break

    if endpoint == -1:
        endpoint = len(line)

    extract = line[:endpoint]

    if len(extract) > 50:
        print extract
        break
