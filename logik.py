#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:10:21 2019

@author: lov35174
"""

from os.path import basename, splitext
import tkinter as tk
from tkinter import Canvas, Label
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
        
        #skrytá pole
        self.skryteBarvy = []
        for sloupec in range(5):
            c = Canvas(self, background='black', width=self.sirka, height=self.vyska)
            c.grid(column=sloupec,row=0)
            self.skryteBarvy.append(c)
            
        ### titulek
        self.lbltit = Label(self, text=u"Logik")
        self.lbltit.grid(row = 1,column = 1,columnspan=5)
        
        self.lblskore = Label(self, text=u"Barva/Pozice")
        self.lblskore.grid(row = 1,column = 6,columnspan=5)
        
        #pole s hádanou barvou
        self.hadaneBarvy = []
        for radek in range(10):
            radekBarev = []
            for sloupec in range(5):
                c = Canvas(self, background='light grey', width=self.sirka, height=self.vyska)
                c.grid(column=sloupec,row=radek+2)
                radekBarev.append(c)
            self.hadaneBarvy.append(radekBarev)
        self.hadaneBarvy[1][4].config(background='magenta')
        
        #odpověď programu
        odpovedProgramu = []
        for radek in range(10):
            lbl = Label(self, text='-/-')
            lbl.grid(column=8, row= radek+2)
            odpovedProgramu.append(lbl)
            
        #oddělovací čára
        self.cancar = Canvas( background='#777',width=6*self.sirka, height=8)
        self.cancar.grid(column=0,row=12, columnspan=5)
        
        #tlačítka
        for radek, barva in enumerate(self.barvy):
            for sloupec in range(5):
                def akce(r=radek, s=sloupec):
                    self.click(r, s)
                self.b = tk.Button(width=self.sirka, height=self.vyska, bg=barva, fg=barva, bitmap='gray12', activebackground=barva, activeforeground=barva, command=akce)
                self.b.grid(row=radek+12,column=sloupec)
                
        #tlačítko Odeslat
        self.tlcodes = tk.Button(self, text=u'Odeslat')
        self.tlcodes.grid(row=13, column=6, columnspan=4)
    
        self.bind("<Escape>",self.quit)
        
    def click(self, r, s):
        self.hadaneBarvy[self.aktradek][s].config(bg=self.barvy[r])
        print(r, s)
        
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
