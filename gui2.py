#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : gui2.py
# @Author   : Feng
# @Date     : 2017/2/17

from Tkinter import *
import tkMessageBox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('hello world')

app.mainloop()
