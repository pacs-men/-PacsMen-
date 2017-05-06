# -*- coding: utf-8 -*-
import Carte.carte as carte
import Carte.script as script
import Carte.inventaire as inventaire
import combat.perso as perso
import Carte.menu as menu
import pygame
from pygame.locals import *
import sys
import Carte.objet as objet
import combat.combat as combat
import pickle
import random
#sys.path.append()

#definition des couleurs
black=(0,0,0)
white=(0xFF,0xFF,0xFF)

#initialisation de la fenetre
taille_fenetre=20
pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme Pygame de base')

#creation de la carte et initialisation du deplacement
mape = carte.carte(fichier = "carte.mp")
taille_carte = mape.taille_mat[0]
mvt_perso = objet.perso(mape, 2, 3)

#creation d'une liste contenant tous les personnages jouable
joueur = [perso.AssassinsMagique(),perso.AssassinsPhysique(),perso.Combattant(),perso.Mage(),perso.Soigneur(),perso.Archer()]

#liste de tous les ennemis
ennemi= [perso.Aigles(),perso.Araingnees(),perso.Rats(),perso.Geant(),perso.Gobelins(),perso.Golems(),perso.Slime(),perso.Carapateur(),perso.Centaures(),perso.Loup_garou(),perso.Treant(),perso.Nains(),perso.Elfs()]

#choix de de l'ennemi
e = random.randrange(0,12)
ennemi_combat=[]
for a in range (3): 
    ennemi_combat.append(ennemi[e])

#creation des variables pour ecrire un texte
font = pygame.font.SysFont('Calibri', 25, True, False)
ecrire = font.render

#creation de la vatiable permettant de dessiner des rectangles
dessiner=pygame.draw.rect

#initialisations de quelques variables utiles
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
    

affichercarte(x,y)
pygame.key.set_repeat(300,70)

j=menu.start_menu(fenetre,joueur)
if j == "End":
    sys.exit(0)
personnage=joueur[j].img.convert()

while True:
    # prise en compte des evenements
    for event in pygame.event.get():
        if event.type == QUIT:
            break
            
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

            if event.key == K_TAB:
                combat.affiche_combat(fenetre,joueur[j],ennemi_combat)

            if event.key == K_s:
                for a in range (len(sc.ls_page)):
                    text = font.render(dialogues.ls_page[a],True,black)
                    fenetre.blit(text, [0,0])
                    pygame.display.flip()
            
            if event.key == K_i:
                 inventaire.inventaire(fenetre,joueur[j])

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
