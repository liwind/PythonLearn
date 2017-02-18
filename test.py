#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fn(x, y):
    return x * 10 + y


dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def chartonum(str):
    return dic[str]


l0 = reduce(fn, map(chartonum, '13579'))
print l0 + 1

print 'eg1'
l1 = ['adam', 'LISA', 'barT']


def reg(str):
    return (str.lower()).capitalize()


print map(reg, l1)

def prod(x, y):
    return x*y

print reduce(prod, [1,2,3,4])
