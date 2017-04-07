# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 11:38:52 2017

@author: nassim.zaki
"""

import pygame

from pygame.locals import *


pygame.init()


#Ouverture de la fenêtre Pygame

fenetre = pygame.display.set_mode((640, 480))


#Chargement et collage du fond

fond = pygame.image.load("data/herbe.png").convert()

fenetre.blit(fond, (0,0))


#Rafraîchissement de l'écran

pygame.display.flip()


#BOUCLE INFINIE

continuer = 1

while continuer:

    continuer = int(input())