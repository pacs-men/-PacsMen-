# -*- coding: utf-8 -*-
import pygame
from pygame.locals import*

from cases import*
from carte import*
import sys
sys.path.append("..")
import combat.combat as combat


class objet:
    def __init__(self, carte, x, y):
        if carte.matrice_objet[x][y] == None and carte.matrice_case[x][y]:
            self.carte = carte
            carte.placer_obj(self, x, y)
            self.posx = x
            self.posy = y
            self.rep = "X"
        else:
            self.carte = None
            self.posx = 0
            self.posy = 0
            self.rep = "X"
    
    def interagir(self):
        pass
    def effacer(self):
        self.carte.effacer_obj(self.posx, self.posy)
                
class obj_boug(objet):
    def __init__(self, carte, x, y):
        objet.__init__(self, carte, x, y)
        self.direction = "gauche"
        self.dict_dir = {"gauche":(-1, 0), "droite":(1, 0), "haut":(0, -1), "bas":(0, 1)}
        self.image = pygame.image.load("data/perso.png")
        
    def ch_direction(self, direction):
        if direction in ["haut", "bas", "gauche", "droite"]:
            self.direction = direction
            return True
        else:
            return False
        
    def avancer(self):
        if self.carte.est_marchable(self.posx+self.dict_dir[self.direction][0], self.posy+self.dict_dir[self.direction][1]) == True:
            if self.carte.obj_vide(self.posx+self.dict_dir[self.direction][0], self.posy+self.dict_dir[self.direction][1]) == True:  
            
                self.carte.deplacer((self.posx, self.posy), (self.posx+self.dict_dir[self.direction][0], self.posy+self.dict_dir[self.direction][1]))
                self.posx = self.posx+self.dict_dir[self.direction][0]
                self.posy = self.posy+self.dict_dir[self.direction][1]
                


class perso(obj_boug):
    def __init__(self, carte, x, y, images):
        obj_boug.__init__(self, carte , x, y)
        self.dict_images = {"gauche": images[0],"droite": images[1],"haut":images[2],"bas":images[3]}

    def avancer(self):
        if self.carte.est_marchable(self.posx+self.dict_dir[self.direction][0], self.posy+self.dict_dir[self.direction][1]) == True:
            if self.carte.obj_vide(self.posx+self.dict_dir[self.direction][0], self.posy+self.dict_dir[self.direction][1]) == True:  
            
                self.carte.deplacer((self.posx, self.posy), (self.posx+self.dict_dir[self.direction][0], self.posy+self.dict_dir[self.direction][1]))
                self.posx = self.posx+self.dict_dir[self.direction][0]
                self.posy = self.posy+self.dict_dir[self.direction][1]
            else:
                self.carte.matrice_objet[self.posx+self.dict_dir[self.direction][0]][self.posy+self.dict_dir[self.direction][1]].interagir()
    
    def ch_direction(self, direction):
        if direction in ["haut", "bas", "gauche", "droite"]:
            self.direction = direction
            self.image = self.dict_images[self.direction]
            return True
        else:
            return False
    
class arbre(objet):
     def __init__(self, carte, x, y):
         objet.__init__(self, carte, x, y)
         self.image = pygame.image.load("data/sprite_01.png")

class ennemi(obj_boug):
     def __init__(self, carte, x, y, num, image):
         objet.__init__(self, carte, x, y)
         self.image = image
         self.num = num

     def interagir(self):
         print("combat")
         self.carte.combat = [True, self]
