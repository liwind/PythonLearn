#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Tkinter import *

root = Tk()

list=["C", "python", "php", "html", 'SQL']
movie=['CSS', 'jQuery']
listbox1=Listbox(root)
listbox2=Listbox(root)

for item in list:
	listbox1.insert(0, item)
	
for item in movie:
	listbox2.insert(0, item)
	
listbox1.pack()
listbox2.pack()
root.mainloop()