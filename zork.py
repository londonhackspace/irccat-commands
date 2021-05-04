#!/usr/bin/env python

import sys
import time
import re
import subprocess

output_path = '/usr/share/irccat/zork_input.dat'   #file of input for zork
input_path = '/usr/share/irccat/zork_output.dat' #file of output from zork


def write_command(path, data):
    with open(path, 'w') as f:
        f.write(data+'\r')

def get_response(path):
    with open(path, 'r') as f:
        data = f.read()

    data = data.split('>')

    response = data[-2].split('\r')[1:]    
    return response

def sanitize(data):
    #print (repr(data))
    sections = data.split('\x1b[m')
    data = sections[-1]
    data = re.sub('\x1b\[[0-9]+;[0-9]+H', ' ', data)
    p = subprocess.Popen(["teseq|grep '^-\?|'|reseq - -"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    #p = subprocess.Popen(["teseq"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    (out, err) = p.communicate(input=data)
    return out


if len(sys.argv) > 5:
    term = ' '.join(sys.argv[5:])

    if term.lower() in ('y', 'yes'):
        term = 'no'

    if term.lower() not in ('exit', 'quit', 'restart'):
        write_command(output_path, term)

        time.sleep(1)
        response = get_response(input_path)
        print (sanitize(' '.join(response)).rstrip())
