#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# __author__  =  "ffadmin"
import sys
def format_log(txt):
    with open(txt,'r') as f:
        Wlist = f.readlines()
        for r in Wlist:
            if '2017-' in r:
                count = r.split(' ')[2].split('(')[1]
                if '2017-' in r and float(count)<2:
                    print Wlist[Wlist.index(r) - 1],
                    print r,

if __name__ == '__main__':
    format_log(sys.argv[1])

