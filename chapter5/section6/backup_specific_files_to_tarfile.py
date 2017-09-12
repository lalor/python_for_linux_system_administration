#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function
import os
import fnmatch
import tarfile
import datetime


def find_specific_files(root, patterns=['*'], exclude_dirs=[]):
    # 该函数的实现参考 5.3.4 节
    pass

def main():
    patterns= ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
    now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    filename = "all_images_{0}.tar.gz".format(now)
    with tarfile.open(filename, 'w:gz') as f:
        for item in find_specific_files(".", patterns):
            f.add(item)


if __name__ == '__main__':
    main()
