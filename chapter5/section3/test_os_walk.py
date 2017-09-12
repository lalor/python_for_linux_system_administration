#!/usr/bin/python
#-*- coding: UTF-8 -*-
import os
import fnmatch

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []

for root, dirnames, filenames in os.walk(os.path.expanduser("~lmx/t")):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))

print(matches)
