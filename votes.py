#!/usr/bin/env python
import requests
import nextevent
import datetime

response = requests.get('http://www.opavote.org/api/elections/4877610177789952?p=n_votes')
votes = int(response.content)

total = 1119

voting_ends = datetime.datetime(2014, 12, 29, 21, 0)
if voting_ends > datetime.datetime.now():
    end = nextevent.untilmsg(voting_ends).lower()

    print "%s votes cast (%i%% of membership). Voting closes in %s." % (votes, (100.0/total)*votes, end)
