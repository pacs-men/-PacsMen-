# -*- coding: utf-8 -*-
import Carte.carte as carte
import Carte.script as script
#import Carte.inventaire as inventaire
import combat.perso as perso
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
mvt_perso = objet.obj_boug(mape, 2, 2)

#creation d'une liste contenant tous les personnages jouable
joueur = [perso.AssassinsMagique(),perso.AssassinsPhysique(),perso.Combattant(),perso.Mage(),perso.Soigneur(),perso.Archer()]
j=0
personnage=joueur[j].img.convert()

#liste de tous les ennemis
ennemi= [perso.Aigles(),perso.Araingnees(),perso.Rats(),perso.Geant(),perso.Gobelins(),perso.Golems(),perso.Slime(),perso.Carapateur(),perso.Centaures(),perso.Loup_garou(),perso.Treant(),perso.Nains(),perso.Elfs()]

#choix de de l'ennemi
e = random.randrange(0,12)
ennemi_combat=[]
for a in range (3): 
    ennemi_combat.append(ennemi[e])

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
    
#fonction pour l'affichage du menu de depart
def start_menu(fenetre):
    fenetre.fill(white)
    img_menu = pygame.image.load("data/imagemenu")
    fenetre.blit(img_menu,[0,0])
    text1 = font.render(joueur[0].nom,True,black)
    text2 = font.render(joueur[1].nom,True,black)
    text3 = font.render(joueur[2].nom,True,black)
    text4 = font.render(joueur[3].nom,True,black)
    text5 = font.render(joueur[4].nom,True,black)
    text6 = font.render(joueur[5].nom,True,black)
    fenetre.blit(text1, )
    

    
    

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
                if mvt_perso.direction != "bas":
                    mvt_perso.ch_direction("bas")
                else:
                    mvt_perso.avancer()
            if event.key == K_UP:
                if mvt_perso.direction != "haut":
                    mvt_perso.ch_direction("haut")
                else:
                    mvt_perso.avancer()
            if event.key == K_LEFT:
                if mvt_perso.direction != "gauche":
                    mvt_perso.ch_direction("gauche")
                else:
                    mvt_perso.avancer()
            if event.key == K_RIGHT:
                if mvt_perso.direction != "droite":
                    mvt_perso.ch_direction("droite")
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
                 inventaire.inventaire

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
    #fenetre.blit(personnage, [i, j])
    pygame.display.flip()
