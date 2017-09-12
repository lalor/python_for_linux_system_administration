#!/usr/bin/python
#-*- coding: UTF-8 -*-
import os
import fnmatch

def is_file_match(filename, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False

def find_specific_files(root, patterns=['*'], exclude_dirs=[]):
    for root, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if is_file_match(filename, patterns):
                yield os.path.join(root, filename)

        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)
