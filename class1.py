#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : class1.py
# @Author   : Feng
# @Date     : 2017/2/15

import types
import logging

class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def __str__(self):
        return 'Student object (name: %s)' % self.__name

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

li=Student('li',80)
feng=Student('feng',85)
test=Student('test', 999)

class Animal:
    def run(self):
        print 'animal'

    def run_twice(self):
        self.run()
        self.run()

class Dog(Animal):
    def run(self):
        print 'dog'

class Cat(Animal):
    def run(self):
        print 'cat'


a=Animal()
d=Dog()

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

    def __getitem__(self, n):
        a, b = 1,1
        for x in range(n):
            a, b = b, a+b
        return a

f=Fib()
logging.basicConfig(level=logging.INFO)
print f[5]
