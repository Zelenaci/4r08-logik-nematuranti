#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:10:21 2019

@author: lov35174
"""

from os.path import basename, splitext
import tkinter as tk
from tkinter import Canvas, Label
import random
# from tkinter import ttk


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = 'Foo'

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.barvy = "#c90000 #99dd00 #0000ff #ffff00 #008888 #880088 #dd9900 #ffffff".split()
        self.sirka = 30
        self.vyska = 20
        self.aktradek = 9
        self.had=None
        self.pokus=[None]*5
        
        #skrytá pole
        self.skryteBarvy = []
        for sloupec in range(5):
            c = Canvas(self, background='black', width=self.sirka, height=self.vyska)
            c.grid(column=sloupec,row=0)
            self.skryteBarvy.append(c)
            
        ### titulek
        self.lbltit = Label(self, text=u"Logik")
        self.lbltit.grid(columnspan=5, row=1)
        
        self.lblbp = Label(self, text=u"Barva/Pozice")
        self.lblbp.grid(columnspan=3, row=1, column=6)
        
        #pole s hádanou barvou
        self.hadaneBarvy = []
        for radek in range(10):
            radekBarev = []
            for sloupec in range(5):
                c = Canvas(self, background='light grey', width=self.sirka, height=self.vyska)
                c.grid(column=sloupec,row=radek+2)
                radekBarev.append(c)
            self.hadaneBarvy.append(radekBarev)
        
        #odpověď programu
        self.odpovedProgramu = []
        for radek in range(10):
            lbl = Label(self, text='-/-')
            lbl.grid(column=7, row= radek+2)
            self.odpovedProgramu.append(lbl)
            
        #oddělovací čára
        self.cancar = Canvas( background='black',width=6*self.sirka, height=8)
        self.cancar.grid(column=0,row=12, columnspan=5)
        
        #tlačítka
        for radek, barva in enumerate(self.barvy):
            for sloupec in range(5):
                def akce(r=radek, s=sloupec):
                    self.click(r, s)
                b = tk.Button(width=self.sirka, height=self.vyska, bg=barva, fg=barva, bitmap='gray12', activebackground=barva, activeforeground=barva, command=akce)
                b.grid(row=radek+13,column=sloupec)
        
        #tlačítko Nová Hra
        self.tlchra = tk.Button(self, text=u'Nová hra', command=self.generujHadanku)
        self.tlchra.grid(row=13, column=6, columnspan=4)
        
        #tlačítko Odeslat
        self.tlcodes = tk.Button(self, text=u'Odeslat', command=self.odeslat)
        self.tlcodes.grid(row=14, column=6, columnspan=4)
    
        #tlačítko znovu
        self.tlznov = tk.Button(self,text = 'Znovu', command=None)
        self.tlznov.grid(column= 6,row=15, columnspan = 4 )
    
        self.bind("<Escape>",self.quit)
        
    def click(self, r, s):
        self.hadaneBarvy[self.aktradek][s].config(bg=self.barvy[r])
        print(r, s)

        
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
