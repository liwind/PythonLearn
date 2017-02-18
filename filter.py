#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def is_odd(n):
    return n % 2 == 1


print filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def not_empty(s):
    return s and s.strip()

print filter(not_empty, ['a', 'b', None, 'c', ''])

def is_pri(num):
    if num==1:
        return False
    for x in range(2, num+1):
        if num%x==0:
            return x!=num

print filter(is_pri, range(1, 101))