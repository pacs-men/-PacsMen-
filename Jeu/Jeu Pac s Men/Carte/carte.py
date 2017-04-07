# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 22:22:10 2017

@author: Emeric Coudeville
"""
import pygame
from pygame.locals import*

from cases import*
import objet

class carte:
    
    def __init__(self, taille_mat):
        
        self.taille_mat = [taille_mat, taille_mat]
        # création de la matrice qui sert au cases dde la carte
        self.dict_cases = {
                            "herbe": herbe(),
                            "mur": mur()
                           }             
        self.matrice_case = [[[] for a in range(self.taille_mat[1])] for a in range(self.taille_mat[0])]
        self.remplir_mat_cases()
        
        # création de la matrice qui sert gérer les objet de la scène
        self.matrice_objet = [[None for a in range(self.taille_mat[1])] for a in range(self.taille_mat[0])]
        
        
    def remplir_mat_cases(self):
        for x in range(self.taille_mat[0]):
            for y in range(self.taille_mat[1]):
                self.matrice_case[x][y] = "herbe"
                
                
        for x in range(self.taille_mat[0]):
            self.matrice_case[x][0] = "mur"
            self.matrice_case[x][self.taille_mat[0]-1] = "mur"
            
        for y in range(self.taille_mat[1]):
            self.matrice_case[0][y] = "mur"
            self.matrice_case[self.taille_mat[1]-1][y] = "mur"
                
    def get_image_case(self, x, y):
        return self.dict_cases[self.matrice_case[x][y]].image
        
       
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
        
        
if __name__ == "__main__":
    
    a = carte(10)
    print a
    b = objet.objet(a, 5, 5)
    
    print a.matrice_objet
    print a
    
    
    
    
    
    
    
    
    
    
    