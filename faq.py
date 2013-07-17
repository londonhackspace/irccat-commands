#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys

if len(sys.argv) > 5:
    term = ' '.join(sys.argv[5:])

    if "can i visit" in term.lower():
        print "While visitors can turn up at any time it's possible that no one will be there to let them in. There's also a chance everyone present will be too busy to give a tour or show visitors the ropes. In the past this has lead to people feeling lost and unwelcome, for this reason we highly encourage newbies come along to our Tuesday social night where there are proper introductions."
    elif "how much" in term.lower():
        print "The Hackspace doesn't have tiered or fixed membership fees. It's pay what you feel you get out of it. The minimum is £5/mo but the space needs members to be paying an average just over £20/mo in order to survive. If you're not using the space much or are on low income, it's fine to pay less but if you're using the space quite a bit or can afford to then you really should be paying at least the average."
    elif "jet" in term.lower():
        print "No"
    elif "radioactive" in term.lower():
        print "We are currently trying to set up a Nuclear Physics subgroup. Please contact them."
