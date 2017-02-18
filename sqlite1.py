#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : sqlite1.py
# @Author   : Feng
# @Date     : 2017/2/17

import sqlite3

conn = sqlite3.connect('test.db')
curs = conn.cursor()
sql = 'select * from user'
curs.execute(sql)
values = curs.fetchall()
print values
curs.close()
conn.close()
