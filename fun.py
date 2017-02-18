#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(3))

def cal_sum(*args):
    sumx=0
    for n in args:
        sumx += n
    return sumx

print(cal_sum(1,2,3,4,5))

def lazy_sum(*args):
    def sumx():
        ax=0
        for n in args:
            ax += n
        return ax
    return sumx

f1=lazy_sum(1,3,5,7,9)

f2=lazy_sum(1,3,5,7,9)

print f1==f2
print f1()==f2()

def count():
    fs = []
    for i in range(1, 4):
        def f(i):
             return i*i
        fs.append(f(i))
    return fs

f1, f2, f3=count()
print f1,f2,f3

f=lambda x:x*x
print f(2)

def build(x,y):
    return lambda :x*x+y*y

f=build(3,4)
print f()