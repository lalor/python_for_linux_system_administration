#!/usr/bin/python
#-*- coding: UTF-8 -*-
import codecs

class Open(object):

    def __init__(self, filename, mode, encoding="utf-8"):
        self.fp = codecs.open(filename, mode, encoding)

    def __enter__(self):
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()


data = u"上下文管理器"
with Open('data.txt', 'w') as f:
    f.write(data)
