
import pygame
from pygame.locals import *
pygame.init()

#definition des couleurs
black=(0,0,0)
white=(0xFF,0xFF,0xFF)
jaune=(255, 255, 153)

#creation des variables pour ecrire un texte
font = pygame.font.SysFont('Calibri', 25, True, False)
ecrire = font.render

#creation de la vatiable permettant de dessiner des rectangles
dessiner=pygame.draw.rect


def start_menu(fenetre,joueur):
    
    #pygame.mixer.music.load('data/01 - Where Do The Children Play.mp3')
    #pygame.mixer.music.play(-1)
    fenetre.fill(white)
    position_bouton=0
    img_menu = pygame.image.load("data/imagemenu.jpg")
    text1 = ecrire("Sebastien"+" "+"Assassin Magique",True,black)
    text2 = ecrire("Nassim"+" "+"Assassin Physique",True,black)
    text3 = ecrire("Pierre Antoine"+" "+"Combattant",True,black)
    text4 = ecrire("Emeric"+" "+"Mage",True,black)
    text5 = ecrire("Clarisse"+" "+"Soigneur",True,black)
    text6 = ecrire("Martin"+" "+"Archer",True,black)
    
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
                        pygame.mixer.music.load('data/01 - Chanson Pour l Auvergnat.mp3')
                        #pygame.mixer.music.play(-1)
                        return joueur[0]()
                    if position_bouton == 1:
                        pygame.mixer.music.load('data/01 - Chanson Pour l Auvergnat.mp3')
                        #pygame.mixer.music.play(-1)
                        return joueur[1]()
                    if position_bouton == 2:
                        pygame.mixer.music.load('data/01 - Chanson Pour l Auvergnat.mp3')
                        #pygame.mixer.music.play(-1)
                        return joueur[2]()
                    if position_bouton == 3:
                        pygame.mixer.music.load('data/01 - Chanson Pour l Auvergnat.mp3')
                        #pygame.mixer.music.play(-1)
                        return joueur[3]()
                    if position_bouton == 4:
                        pygame.mixer.music.load('data/01 - Chanson Pour l Auvergnat.mp3')
                        #pygame.mixer.music.play(-1)
                        return joueur[4]()
                    if position_bouton == 5:
                        pygame.mixer.music.load('data/01 - Chanson Pour l Auvergnat.mp3')
                        #pygame.mixer.music.play(-1)
                        return joueur[5]()
        pygame.display.flip()
    pygame.mixer.music.load('data/01 - Chanson Pour l Auvergnat.mp3')
    #pygame.mixer.music.play(-1)

def menupause(fenetre,joueur):
    #pygame.mixer.music.stop()
    position_bouton = 0
    grandtitre=pygame.font.Font('data/fonts/old_london/OldLondon.ttf',55)
    text1 = ecrire("Reprendre",True,black)
    text2 = ecrire("Menu Principal",True,black)
    text3 = ecrire("Retour au Bureau",True,black)
    titre1=grandtitre.render("MENU PAUSE", True, black)
    while True:
        fenetre.fill(jaune)
        dessiner(fenetre, black, [170, 379+84*position_bouton, 300, 64], 3)
        dessiner(fenetre, black, [170, 379, 300, 64], 1)
        dessiner(fenetre, black, [170, 463, 300, 64], 1)
        dessiner(fenetre, black, [170, 547, 300, 64], 1)
        fenetre.blit(titre1, titre1.get_rect(center=(fenetre.get_width()/2, 60)))
        fenetre.blit(text1, text1.get_rect(center=(fenetre.get_width()/2, 411)))
        fenetre.blit(text2, text2.get_rect(center=(fenetre.get_width()/2, 495)))
        fenetre.blit(text3, text3.get_rect(center=(fenetre.get_width()/2, 579)))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return "End"
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if position_bouton == 0:
                        return None
                    if position_bouton == 1:
                        return start_menu(fenetre,joueur)
                    if position_bouton == 2:
                        return "End"
                if event.key == K_ESCAPE:
                    pygame.mixer.music.load('data/01 - Chanson Pour l Auvergnat.mp3')
                    #pygame.mixer.music.play(-1)
                    return None
                if event.key == K_DOWN or event.key == K_RIGHT:
                    if position_bouton <2:
                        position_bouton += 1
                if event.key == K_UP or event.key == K_LEFT:
                    if position_bouton >0:
                        position_bouton -= 1
        pygame.display.flip()

