# -*- coding: utf-8 -*-
"""
Created on Mon May 01 20:26:04 2017

@author: nassim
"""
import pygame
import combat.combat as combat

pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme Pygame de base')

joueur = combat.Mage()
ennemi = [combat.Elfs(), combat.Nains()]

combat.affiche_combat(fenetre,joueur,ennemi)
pygame.display.flip()