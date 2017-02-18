#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket

soc = socket.socket()
host = socket.gethostname()
port = 3154
soc.bind((host, port))
soc.listen(5)
while True:
	con, adder=soc.accept()
	print('address: ', adder)
	con.send('welcome')
	con.close()
	
