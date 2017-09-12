#!/usr/bin/python
#-*-coding: UTF-8 -*-
from __future__ import print_function

d = {}
with open('access.log') as f:
    for line in f:
        key = line.split()[8]
        d.setdefault(key, 0)
        d[key] += 1

sum_requests= 0
error_requests= 0

for key, val in d.iteritems():
    if int(key) >= 400:
        error_requests+= val
    sum_requests+= val

print('error rate: {0:.2f}%'.format(error_requests * 100.0 / sum_requests))
