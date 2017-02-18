#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket

soc=socket.socket()
host=socket.gethostname()
port=3154
soc.connect((host, port))
print soc.recv(1024)
soc.close()