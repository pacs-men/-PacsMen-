# -*- coding: utf-8 -*-
import carte_test
import pygame
from pygame.locals import *
import sys
sys.path.append("C:/Users/nassim/Documents/GitHub/Unfaithful-Spaghetti/Jeu Pac s Men/combat")
import combat


#==============================================================================
# map=cases.carte(10)
# map.matrice[x][y].afficher(i, j)
#==============================================================================




D=20
taille_carte = 30
pygame.init()
fenetre=pygame.display.set_mode((640,640), RESIZABLE)
pygame.display.set_caption('Programme Pygame de base')

mape= carte_test.carte(taille_carte)
x=0
y=0
def affichercarte(x0,y0):
    for x in range(D):
        for y in range(D):
            fenetre.blit(mape.get_image_case(x+x0, y+y0),(x*32, y*32))

#def perso(i,j):
#    self.image = pygame.image.load("Data/personnage").convert_alpha()

imgJoueur = combat.AssassinsMagique()
personnage=imgJoueur.img

background_song=pygame.mixer.Sound("song1.ogg")

continuer = 1
player_position = pygame.mouse.get_pos()

while continuer:
    affichercarte(x,y)

    i = player_position[0]
    j = player_position[1]
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        tkey=pygame.key.get_pressed()
        if tkey[K_LEFT]:
            i -= 32
            if x>0:
                x-=1
            affichercarte(x,y)
            pygame.display.update()
        elif tkey[K_RIGHT]:
            i += 32
            if x<taille_carte-D:
                x+=1
            affichercarte(x,y)
            pygame.display.update()
        elif tkey[K_UP]:
            j += 32
            if y>0:
                y-=1
            affichercarte(x,y)
            pygame.display.update()
        elif tkey[K_DOWN]:#On descend le perso
            j -= 32
            if y<taille_carte-D:
                y+=1
            affichercarte(x,y)
            pygame.display.update()

    fenetre.blit(personnage, [i, j])
    background_song.play()
    pygame.display.flip()
#==============================================================================
# def haut():
#     global x,y
#     y+=2
#     draw(x,y)
#
# def bas():
#     global x,y
#     y-=2
#     draw(x,y)
#
# def droite():
#     global x,y
#     x-=2
#     draw(x,y)
#
# def gauche():
#     global x,y
#     x+=2
#     draw(x,y)
#
# def draw(x,y):
#     global carte
#     carte.delete(ALL)
#
# for event in pygame.event.get():
# 	if event.type == QUIT:
# 		return
# 	elif event.type == KEYDOWN:
# 		if event.key == K_UP:
# 			haut()
# 		if event.key == K_DOWN:
# 			bas()
# 	elif event.type == KEYUP:
# 		if event.key == K_UP or event.key == K_DOWN:
#	player.movepos = [0,0]
#			player.state = "still"
# continuer = 1
#
#
# while continuer:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             continuer = 0
#==============================================================================

