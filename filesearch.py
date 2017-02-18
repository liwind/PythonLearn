#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : filesearch.py
# @Author   : Feng
# @Date     : 2017/2/15


import os


def searchfile(s, l, cpath):
    for fp in os.listdir(cpath):
        if os.path.isfile(fp):
            if fp.find(s) > -1:
                l.append(fp)
        if os.path.isdir(fp):
            npath = os.path.join(cpath, fp)
            searchfile(s, l, npath)

def search(s):
    l = []
    cpath = os.getcwd()
    searchfile(s, l, cpath)
    print l

search('fi')