#!/usr/bin/python
#-*- coding: UTF-8 -*-
import codecs
from contextlib import contextmanager

@contextmanager
def Open(filename, mode, encoding='utf-8'):
    fp = codecs.open(filename, mode, encoding)
    try:
        yield fp
    finally:
        fp.close()

data = u"上下文管理器"
with Open('data.txt', 'w') as f:
    f.write(data)
