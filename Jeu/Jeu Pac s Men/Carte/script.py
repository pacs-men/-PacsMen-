# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 22:38:18 2017

@author: nassim
"""

class script1:
    def __init__(self,fenetre):
        fenetre.fill((255,255,255))
        self.texte = "bla bla bla bla bla"
        self.mots1 = page1().texte
        self.surface = ""

    def page1(self):
        self.nom = "Script1"
        self.page = "Page1"
        self.texte = "test de la page 1"

    def page2(self):
        self.nom = "Script1"
        self.page = "Page2"
        self.texte = "bla bla bla bla bla"

    def page3(self):
        self.nom = "Script1"
        self.page = "Page3"
        self.texte = "bla bla bla bla bla"

    def page4(self):
        self.nom = "Script1"
        self.page = "Page4"
        self.texte = "bla bla bla bla bla"