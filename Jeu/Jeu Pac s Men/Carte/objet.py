# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 22:19:57 2017

@author: Emeric Coudeville
"""

import pygame
from pygame.locals import*

from cases import*
from carte import*

class objet:
    def __init__(self, carte, x, y):
        if carte.matrice_objet[x][y] == None:
            self.carte = carte
            carte.placer_obj(self, x, y)
            self.posx = x
            self.poxy = y
            self.rep = "X"
        else:
            return "nn"
                
class obj_boug(objet):
    def __init__(self, carte, x, y):
        objet.__init__(self, carte, x, y)
        self.direction = "gauche"
        self.dict_dir = {"gauche":(-1, 0), "droite":(1, 0), "haut":(0, -1), "bas":(0, 1)}
    
    def ch_direction(self, direction):
        self.direction = direction
        
    def avancer(self):
        pass
    