#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket, time

def sendMessage(message):
    print message
    return
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('172.31.24.101', 12345))
        s.send('%s' % message)
        s.close()
    except Exception, e:
        pass

n = 5

while True:
    if n == 5 and time.strftime('%H:%M:%S') == '23:59:55':
        sendMessage('5!')
        n = 4
    if n == 4 and time.strftime('%H:%M:%S') == '23:59:56':
        sendMessage('4!')
        n = 3
    if n == 3 and time.strftime('%H:%M:%S') == '23:59:57':
        sendMessage('3!')
        n = 2
    if n == 2 and time.strftime('%H:%M:%S') == '23:59:58':
        sendMessage('2!')
        n = 1
    if n == 1 and time.strftime('%H:%M:%S') == '23:59:59':
        sendMessage('1!')
        n = 0
    if n == 0 and time.strftime('%H:%M:%S') == '00:00:00':
        sendMessage('   。☆。*。☆。')
        sendMessage('  ★。＼｜／。★')
        sendMessage('* Happy New Year *')
        sendMessage('  ★。／｜＼。★')
        sendMessage('  。☆。*。☆。 *')
        sendMessage('     。★。*')
        break

    time.sleep(0.01)

