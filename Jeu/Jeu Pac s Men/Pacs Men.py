# -*- coding: utf-8 -*-
#! /usr/bin/python

import pygame
pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme Pygame de base')

import Carte.carte as carte
import Carte.script as script
import Carte.inventaire as inventaire
import combat.perso as perso
import Carte.menu as menu

from pygame.locals import *
import sys
import Carte.objet as objet
import Carte.scriptpa as script_pa
import combat.combat as combat
import pickle
import random
#sys.path.append()

#definition des couleurs
black=(0,0,0)
white=(0xFF,0xFF,0xFF)
red=(255,0,0)

#initialisation de la fenetre
taille_fenetre=20


#creation d'une liste contenant tous les personnages jouable
joueur = [perso.AssassinsMagique,perso.AssassinsPhysique,perso.Combattant,perso.Mage,perso.Soigneur,perso.Archer]

#creation des variables pour ecrire un texte
font = pygame.font.SysFont('Calibri', 25, True, False)
ecrire = font.render

#creation de la vatiable permettant de dessiner des rectangles
dessiner=pygame.draw.rect

#initialisations de quelques variables utiles
x=0
y=0


dict_fleche = {K_DOWN: "bas", K_UP:"haut", K_RIGHT:"droite", K_LEFT:"gauche"}

pygame.key.set_repeat(300,70)

#declanchement de la musique
pygame.mixer.music.load('data/Linconnue V4 Pont.wav')
pygame.mixer.music.play(-1)

continuer = True

joueur=menu.start_menu(fenetre,joueur)

def affichercarte(x0,y0, xmvt, ymvt):

    for x in range(-1, taille_fenetre+1):
        for y in range(-1, taille_fenetre+1):
            if xmvt:
                posx = (x+mvt_perso.dict_dir[mvt_perso.direction][0])*32 -mvt_perso.dict_dir[mvt_perso.direction][0]*4*mvt_perso.stade_animation
            else:
                posx = x*32
            if ymvt:
                posy = (y+mvt_perso.dict_dir[mvt_perso.direction][1])*32 -mvt_perso.dict_dir[mvt_perso.direction][1]*4*mvt_perso.stade_animation
            else:
                posy = y*32
            fenetre.blit(mape.get_image_case(x+x0, y+y0),(posx, posy))
            
            if x+x0>= len(mape.matrice_objet):
                x=x-1
            if y+y0>= len(mape.matrice_objet[0]):
                y=y-1

            if mape.matrice_objet[x+x0][y+y0]!= None and mape.matrice_objet[x+x0][y+y0] != mvt_perso:
                fenetre.blit(mape.get_image_obj(x+x0, y+y0),(posx, posy))

def afficher_joueur(x0, y0, xmvt, ymvt):
    if mvt_perso.stade_animation!= 0:
        if not xmvt: 
            imgx = (32*(mvt_perso.posx-mvt_perso.dict_dir[mvt_perso.direction][0]-x0))+(4*mvt_perso.dict_dir[mvt_perso.direction][0]*mvt_perso.stade_animation)-16
        else:
            imgx = (32*(mvt_perso.posx-x0))-16
        if not ymvt: 
            imgy = (32*(mvt_perso.posy-mvt_perso.dict_dir[mvt_perso.direction][1]-y0))+(4*mvt_perso.dict_dir[mvt_perso.direction][1]*mvt_perso.stade_animation)-32
        else:
            imgy = (32*(mvt_perso.posy-y0))-32
    else:
        imgx = (32*(mvt_perso.posx-x0))-16
        imgy = (32*(mvt_perso.posy-y0))-32

    fenetre.blit(mvt_perso.dict_images[mvt_perso.direction][mvt_perso.stade_animation],(imgx, imgy))


    
def affiche_pv(joueur,fenetre):
    prct_pv=(joueur.pv/joueur.pv_max)*100
    dessiner(fenetre,black,(9,9,102,12),1)
    dessiner(fenetre,red,(10,10,prct_pv,10))
    fenetre.blit(ecrire(str(joueur.pv)+"/"+str(joueur.pv_max),True,black),(120,10))
   
def afficher_ecran():
# affichage
    x_mvt_carte = True    
    y_mvt_carte = True
    
    if mvt_perso.posx<10:
        x0 = 0
    elif mvt_perso.posx>=taille_carte-11:
        x0 = taille_carte-20
        x_mvt_carte = False
    else:
        x0 = mvt_perso.posx-10

    if mvt_perso.posy<10:
        y0 = 0
        y_mvt_carte = False
    elif mvt_perso.posy>=taille_carte-11:
        y0 = taille_carte-20
        y_mvt_carte = False
    else:
        y0 = mvt_perso.posy-10
    
    if mvt_perso.stade_animation == 0:
        x_mvt_carte = False    
        y_mvt_carte = False
    
    if mvt_perso.posx<11:
        x_mvt_carte = False    
    if mvt_perso.posx>=taille_carte-9:
        x_mvt_carte = False    
    if mvt_perso.posy<11:
        y_mvt_carte = False    
    if mvt_perso.posy>=taille_carte-9:
        y_mvt_carte = False    
    
    
    affichercarte(x0,y0, x_mvt_carte, y_mvt_carte)
    afficher_joueur(x0, y0, x_mvt_carte, y_mvt_carte)               
    affiche_pv(joueur,fenetre)

def ouvrir_map():
    carte = ""
    with open("carte.mp", "rb") as fichier:
        depick = pickle.Unpickler(fichier)
        carte = depick.load()

    for x in range(len(carte)):
        for y in range(len(carte)):
            if carte[x][y] == "Herbe":
                carte[x][y]+= str(random.randrange(1, 5))
    return carte

#creation de la carte et initialisation du deplacement
mape = carte.carte("carte.mp", joueur)
taille_carte = mape.taille_mat[0]


if joueur == "End":
    continuer = False
else:
    mvt_perso = objet.perso(mape, 2, 2, joueur.ls_images)
    script_pa.script_pa(fenetre)
    pygame.mixer.music.load('data/compo 1.wav')
    pygame.mixer.music.play(-1)

direction_sauvegardee= ""

while continuer:
    # prise en compte des evenements
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            
        if event.type == KEYDOWN:
            if mvt_perso.stade_animation == 0:
                if event.key in [K_DOWN, K_UP, K_LEFT, K_RIGHT]:
                                        
                    if mvt_perso.direction != dict_fleche[event.key]:
                        mvt_perso.ch_direction(dict_fleche[event.key])
                        mvt_perso.avancer()
                    else:
                        mvt_perso.avancer()
                elif direction_sauvegardee in [K_DOWN, K_UP, K_LEFT, K_RIGHT]:
                    if mvt_perso.direction != dict_fleche[direction_sauvegardee]:
                        mvt_perso.ch_direction(dict_fleche[direction_sauvegardee])
                        mvt_perso.avancer()
                    else:
                        mvt_perso.avancer()
                    
            else:
                if event.key in [K_DOWN, K_UP, K_LEFT, K_RIGHT]:
                    direction_sauvegardee = event.key

                                 
            if event.key == K_ESCAPE:
                info = menu.menupause(fenetre,joueur)
                if info == "End":
                    continuer = False
                if info != None:
                    j=info

            if event.key == K_s:
                for a in range (len(sc.ls_page)):
                    text = font.render(dialogues.ls_page[a],True,black)
                    fenetre.blit(text, [0,0])
                    pygame.display.flip()
            
            if event.key == K_i:
                 inventaire.inventaire(fenetre,joueur)
                 
    #Decleclenchement du combat
    if mape.combat[0] == True:
        a = combat.affiche_combat(fenetre,joueur, mape.combat[1].ls_ennemi)
        if a == "fin":
            print mape.combat[1]
            
            mape.combat[1].effacer()
        elif a == "Fuite":
            pass
        elif a == "Joueur mort joueur":
            print("Afficher Mort A faire")
        mape.combat = [False]
        
    if mape.carte_changee:
        print mape.matrice_case
        mvt_perso = objet.perso(mape, 2, 2, joueur.ls_images)
        mape.carte_changee = False       
    
    
    afficher_ecran()
    pygame.display.flip()
    mvt_perso.step()
pygame.quit()
