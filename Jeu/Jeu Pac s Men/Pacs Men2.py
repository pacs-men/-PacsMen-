# -*- coding: utf-8 -*-
import Carte.carte as carte
import Carte.script as script
import Carte.inventaire as inventaire
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
jaune=(255, 255, 153)

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

#liste de tous les ennemis
ennemi= [perso.Aigles(),perso.Araingnees(),perso.Rats(),perso.Geant(),perso.Gobelins(),perso.Golems(),perso.Slime(),perso.Carapateur(),perso.Centaures(),perso.Loup_garou(),perso.Treant(),perso.Nains(),perso.Elfs()]

#choix de de l'ennemi
e = random.randrange(0,12)
ennemi_combat=[]
for a in range (3): 
    ennemi_combat.append(ennemi[e])

#dialogues=script.script1(texte)

#creation des variables pour ecrire un texte
font = pygame.font.SysFont('Calibri', 25, True, False)
ecrire = font.render

#creation de la vatiable permettant de dessiner des rectangles
dessiner=pygame.draw.rect

#initialisations de quelques variables utiles
x=0
y=0
boucle = 1

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
    global j, boucle
    fenetre.fill(white)
    position_bouton=0
    img_menu = pygame.image.load("data/imagemenu.jpg")
    fenetre.blit(img_menu,[0,0])
    
    dessiner(fenetre, black, [170, 547, 300, 64], 1)
    dessiner(fenetre, black, [170, 483, 300, 64], 1)
    dessiner(fenetre, black, [170, 419, 300, 64], 1)
    dessiner(fenetre, black, [170, 355, 300, 64], 1)
    dessiner(fenetre, black, [170, 291, 300, 64], 1)
    dessiner(fenetre, black, [170, 227, 300, 64], 1)
    
    while boucle == 1:
        pygame.draw.rect(fenetre, white, [170, 227+64*(position_bouton-1), 300, 64], 3)
        pygame.draw.rect(fenetre, white, [170, 227+64*(position_bouton+1), 300, 64], 3)
        pygame.draw.rect(fenetre, black, [170, 227+64*position_bouton, 300, 64], 3)
        
        text1 = ecrire(joueur[0].nom,True,black)
        text2 = ecrire(joueur[1].nom,True,black)
        text3 = ecrire(joueur[2].nom,True,black)
        text4 = ecrire(joueur[3].nom,True,black)
        text5 = ecrire(joueur[4].nom,True,black)
        text6 = ecrire(joueur[5].nom,True,black)
        
        fenetre.blit(text6, text6.get_rect(center=(fenetre.get_width()/2, 579)))
        fenetre.blit(text5, text5.get_rect(center=(fenetre.get_width()/2, 515)))
        fenetre.blit(text4, text4.get_rect(center=(fenetre.get_width()/2, 451)))
        fenetre.blit(text3, text3.get_rect(center=(fenetre.get_width()/2, 387)))
        fenetre.blit(text2, text2.get_rect(center=(fenetre.get_width()/2, 323)))
        fenetre.blit(text1, text1.get_rect(center=(fenetre.get_width()/2, 259)))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                boucle = 0
            if event.type == KEYDOWN:
                if event.key == K_DOWN or event.key == K_RIGHT:
                    if position_bouton <5:
                        position_bouton += 1
                if event.key == K_UP or event.key == K_LEFT:
                    if position_bouton >0:
                        position_bouton -= 1
                if event.key == K_RETURN:
                    if position_bouton == 0:
                        j = 0
                        boucle = 0
                    if position_bouton == 1:
                        j = 1
                        boucle = 0
                    if position_bouton == 2:
                        j = 2
                        boucle = 0
                    if position_bouton == 3:
                        j = 3
                        boucle = 0
                    if position_bouton == 4:
                        j = 4
                        boucle = 0
                    if position_bouton == 5:
                        j = 5
                        boucle = 0    
        pygame.display.flip()
        
def menupause(fenetre):
    fenetre.fill(jaune)
    position_bouton = 0
    pause = 1
    grandtitre=pygame.font.Font('data/fonts/old_london/OldLondon.ttf',55)

    dessiner(fenetre, black, [170, 379, 300, 64], 1) 
    dessiner(fenetre, black, [170, 463, 300, 64], 1)    
    dessiner(fenetre, black, [170, 547, 300, 64], 1)

    while pause == 1:
#        pygame.draw.rect(fenetre, white, [170, 227+64*(position_bouton-1), 300, 64], 3)
#        pygame.draw.rect(fenetre, white, [170, 227+64*(position_bouton+1), 300, 64], 3)
#        pygame.draw.rect(fenetre, black, [170, 227+64*position_bouton, 300, 64], 3)
        titre1=grandtitre.render("MENU PAUSE", True, black)
        fenetre.blit(titre1, titre1.get_rect(center=(fenetre.get_width()/2, 60)))
        text1 = ecrire("Reprendre",True,black)
        text2 = ecrire("Menu Principal",True,black)
        text3 = ecrire("Retour au Bureau",True,black)
        
        fenetre.blit(text1, text1.get_rect(center=(fenetre.get_width()/2, 411)))
        fenetre.blit(text2, text2.get_rect(center=(fenetre.get_width()/2, 485)))
        fenetre.blit(text3, text3.get_rect(center=(fenetre.get_width()/2, 387)))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pause = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause = 0
                if event.key == K_DOWN or event.key == K_RIGHT:
                    pass
        pygame.display.flip()
        
        

continuer = 1
affichercarte(x,y)
#background_song.play()
pygame.key.set_repeat(300,70)

while continuer:
    # prise en compte des evenements
    #background_song.play()
    start_menu(fenetre)
    personnage=joueur[j].img.convert()
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
                 inventaire.inventaire(fenetre,joueur[j])
            
            if event.key == K_ESCAPE:
                menupause(fenetre)

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
