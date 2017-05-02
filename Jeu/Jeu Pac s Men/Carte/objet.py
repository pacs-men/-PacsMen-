import pygame
from pygame.locals import*

from cases import*
from carte import*

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
                
class obj_boug(objet):
    def __init__(self, carte, x, y):
        objet.__init__(self, carte, x, y)
        self.direction = "gauche"
        self.dict_dir = {"gauche":(-1, 0), "droite":(1, 0), "haut":(0, -1), "bas":(0, 1)}
    
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
    def __init__(self, carte, x, y):
        obj_boug.__init__(self, carte , x, y)
        self.dict_images = {"gauche":pygame.image.load(""),"droite":pygame.image.load(""),"haut":pygame.image.load(""),"bas":pygame.image.load("") }

class arbre(objet):
     def __init__(self, carte, x, y):
         objet.__init__(self, carte, x, y)
         self.image = pygame.image.load("sprite_01")
