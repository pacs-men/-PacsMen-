# -*- coding: utf-8 -*-
"""
@author: nassim
"""
import pygame

pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme Pygame de base')

coffre=pygame.image.load("data/chest2.png")
while True:
	fenetre.blit(coffre,(0,0),(0,0,32,32))
	fenetre.blit(coffre,(64,64),(32,0,32,32))
	pygame.display.flip()

