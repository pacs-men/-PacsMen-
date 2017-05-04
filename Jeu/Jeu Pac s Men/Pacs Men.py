# -*- coding: utf-8 -*-
import Carte.carte as carte
import Carte.script as script
import pygame
from pygame.locals import *
import sys
import Carte.objet as objet
import combat.combat as combat
import pickle
import random
#sys.path.append()



black=(0,0,0)
white=(0xFF,0xFF,0xFF)

taille_fenetre=20
pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme Pygame de base')

mape = carte.carte(fichier = "carte.mp")
taille_carte = mape.taille_mat[0]
perso = objet.obj_boug(mape, 2, 2)

joueur = combat.AssassinsMagique()
personnage=joueur.img.convert_alpha()

ennemi= [combat.Aigles(),combat.Araingnees(),combat.Rats(),combat.Geant(),combat.Gobelins(),combat.Golems(),combat.Slime(),combat.Carapateur(),combat.Centaures(),combat.Loup_garou(),combat.Treant(),combat.Nains(),combat.Elfs()]
#choix de de l'ennemi
#e = random.randrange(0,12)
e = 4

#dialogues=script.script1(texte)
font = pygame.font.SysFont('Calibri', 25, True, False)

x=0
y=0
def affichercarte(x0,y0):
    for x in range(taille_fenetre):
        for y in range(taille_fenetre):
            fenetre.blit(mape.get_image_case(x+x0, y+y0),(x*32, y*32))

    for x in range(taille_fenetre):
        for y in range(taille_fenetre):
            if mape.matrice_objet[x+x0][y+y0] != None:
                fenetre.blit(mape.get_image_obj(x+x0, y+y0),(x*32, y*32))

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


continuer = 1

affichercarte(x,y)
#background_song.play()
pygame.key.set_repeat(300,70)

while continuer:
    # prise en compte des evenements
    #background_song.play()
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
                combat.affiche_combat(fenetre,joueur,ennemi[e])

            if event.key == K_s:
                for a in range (len(sc.ls_page)):
                    text = font.render(dialogues.ls_page[a],True,black)
                    fenetre.blit(text, [0,0])
                    pygame.display.flip()

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
