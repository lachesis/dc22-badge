#!/usr/bin/python2
import sys
if len(sys.argv) < 3:
    print 'Usage: {} <dump.raw> <dump.binary>'
    print 'Convert a raw dump file to a binary file.'
    sys.exit(1)

with open(sys.argv[1], 'r') as inp:
    data = []
    lastAddr = 0
    on = False
    for line in inp:
        if 'start' in line:
            on = True
        if not on: continue

        try:
            addr, b = line.split('-')
            addr = int(addr)
            b = int(b)
        except: continue

        if addr != lastAddr:
            raise Exception("Skipped a byte! addr: {}, lastAddr: {}".format(addr, lastAddr))
        
        if int(b) > 255 or b < 0:
            raise Exception("Byte {} out of range!".format(b))

        # Actually append the data :)
        data.append(chr(b))
        lastAddr += 1

        if 'end' in line:
            on = False

    print "Read {} bytes from raw file".format(len(data))

    l = len(data)
    for i in xrange(len(data)-1, 0, -1):
        if data[i] != chr(255):
            l = i
            break

    data = data[:l]
    print "Trimmed to {} bytes.".format(l)

    with open(sys.argv[2], 'wb') as out:
        for d in data:
            out.write(d)
        print "Wrote to {}".format(sys.argv[2])
