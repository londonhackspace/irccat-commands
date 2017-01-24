#!/usr/bin/env python
import requests
import nextevent
import datetime

#response = requests.get('http://www.opavote.com/api/elections/6555796884160512/n-votes')
response = requests.get('http://www.opavote.com/api/elections/6120523440324608/n-votes')
votes = int(response.content)

total = 1228

voting_ends = datetime.datetime(2016, 12, 4, 0, 0)
if voting_ends > datetime.datetime.now():
    end = nextevent.untilmsg(voting_ends).lower()

    print "%s votes cast (%i%% of membership). Voting closes in %s." % (votes, (100.0/total)*votes, end)
