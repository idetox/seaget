#!/usr/bin/python2
# clean rewrite and combination of all my old python scripts
# TODO:
# - get basic functions []
# - add advances functions like:
#       looking for password at address $foo
#       write to buffer/memory
#       search for password without dumping
#       add devices with known address

import argparse
try:
    import serial
except:
    print 'You have to install pyserial'
    quit()
import sys,os,re,time

class SeaGet():
    debug=0

    def send():
        pass

    def __init__(self,baud, cont, dumptype, filename, device, new_baud=False):
        ser = serial.Serial(port=device, baudrate=baud, bytesize=8,parity='N',stopbits=1,timeout=0.1)
        #set right diagnostic mode
        ser.write("\x1A\n")

    def read_buffer():
        pass
        
    def read_memory():
        pass

    def dump_buffer():
        pass
        
    def dump_memory():
        pass

def main():
    parser = argparse.ArgumentParser(description='Dump memory/buffer of a seagate hd using a serial connection.')
    parser.add_argument('--dumptype', metavar='memory/buffer', nargs=1, default='memory', help='What gets dumped')
    parser.add_argument('--baud', metavar=38400, default=38400, help='current baud rate [38400,115200]')
    parser.add_argument('--new-baud', metavar=115200, default=115200, help='set new baud rate [38400,115200]')
    parser.add_argument('-c', dest='cont', action='store_const', const=True, help='Continue dump')
    parser.add_argument('--device', metavar='/dev/ttyUSB0', default='/dev/ttyUSB0', help='the serial device you use')
    parser.add_argument('filename', metavar='dumpfile', help='the name of the dump file, duh')
    args = parser.parse_args()
    see = SeaGet(args.baud, args.cont, args.dumptype, args.filename, args.device, args.new_baud)

if __name__ == '__main__':
    main()
