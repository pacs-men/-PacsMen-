# -*- coding: utf-8 -*-
import pygame
from pygame.locals import*

from cases import*
from carte import*
import sys
sys.path.append("..")
import combat.combat as combat
import subprocess

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
        self.image = pygame.image.load("data/perso.png").convert_alpha()
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
        self.stade_animation = 0
        self.inc = 0
    def avancer(self):
        if self.carte.est_marchable(self.posx+self.dict_dir[self.direction][0], self.posy+self.dict_dir[self.direction][1]) == True:
            if self.carte.obj_vide(self.posx+self.dict_dir[self.direction][0], self.posy+self.dict_dir[self.direction][1]) == True:  
            
                self.carte.deplacer((self.posx, self.posy), (self.posx+self.dict_dir[self.direction][0], self.posy+self.dict_dir[self.direction][1]))
                self.posx = self.posx+self.dict_dir[self.direction][0]
                self.posy = self.posy+self.dict_dir[self.direction][1]
                self.stade_animation = 1
            else:
                self.carte.matrice_objet[self.posx+self.dict_dir[self.direction][0]][self.posy+self.dict_dir[self.direction][1]].interagir()
    
    def ch_direction(self, direction):
        if direction in ["haut", "bas", "gauche", "droite"]:
            self.direction = direction
            #self.image = self.dict_images[self.direction]
            return True
        else:
            return False
            
    def step(self):
        if self.inc == 2:         
            if self.stade_animation !=0:
                if self.stade_animation == 8:
                    self.stade_animation = 0
                else:
                    self.stade_animation +=1
            self.inc = 0
        self.inc+=1
class arbre(objet):
     def __init__(self, carte, x, y):
         objet.__init__(self, carte, x, y)
         self.image = pygame.image.load("data/sprite_01.png")


class ennemi(obj_boug):
     def __init__(self, carte, x, y, ls_ennemi):
         objet.__init__(self, carte, x, y)
         self.ls_ennemi = ls_ennemi
         self.image = ls_ennemi[0].img

     def interagir(self):
         print("combat")
         self.carte.combat = [True, self]


class coffre(objet):
    def __init__(self, carte, x, y, contenu):
        objet.__init__(self, carte, x, y)
        self.contenu = contenu
        self.image_complet = pygame.image.load("data/chest2.png")
        self.image_fermee = self.image_complet.subsurface((0, 0, 32, 32))
        self.image_ouverte = self.image_complet.subsurface((32, 0, 32, 32))
        self.image = self.image_fermee
        
    def interagir(self):
        for potion in self.contenu:
            exec("self.carte.joueur."+potion+" += 1")
        self.contenu = []
        self.image = self.image_ouverte

class porte(objet):
    def __init__(self, carte, x, y):
        objet.__init__(self, carte, x, y)
        self.image = pygame.image.load("data/sprite_07.png")
    
    def interagir(self):
        self.effacer()
        
class porte_boss(objet):
    def __init__(self, carte, x, y):
        objet.__init__(self, carte, x, y)
        self.image = pygame.image.load("data/castledoors32.png")
    
    def interagir(self):
        self.carte.changer_carte()

class boss(obj_boug):
    def __init__(self, carte, x, y, ls_ennemi):
         objet.__init__(self, carte, x, y)
         self.ls_ennemi = ls_ennemi
         self.image = ls_ennemi[0].img

    def interagir(self):
         self.carte.combat = [True, self]


class coffre_boss(objet):
    def __init__(self, carte, x, y):
        objet.__init__(self, carte, x, y)
        self.image_complet = pygame.image.load("data/chest2.png")
        self.image_fermee = self.image_complet.subsurface((0, 0, 32, 32))
        self.image_ouverte = self.image_complet.subsurface((32, 0, 32, 32))
        self.image = self.image_fermee
    def interagir(self):        
        self.carte.joueur.upgrade(self.carte.niv_carte+1)
        self.image = self.image_ouverte


class Stalagmites(objet):
     def __init__(self, carte, x, y):
         objet.__init__(self, carte, x, y)
         self.image = pygame.image.load("data/sprite_00.png")

class pnj(objet):
     def __init__(self, carte, x, y):
         objet.__init__(self, carte, x, y)
         self.image = pygame.image.load("data/Sprite_RC.png")
     
     def interagir(self):
         subprocess.call("start python RC/ElProyectoRubiksCube.py")