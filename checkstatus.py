#!/usr/bin/env python

import sys
import serial
import requests

SERIAL_PORT = "/dev/tty.usbserial-A70064Mh"
SERIAL_BAUD = 9600

def usage():
    print 'Usage: %s url1 [url2] [url3] ...' % __file__
    sys.exit(1)

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        usage()

    s = serial.Serial(SERIAL_PORT, SERIAL_BAUD, timeout=1)
    any_down = False 

    for url in sys.argv[1:]:
        print '=' * 80
        print 'Checking url:', url

        try:
            response = requests.get(url)
        except:
            print 'Got exception. Site is down!'
            any_down = True
            break

        print 'Got response code:', response.status_code

        if response.status_code != 200:
            print 'Site is DOWN!!!'
            any_down = True
            break
        else:
            print 'Site is up.'

    if any_down:
        s.write('0')
    else:
        s.write('1')

    s.close()

    print 'Done Checking.'


