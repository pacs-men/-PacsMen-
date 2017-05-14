# -*- coding: utf-8 -*-
"""
@author: nassim
"""
import pygame
from pygame.locals import *
import combat.perso as perso

pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme Pygame de base')
joueur=perso.Archer()

font = pygame.font.SysFont('Calibri', 25, False, False)
ecrire=font.render
black=(0,0,0)
white=(255,255,255)
p=0 

coffre=pygame.image.load("data/chest2.png")

pvperso=ecrire("Pvhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhug:",True,white)
pvperso_rect=pvperso.get_rect()
#pvperso_rect.topright=(620,2)
pvperso_rect.right = 640
pvperso_rect.top = 30
fenetre.blit(pvperso,pvperso_rect)
img = pygame.image.load("data/Martin/complet.png")

k=0
i=1
dict_image={}
dict_image1={}
dict_image2={}
dict_image3={}
for b in range (0,448,64):
    dict_image[i]=img.subsurface(b,0,64,64)
    dict_image1[i]=img.subsurface(b,64,64,64)
    dict_image2[i]=img.subsurface(b,128,64,64)
    dict_image3[i]=img.subsurface(b,192,64,64)
    i+=1

def anim_joueur(fenetre,joueur,p):
    imganim = joueur.img_combat
    fenetre.fill(white,(150,250,64,64))
    fenetre.blit(imganim,(150,250),(64*p,64*19,64,64))
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            break
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                p+=1
                anim_joueur(fenetre,joueur,p)
    if p<12:
        p+=1
        anim_joueur(fenetre,joueur,p)
    else:
        p=0
    k+=1
    fenetre.fill(white,(500,200,64,64))
    fenetre.blit(dict_image[k],(500,200))
    fenetre.fill(white,(550,100,64,64))
    fenetre.blit(dict_image1[k],(550,100))
    fenetre.fill(white,(300,250,64,64))
    fenetre.blit(dict_image2[k],(300,250))
    fenetre.fill(white,(310,320,64,64))
    fenetre.blit(dict_image3[k],(310,320))
    if k ==5:
        k=0
    anim_joueur(fenetre,joueur,p)
    fenetre.blit(coffre,(0,0),(0,0,32,32))
    fenetre.blit(coffre,(64,64),(32,0,32,32))
    fenetre.blit(pvperso,pvperso_rect)
    pygame.time.wait(100)
    pygame.display.flip()

#fenetre.blit(img,(150,250),(1280,64,64,64))
