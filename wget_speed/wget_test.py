#! /usr/bin/env python2.6
#  -*- coding: utf-8 -*-
# __author__  =  "ffadmin"


import commands
import time

wget_list = \
    [
    '101.227.17.92:55336/live/c2_mon/speed.test',
    '101.227.12.9/speed.test',
    '101.227.201.66/speed.test ',


    ]
def enter(f):
    def enter1():
        with open('wget_log.txt','a') as f1:
            f1.writelines('\n\n')
        return f
    return  enter1()
@enter
def wget_count():
    for i in wget_list:
        wget_res = commands.getoutput('wget %s -O /dev/null'%i)
        d = \
'%s\n' \
'%s'%(wget_res.split('\n')[0].split(' ')[3],wget_res.split('\n')[-2])
        with open('wget_log.txt','a') as f:
            f.writelines('%s\n'%(d))





if __name__ == "__main__":
    wget_count()

