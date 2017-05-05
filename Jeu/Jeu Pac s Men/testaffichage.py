# -*- coding: utf-8 -*-
"""
Created on Mon May 01 20:26:04 2017

@author: nassim
"""
import pygame
import combat.combat as combat
import combat.perso as perso

pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme Pygame de base')

joueur = perso.Mage()
ennemi = [perso.Elfs(), perso.Nains()]

combat.affiche_combat(fenetre,joueur,ennemi)
pygame.display.flip()