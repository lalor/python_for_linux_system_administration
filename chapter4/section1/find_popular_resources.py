#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function
from collections import Counter

c = Counter()
with open('access.log') as f:
    for line in f:
        c[line.split()[6]] += 1

print("Popular resources : {0}".format(c.most_common(10)))
