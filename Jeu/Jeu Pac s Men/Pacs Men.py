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




pygame.key.set_repeat(300,70)

#declanchement de la musique
pygame.mixer.music.load('data/Linconnue V4 Pont.wav')
pygame.mixer.music.play(-1)

continuer = True

joueur=menu.start_menu(fenetre,joueur)

def affichercarte(x0,y0):
    for x in range(taille_fenetre):
        for y in range(taille_fenetre):
            fenetre.blit(mape.get_image_case(x+x0, y+y0),(x*32, y*32))

    for x in range(taille_fenetre):
        for y in range(taille_fenetre):
            if mape.matrice_objet[x+x0][y+y0] != None:
                fenetre.blit(mape.get_image_obj(x+x0, y+y0),(x*32, y*32))
    affiche_pv(joueur,fenetre)

def affiche_pv(joueur,fenetre):
    prct_pv=(joueur.pv/joueur.pv_max)*100
    dessiner(fenetre,black,(9,9,102,12),1)
    dessiner(fenetre,red,(10,10,prct_pv,10))
    fenetre.blit(ecrire(str(joueur.pv)+"/"+str(joueur.pv_max),True,black),(120,10))
    
               
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
    mvt_perso = objet.perso(mape, 2, 2, joueur.ls_imagedir)
    script_pa.script_pa(fenetre)
    pygame.mixer.music.load('data/compo 1.wav')
    pygame.mixer.music.play(-1)



while continuer:
    # prise en compte des evenements
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                if mvt_perso.direction != "bas":
                    mvt_perso.ch_direction("bas")
                    mvt_perso.avancer()
                else:
                    mvt_perso.avancer()
            if event.key == K_UP:
                if mvt_perso.direction != "haut":
                    mvt_perso.ch_direction("haut")
                    mvt_perso.avancer()
                else:
                    mvt_perso.avancer()
            if event.key == K_LEFT:
                if mvt_perso.direction != "gauche":
                    mvt_perso.ch_direction("gauche")
                    mvt_perso.avancer()
                else:
                    mvt_perso.avancer()
            if event.key == K_RIGHT:
                if mvt_perso.direction != "droite":
                    mvt_perso.ch_direction("droite")
                    mvt_perso.avancer()
                else:
                    mvt_perso.avancer()


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
        mvt_perso = objet.perso(mape, 2, 2, joueur.ls_imagedir)
        mape.carte_changee = False       
    
    # affichage
    if mvt_perso.posx<10:
        x0 = 0
    elif mvt_perso.posx>=taille_carte-11:
        x0 = taille_carte-20
    else:
        x0 = mvt_perso.posx-10

    if mvt_perso.posy<10:
        y0 = 0
    elif mvt_perso.posy>=taille_carte-11:
        y0 = taille_carte-20

    else:
        y0 = mvt_perso.posy-10
    affichercarte(x0,y0)
    pygame.display.flip()
    
pygame.quit()
