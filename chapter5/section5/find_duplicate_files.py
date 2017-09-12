#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function
import hashlib
import sys
import os
import fnmatch

CHUNK_SIZE = 8192

def find_specific_files(root, patterns=['*'], exclude_dirs=[]):
    # 该函数的实现参考 5.3.4 节
    pass

def get_chunk(filename):
    with open(filename) as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            else:
                yield chunk

def get_file_checksum(filename):
    h = hashlib.md5()
    for chunk in get_chunk(filename):
        h.update(chunk)
    return h.hexdigest()

def main():
    sys.argv.append("")
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        raise SystemExit("{0} is not a directory".format(directory))

    record = {}
    for item in find_specific_files(directory):
        checksum = get_file_checksum(item)
        if checksum in record:
            print('find duplicate file: {0} vs {1}'.format(record[checksum], item))
        else:
            record[checksum] = item

if __name__ == '__main__':
    main()
