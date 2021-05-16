#!/opt/irccat/irccat-commands/lhsephem-venv/bin/python
from lhsephem import getbody, lhs
from ephem import EarthSatellite, EllipticalBody, meters_per_au

import sys, math
import requests
from lxml import etree, objectify
from datetime import datetime, timedelta

def revgeocode(lat, lng):
    # http://www.geonames.org/export/web-services.html
    resp = requests.get('http://api.geonames.org/extendedFindNearby', params={'lat': lat, 'lng': lng, 'username': 'ms7821'})
    root = objectify.fromstring(resp.content)
    #print (resp.content)

    if hasattr(root, 'geoname'):
        # http://www.geonames.org/export/codes.html
        geonames = list(root.geoname)
        """
        <name>Earth</name>
        <fcl>L</fcl>
        <fcode>AREA</fcode>

        <name>Africa</name>
        <fcl>L</fcl>
        <fcode>CONT</fcode>

        <name>Libya</name>
        <fcl>A</fcl>
        <fcode>PCLI</fcode>

        <name>Al \u2018Uwayn\u0101t</name>
        <fcl>P</fcl>
        <fcode>PPL</fcode>
        """
        if len(geonames) < 3:
            return geonames[-1].name
        # We don't care about province names - country is more meaningful
        if len(geonames) < 5:
            return geonames[2].name
        return '%s, %s' % (geonames[4].name, geonames[2].name)

    elif hasattr(root, 'address'):
        # http://www.geonames.org/maps/us-reverse-geocoder.html#findNearestAddress
        return '%s, %s' % (root.address.placename, root.address.adminName1)
    elif hasattr(root, 'country'):
        # http://www.geonames.org/export/web-services.html#countrysubdiv
        return root.countryName
    elif hasattr(root, 'ocean'):
        # http://www.geonames.org/export/web-services.html#ocean
        return root.ocean.name


def print_location(sat):
    name = sat.name
    if len(name) == 32:
        # It's probably been truncated
        name, _ = name.rsplit(' ', 1)
        name += '...'

    if isinstance(sat, EarthSatellite):
        lat = sat.sublat / math.pi * 180
        lng = (sat.sublong / math.pi * 180 + 180) % 360 - 180

        loc = revgeocode(lat, lng)

        location_msg = ' (%s)' % loc if loc else ''
        eclipsed_msg = ', eclipsed' if sat.eclipsed else ''

        if abs(datetime.utcnow() - sat._epoch.datetime()) > timedelta(seconds=3600):
            updated_msg = ' (updated %s)' % sat._epoch.datetime().strftime('%Y-%m-%d %H:%M')
        else:
            updated_msg = ''

        msg = '%s: %skm above %s,%s%s, distance %skm %skm/s, magnitude %s%s%s' % (
            name,
            int(round(sat.elevation / 1000)),
            round(lat, 3),
            round(lng, 3),
            location_msg,
            int(round(sat.range / 1000)),
            round(sat.range_velocity / 1000, 2),
            sat.mag,
            eclipsed_msg,
            updated_msg,
        )

    elif isinstance(sat, EllipticalBody):
        if math.isnan(sat.earth_distance):
            distance_msg = ''
        else:
            distance_msg = ', distance %skm' % int(round(sat.earth_distance * meters_per_au / 1000.0))

        if abs(datetime.utcnow() - sat._epoch_M.datetime()) > timedelta(seconds=3600):
            updated_msg = ' (updated %s)' % sat._epoch_M.datetime().strftime('%Y-%m-%d %H:%M')
        else:
            updated_msg = ''

        msg = '%s: %s, %s%s, magnitude %s%s' % (
            name,
            sat.ra,
            sat.dec,
            distance_msg,
            sat.mag,
            updated_msg,
        )

    print (msg.encode('utf-8'))


args = sys.argv[5:]

if args:
    body = ' '.join(args)
else:
    sys.exit(1)



sat = getbody(body)
#print (dir(sat))
sat.compute(lhs)
print_location(sat)

#for i in range(30):
#    lhs.date = '2014/5/2 17:39:%s' % i
#    sat.compute(lhs)
#    print_location(sat)


