# -*- coding: utf-8 -*-
import carte
import pygame
from pygame.locals import *
import sys
import objet
sys.path.append("../combat")
import combat


#==============================================================================
# map=cases.carte(10)
# map.matrice[x][y].afficher(i, j)
#==============================================================================




D=20
taille_carte = 30
pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme Pygame de base')

mape= carte.carte(taille_carte)
perso = objet.obj_boug(mape, 10,10)

imgJoueur = combat.AssassinsMagique()
personnage=imgJoueur.img.convert_alpha()
x=0
y=0
def affichercarte(x0,y0):
    for x in range(D):
        for y in range(D):
            fenetre.blit(mape.get_image_case(x+x0, y+y0),(x*32, y*32))

    for x in range(D):
        for y in range(D):
            if mape.matrice_objet[x+x0][y+y0] != None:
                fenetre.blit(personnage,(x*32, y*32))

#def perso(i,j):
#    self.image = pygame.image.load("Data/personnage").convert_alpha()




background_song=pygame.mixer.Sound("Data/laser5.ogg")

continuer = 1
player_position = [5, 5]

affichercarte(x,y)
background_song.play()
pygame.key.set_repeat(300,70)

#i = player_position[0]
#j = player_position[1]

while continuer:
    # prise en compte des evenements
    background_song.play()
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                if perso.direction != "bas":
                    perso.ch_direction("bas")
                else:
                    perso.avancer()
            if event.key == K_UP:
                if perso.direction != "haut":
                    perso.ch_direction("haut")
                else:
                    perso.avancer()
            if event.key == K_LEFT:
                if perso.direction != "gauche":
                    perso.ch_direction("gauche")
                else:
                    perso.avancer()
            if event.key == K_RIGHT:
                if perso.direction != "droite":
                    perso.ch_direction("droite")
                else:
                    perso.avancer()

            if event.key == K_TAB:
                combat.affiche_combat(fenetre)
        '''
         tkey = pygame.key.get_pressed()
        if tkey[K_LEFT]:
            i -= 32
            if x>0:
                x-=1
            affichercarte(x,y)
            #pygame.display.update()
        elif tkey[K_RIGHT]:
            i += 32
            if x<taille_carte-D:
                x+=1
            affichercarte(x,y)
            #pygame.display.update()
        elif tkey[K_UP]:
            j += 32
            if y>0:
                y-=1
            affichercarte(x,y)
            #pygame.display.update()
        elif tkey[K_DOWN]:#On descend le perso
            j -= 32
            if y<taille_carte-D:
                y+=1
            affichercarte(x,y)
            #pygame.display.update()'''

    # affichage
    if perso.posx<10:
        x0 = 0
    elif perso.posx>=taille_carte-11:
        x0 = taille_carte-20
    else:
        x0 = perso.posx-10

    if perso.posy<10:
        y0 = 0
    elif perso.posy>=taille_carte-11:
        y0 = taille_carte-20

    else:
        y0 = perso.posy-10
    affichercarte(x0,y0)
    #fenetre.blit(personnage, [i, j])
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
