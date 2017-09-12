#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function

ips = []
with open('access.log') as f:
    for line in f:
        ips.append(line.split()[0])

print("PV is {0}".format(len(ips)))
print("UV is {0}".format(len(set(ips))))
