#!/usr/bin/env python

import sys
import serial
import requests

SERIAL_PORT = "/dev/tty.usbserial-A70064Mh"
SERIAL_BAUD = 9600

def usage():
    print 'Usage: %s url' % __file__
    sys.exit(1)

if __name__ == '__main__':
    try:
        url = sys.argv[1]
    except IndexError:
        usage()

    print 'Checking url:', url

    response = requests.get(url)

    print 'Got response code:', response.status_code

    s = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1)

    if response.status_code == 200:
        print 'Site is up.'
        s.write('1')
    else:
        print 'Site is DOWN!!!'
        s.write('0')

    s.close()

    print 'Done Checking.'


