# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 22:19:54 2017

@author: Emeric Coudeville
"""
import pygame
from pygame.locals import*

from carte import*
from objet import*

class case:
    def __init__(self):
        self.type = "case"
        self.marchable = True
        self.ouvrable = False
        self.chemin_image = ""
        self.rep = " "
        self.image = None
    
    def load_image(self):
        self.image = pygame.image.load(self.chemin_image)
        
    def __repr__(self):
        if self.dessus == None:
            return self.rep
        else:    
            return self.dessus.rep
        
    def __str__(self):
        return "case de type {} a la position {} \n marchable = {} ouvrable = {} l'image ce trouve en {}".format(
        self.type, self.pos, self.marchable, self.ouvrable, self.image)
        
class herbe(case):
    def __init__(self):
      case.__init__(self)
      self.type = "herbe"
      self.rep = "H"
      self.chemin_image = "Data/herbe.png"
      self.load_image()
      
      
class mur(case):
    def __init__(self):
      case.__init__(self)
      self.type = "mur"
      self.marchable = False
      self.rep = "M"
      self.chemin_image = "Data/Mur.png"
      self.load_image()