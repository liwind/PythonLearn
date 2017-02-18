#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def cmp_ignore_case(s1, s2):
    u1 = s1.lower()
    u2 = s2.lower()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

