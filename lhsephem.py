#!/opt/irccat/irccat-commands/lhsephem-venv/bin/python
import ephem
from ordereddict import OrderedDict
from urllib import urlopen
from datetime import datetime
import lxml.html
import requests
import math
import callhorizons


def compass(angle):
  bearings = [
    'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
    'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW',
  ]
  sect = int(round(angle / (2 * math.pi) * len(bearings))) % len(bearings)
  return bearings[sect]


def chunk(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]


# For more see http://celestrak.com/NORAD/elements/
class TLESource(object):
    def __init__(self, url):
        self.url = url
        self.entries = None

    def __repr__(self):
        if self.entries is None:
            return '<TLESource %s>' % self.url
        else:
            return '<TLESource %s: %s entries>' % (self.url, len(self.entries))

    def load(self):
        f = urlopen(self.url)
        lines = [l.rstrip() for l in f.readlines()]
        self.entries = chunk(lines, 3)
        # TODO: cache these entries

    def __getitem__(self, name):
        if self.entries is None:
            self.load()
        for tle in self.entries:
            if tle[0].lower() == name.lower():
                return ephem.readtle(*tle)

        else:
            raise KeyError('%s not found in %s' % (name, repr(self)))


class SpaceTrackSource(object):
    url = 'https://www.space-track.org/basicspacedata/query/'
    authurl = 'https://www.space-track.org/ajaxauth/login'
    def __init__(self):
        self.authcookie = None

    def auth(self, query=None):
        params = {
            'identity': 'marksteward@gmail.com',
            'password': '9gO3HL0ajY8K9Pi1',
        }
        if query is not None:
            params['query'] = query
        response = requests.post(self.authurl, data=params)
        self.authcookie = response.cookies
        return response

    def load(self, name):
        # TODO: use the search, or download all TLEs and search as TLESource
        number = name # for now

        params = {
            'class': 'tle_latest',
            'NORAD_CAT_ID': number,
            'ORDINAL': 1,
            'format': 'tle', # or 3le, but update chunk call below
        }
        pred_vals = ['/'.join(map(str, p)) for p in params.items()]
        query_url = self.url + '/'.join(pred_vals)
        if self.authcookie is None:
            response = self.auth(query=query_url)
        else:
            response = requests.get(query_url, cookies=self.authcookie)

        lines = response.content.split('\n')
        self.entries = chunk(lines, 2)

    def __getitem__(self, name):
        self.load(name)
        if self.entries:
            tle = self.entries[0]
            return ephem.readtle(name, *tle)
        else:
            raise KeyError('%s not found')


def add_nl_to_brs(html):
    # nasty hack so I don't have to write a parser that splits by br's
    for br in html.xpath('*//br'):
        br.tail = '\n' + br.tail if br.tail else '\n'

class ZaryaSource(object):
    # Probably no use, as it only includes ellipse info, not mean anomaly
    url = 'http://www.zarya.info/Diaries/Launches/Launches.php'
    def __init__(self, year=None):
        self.year = year
        if self.year is None:
            self.year = datetime.now().year

    def load(self):
        response = requests.get(self.url, params={'year': self.year})
        root = lxml.html.document_fromstring(response.content)

        rows = root.xpath('//table[@id="orbitdata"]//tr[@class="bodyrow" or @class="bodyrowwhitesmall"]')
        for row in rows:
            add_nl_to_brs(row)
            tds = [td.text_content().strip() for td in row.xpath('td')]
            if row.attrib['class'] == 'bodyrow':
                parts = tds[0].split('\n') + [None, None]
                # id = international designator
                description, id, number = parts[:3]
                parts = [p.strip() for p in description.split(u'\xa0', 1)] + [None]
                body, full_name = parts[:2]
                print repr([body, full_name, id, number])
            elif tds[0].startswith('epoch'):
                continue
            elif tds[0].startswith('orbital parameters awaited'):
                continue
            else:
                epoch, semimajor, ecc, perigee, apogee, period, incl, omega, longitude, _ = tds

                # http://www.amsat.org/amsat/keps/kepmodel.html
                # http://www.lns.cornell.edu/~seb/celestia/orbital-parameters.html
                sat = pyephem.EarthSatellite()
                sat.name = body
                sat.catalog_number = number
                sat.full_name = full_name
                sat.id = id

                sat._epoch = datetime.strptime(epoch, '%Y %b %d, %H:%M')
                sat._inc = incl
                equatorial_radius = 6378.145
                #sat._raan = f1(perigee, apogee, semimajor, incl, omega, ecc, equatorialradius)
                sat._e = ecc
                sat._ap = omega          # angle of periapsis
                #sat._M = 0?              # mean anomaly
                sat._n = 60*24 / period  # mean motion
                sat._decay = 0
                sat._drag = 0
                sat._orbit = 0

                self.satellites[body] = sat

    def __getitem__(self, key):
        pass

class HorizonsSource(object):
    def __init__(self, epoch=None):
        if epoch is None:
            epoch = datetime.now()
        self.epoch = epoch
        self.satellites = {}

    def load(self):
        pass

    def __getitem__(self, name):
        if name not in self.satellites:
            q = callhorizons.query(name, smallbody=False)
            q.set_discreteepochs(ephem.julian_date(self.epoch))
            try:
                sats = q.export2pyephem()
            except ValueError as e:
                if e.message.startswith('Unknown target'):
                    raise KeyError('%s not found in %s' % (name, repr(self)))
                raise

            self.satellites[name] = sats[0]

        return self.satellites[name]

def getbody(body):

    sources = OrderedDict([
        ('celestrak-stations', TLESource('http://celestrak.com/NORAD/elements/stations.txt')),
        ('celestrak-recent',   TLESource('http://celestrak.com/NORAD/elements/tle-new.txt')),
#        ('celestrak-gps',      TLESource('http://celestrak.com/NORAD/elements/supplemental/gps.txt')),
#        ('celestrak-visual',   TLESource('http://celestrak.com/NORAD/elements/visual.txt')),
#        ('celestrak-weather',  TLESource('http://celestrak.com/NORAD/elements/weather.txt')),
        ('kepler',             TLESource('http://mstl.atl.calpoly.edu/~ops/keps/kepler.txt')),
#        ('zarya',              ZaryaSource()),
        ('horizons',           HorizonsSource()),
    ])

    aliases = {
        'iss': 'ISS (ZARYA)',
        'dragon': '39680',
        'kicksat': '39685',
    }
    aliases = dict((k.lower(), v) for k, v in aliases.items())
    body = aliases.get(body.lower(), body)

    known_sources = {
        'ISS (ZARYA)': 'celestrak-stations',
    }
    known_sources = dict((k.lower(), v) for k, v in known_sources.items())

    sourcelist = list(sources)

    # TODO: check epoch if there are multiple, and take the one we're nearest to

    # TODO: maybe split this up into identifying the catalog numbers, and then downloading TLEs
    # http://www.celestrak.com/NORAD/elements/master.asp

    if body.isdigit():
        # Assume it's a catalog number
        # Space Track is slow, but good data
        sourcelist.insert(0, 'spacetrack')
        sources['spacetrack'] = SpaceTrackSource()
    else:
        try:
            source = known_sources[body]
            sourcelist.remove(source)
            sourcelist.insert(0, source)
        except KeyError, e:
            pass

    for source in sourcelist:
        source = sources[source]
        try:
            sat = source[body]
        except KeyError, e:
            continue
        else:
            # TODO: cache source
            return sat

    else:
        raise KeyError('TLE entry not found')


lhs = ephem.Observer()
lhs.lat = '51.5322'
lhs.long = '-0.0606'
# base from http://www.daftlogic.com/sandbox-google-maps-find-altitude.htm
lhs.elevation = 22 # +- 2m

