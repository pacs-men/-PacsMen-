# -*- coding: utf-8 -*-
"""
@author: nassim
"""
import pygame

pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme Pygame de base')

font = pygame.font.SysFont('Calibri', 25, False, False)
ecrire=font.render
black=(0,0,0)
white=(255,255,255)

coffre=pygame.image.load("data/chest2.png")

pvperso=ecrire("Pvhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhug:",True,white)
pvperso_rect=pvperso.get_rect()
#pvperso_rect.topright=(620,2)
pvperso_rect.right = 640
pvperso_rect.top = 30
fenetre.blit(pvperso,pvperso_rect)

while True:
	fenetre.blit(coffre,(0,0),(0,0,32,32))
	fenetre.blit(coffre,(64,64),(32,0,32,32))
	fenetre.blit(pvperso,pvperso_rect)
	pygame.display.flip()

