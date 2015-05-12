#!/usr/bin/env python
import requests
import sys

tools = {
    (1, '3-in-1 lathe/mill'):
        ['3in1', '3-in-1', '3 in 1', 'three in one', 'three-in-one'],
    (2, 'Old laser cutter'):
        ['oldlasercutter', 'old lasercutter'],
    (3, 'Lulzbot'):
        ['lulz', 'lulz bot'],
    (4, 'Biohacking Lab'):
        ['biohackers', 'biolab'],
    (5, 'Laser cutter'):
        ['laser', 'lasercutter'],
    (6, 'TIG welder'):
        ['tig'],
    (7, 'Shapeoko'):
        ['shapeoko2', 'shapeoko 2'],
    (8, 'CNC'):
        [],
}

tool = ' '.join(sys.argv[5:])
for (tool_id, tool_name), synonyms in tools.items():
    if tool.lower() in synonyms + [tool_name.lower()]:
        break

else:
    sys.exit(1)

response = requests.get('http://acserver:1234/%s/status' % tool_id)
status = response.content
if status == '1':
    response2 = requests.get('http://acserver:1234/%s/is_tool_in_use' % tool_id)
    inuse = response2.content
    if inuse == 'yes':
        print '%s in service and currently in use' % tool_name
    elif inuse == 'no':
        print '%s in service, but not currently in use' % tool_name

elif status == '0':
    print '%s out of service' % tool_name

