# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:24:09 2017

@author: nassim.zaki
"""
import pygame
from pygame.locals import *
import sys
sys.path.append("../combat")
import combat 
pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme Pygame de base')
Joueur = combat.AssassinsMagique()


def inventaire(fenetre,Joueur):
    continuer = 1
    font = pygame.font.SysFont('Calibri', 25, True, False)
    black=(0,0,0)
    blanc=(0xFF, 0xFF, 0xFF)
    position_bouton = 1
    while continuer == 1:
        if position_bouton == 1:
            pygame.draw.rect(fenetre, blanc, [210, 590, 190, 50], 3)
            pygame.draw.rect(fenetre, blanc, [100, 590, 110, 50], 3)
            pygame.draw.rect(fenetre, black, [0, 590, 100, 50], 3)
        if position_bouton == 2:
            pygame.draw.rect(fenetre, blanc, [0, 590, 100, 50], 3)
            pygame.draw.rect(fenetre, blanc, [210, 590, 190, 50], 3)
            pygame.draw.rect(fenetre, black, [100, 590, 110, 50], 3)
        if position_bouton == 3:
            pygame.draw.rect(fenetre, blanc, [100, 590, 110, 50], 3)
            pygame.draw.rect(fenetre, blanc, [0, 590, 100, 50], 3)
            pygame.draw.rect(fenetre, black, [210, 590, 190, 50], 3)
        text1 = font.render("attaque",True,black)
        text2 =font.render("potion",True,black)
        text3 =font.render("fuite",True,black)
        print Joueur.potionvie1
        pygame.display.flip()
pygame.display.flip()                
inventaire(fenetre,Joueur)