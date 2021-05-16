#!/usr/bin/env python

from urllib.parse import urlencode
from lxml import html

import sys
if len(sys.argv) <= 5:
    sys.exit(1)
postcode = sys.argv[5]

pdf = 'provideDetailsSubview:provideDetailsFragment:provideDetailsForm'
form = {
    pdf+':postCodeInput': postcode,
    pdf+':buildingNumberInput': '1',
    pdf+':searchButton': 'Search',
    pdf: pdf
}

o = urllib2.build_opener(urllib2.HTTPCookieProcessor())
urllib2.install_opener(o)

# FIXME: TFL redesigned their website, this script no longer works as-is

f = o.open('https://congestioncharging.tfl.gov.uk/b/pb/provideDetails.faces?referrer=cc')
f = o.open('https://congestioncharging.tfl.gov.uk/b/pb/provideDetails.faces', urlencode(form))

doc = html.parse(f).getroot()
outside = doc.get_element_by_id('ccImageOutside', None)
inside = doc.get_element_by_id('ccImageInside', None)
if outside is not None:
    print ('Outside the congestion zone')
if inside is not None:
    print ('Inside the congestion zone')
