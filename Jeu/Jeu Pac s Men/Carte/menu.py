
import pygame
from pygame.locals import *
pygame.init()

#definition des couleurs
black=(0,0,0)
white=(0xFF,0xFF,0xFF)

#creation des variables pour ecrire un texte
font = pygame.font.SysFont('Calibri', 25, True, False)
ecrire = font.render

#creation de la vatiable permettant de dessiner des rectangles
dessiner=pygame.draw.rect


def start_menu(fenetre,joueur):
    fenetre.fill(white)
    position_bouton=0
    img_menu = pygame.image.load("data/imagemenu.jpg")
    text1 = ecrire(joueur[0].nom,True,black)
    text2 = ecrire(joueur[1].nom,True,black)
    text3 = ecrire(joueur[2].nom,True,black)
    text4 = ecrire(joueur[3].nom,True,black)
    text5 = ecrire(joueur[4].nom,True,black)
    text6 = ecrire(joueur[5].nom,True,black)
    
    fenetre.fill(white)
    while True:
        fenetre.blit(img_menu,[0,0])
        pygame.draw.rect(fenetre, black, [170, 227+64*position_bouton, 300, 64], 3)
        dessiner(fenetre, black, [170, 547, 300, 64], 1)
        dessiner(fenetre, black, [170, 483, 300, 64], 1)
        dessiner(fenetre, black, [170, 419, 300, 64], 1)
        dessiner(fenetre, black, [170, 355, 300, 64], 1)
        dessiner(fenetre, black, [170, 291, 300, 64], 1)
        dessiner(fenetre, black, [170, 227, 300, 64], 1)
        
        fenetre.blit(text6, text6.get_rect(center=(fenetre.get_width()/2, 579)))
        fenetre.blit(text5, text5.get_rect(center=(fenetre.get_width()/2, 515)))
        fenetre.blit(text4, text4.get_rect(center=(fenetre.get_width()/2, 451)))
        fenetre.blit(text3, text3.get_rect(center=(fenetre.get_width()/2, 387)))
        fenetre.blit(text2, text2.get_rect(center=(fenetre.get_width()/2, 323)))
        fenetre.blit(text1, text1.get_rect(center=(fenetre.get_width()/2, 259)))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return "End"
            if event.type == KEYDOWN:
                if event.key == K_DOWN or event.key == K_RIGHT:
                    if position_bouton <5:
                        position_bouton += 1
                if event.key == K_UP or event.key == K_LEFT:
                    if position_bouton >0:
                        position_bouton -= 1
                if event.key == K_RETURN:
                    if position_bouton == 0:
                        return 0
                    if position_bouton == 1:
                        return 1
                    if position_bouton == 2:
                        return 2
                    if position_bouton == 3:
                        return 3
                    if position_bouton == 4:
                        return 4
                    if position_bouton == 5:
                        return 5
        pygame.display.flip()