# -*- coding: utf-8 -*-
#! /usr/bin/python
import pygame
from pygame.locals import*

from cases import*
from objet import*

import random
import pickle
import sys
sys.path.append("..")
import combat.perso as perso


class carte:
    
    def __init__(self,  joueur):
        self.joueur = joueur
        self.mob_niv1 = [[perso.Rats, perso.Rats, perso.Rats, perso.Rats ],[ perso.Gobelins, perso.Gobelins, perso.Gobelins, perso.Gobelins],[perso.Aigles, perso.Aigles ],[ perso.Slime ], [perso.Carapateur]]
        self.mob_niv2 = [[perso.Centaures, perso.Centaures, perso.Centaures],[perso.Loup_garou],[perso.Araingnees,perso.Araingnees,perso.Araingnees], [perso.Carapateur],[perso.Golems,perso.Golems]]
        self.mob_niv3 = [[perso.Carapateur],[perso.Golems,perso.Golems],[perso.Treant],[perso.Geant],[perso.Nains,perso.Nains,perso.Nains],[perso.Elfs,perso.Elfs]]
        self.ls_ennemi = [self.mob_niv1, self.mob_niv2, self.mob_niv3]
        
        self.niv_carte = 0
        self.cartes = ["carte.mp", "carten2.mp", "carten3.mp"]       
        self.combat = [False]
        self.carte_changee = False
        self.fichier = self.cartes[self.niv_carte]
        self.recup_map()
        self.taille_mat = [len(self.matrice_case), len(self.matrice_case[0])]
         
        # création de la matrice qu sert au cases dde la carte
        self.dict_cases = {
                            "herbe1": herbe1(),
                            "herbe2": herbe2(),
                            "herbe3": herbe3(),
                            "herbe4": herbe4(),
                            "mur": mur(),
                            "murs": murs(),
                            "sols": sols(),
                            "trous":trous()
                          }
        #self.matrice_case = [[[] for a in range(self.taille_mat[1])] for a in range(self.taille_mat[0])]
        
        # création de la matrice qui sert gérer les objet de la scène
        #self.matrice_objet = [[None for a in range(self.taille_mat[1])] for a in range(self.taille_mat[0])]
        
        
    def recup_map(self):
        double_mat = []
        self.fichier = self.cartes[self.niv_carte]
        with open(self.fichier, "r") as fichier:
            pick = pickle.Unpickler(fichier)
            double_mat = pick.load()
        mat_case = double_mat[0]
        self.matrice_case = mat_case
        mat_objet = double_mat[1]
        
        for x in range(len(mat_case)):
            for y in range(len(mat_case[0])):
                if mat_case[x][y] == "herbe":
                    self.matrice_case[x][y] = "herbe"+str(random.randrange(1, 5))
        
        self.matrice_objet = [[None for a in range(len(mat_objet))] for a in range(len(mat_objet[0]))]
        
        for x in range(len(mat_objet)):
            for y in range(len(mat_objet[0])):
                if mat_objet[x][y] != "":
                    if mat_objet[x][y] == "ennemi":
                        e = random.randrange(len(self.ls_ennemi[self.niv_carte]))
                        ls_en = []
                        for a in self.ls_ennemi[self.niv_carte][e]:
                            ls_en.append(a())
                        self.matrice_objet[x][y] = ennemi(self, x, y, ls_en)
                    
                    elif mat_objet[x][y] == "coffre":
                        contenu = self.potions_aleatoires()
                        self.matrice_objet[x][y] = coffre(self, x, y, contenu)
                        
                    else:                        
                        exec("self.matrice_objet[x][y] = "+mat_objet[x][y]+"(self, x, y)")
                
    def changer_carte(self):
        self.niv_carte += 1 
        self.recup_map()
        self.carte_changee = True        
        
    def potions_aleatoires(self):
        ls_potions = [
            "potionvie1",
            "potionvie2",
            "potionvie3",
            "potionarmure1",
            "potionarmure2",
            "potionarmure3",
            "potionforce1",
            "potionforce2",
            "potionforce3",
            "potioncritique1",
            "potioncritique2",
            "potioncritique3",
            "potionvitesse",
            "potionprecision"]
            
        potions_renvoi = []
        
        for i in range(2):
            potions_renvoi.append(ls_potions[random.randrange(len(ls_potions))])
        
        return potions_renvoi
    def get_image_case(self, x, y):
        if x>=len(self.matrice_case):
            x = len(self.matrice_case)-1
        if y>=len(self.matrice_case[0]):
            y = len(self.matrice_case[0])-1
        return self.dict_cases[self.matrice_case[x][y]].image
        
    def get_image_obj(self, x, y):
        return self.matrice_objet[x][y].image
        
       
    def __repr__(self):
        ch = ""
        for x in range(self.taille_mat[0]):
            for y in range(self.taille_mat[1]):
                if self.matrice_objet[x][y] != None:
                    ch += self.matrice_objet[x][y].rep
                else:
                    ch += self.dict_cases[self.matrice_case[x][y]].rep
            ch += "\n"
        return ch 
        
    def placer_obj(self,objet, x, y):
        self.matrice_objet[x][y] = objet
        
    def effacer_obj(self, x, y):
        self.matrice_objet[x][y] = None
    def est_marchable(self, x, y):
        return self.dict_cases[self.matrice_case[x][y]].marchable
       
    def deplacer(self, (x1, y1), (x2, y2)):
        self.matrice_objet[x2][y2] = self.matrice_objet[x1][y1]
        self.matrice_objet[x1][y1] = None
        
    def obj_vide(self, x1, y1):
        if self.matrice_objet[x1][y1] == None:
            return True
        else:
            return False
        
        
if __name__ == "__main__":
    # exemple de fonctionnement de la carte et de objets
    print("")
    print("")
    print("")
    #sys.path.append("..")
    print sys.path
    dir(sys)
    a = carte("carte.mp")
    
    
    print a
    b = obj_boug(a, 5, 5)
    c = objet(a, 6, 5)
    b.ch_direction("bas")
    print a
