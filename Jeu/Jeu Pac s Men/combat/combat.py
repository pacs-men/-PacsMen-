# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

        
def combat_start(joueur,participant):
    ''' 
        fonction principale du combat 
        parametre: class joueur , liste des participants
        
        appelle la fonction secondaire en ajoutant joueur a la liste des participant
        trie les participants au combat selon leur vitesse
    '''
    participant.append(joueur)
    participant.sort(key=lambda v: v.vit)
    participant.reverse()
    combat_attaque(participant)
    participant.remove(joueur)
    
    
def combat_attaque(participant_vit):
    '''
        attaque de tous les participants dans l'ordre de vitesse + test de mort
    '''
    for i in range (len(participant_vit)):
        participant_vit[i].passif_def(participant_vit)
        if participant_vit[i].pv < 0:
            if participant_vit[i].jouable==True:
                break
            else:
                pass
            
        else:
            if participant_vit[i].jouable==True:
                 if joueur.type_action == "potion":
                     joueur.popo_actif()
                 elif joueur.type_action == "attaque":
                     participant_vit[i].attaque()
                     participant_vit[i].popo_def()
            else:
                participant_vit[i].cible_def(participant_vit)
                participant_vit[i].attaque()
                participant_vit[i].popo_def()
            
            
    
    

        
def affiche_combat(fenetre,joueur,ennemi):
    continuer = 1
    position_bouton=1
    black=(0,0,0)
    blanc=(0xFF, 0xFF, 0xFF)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text1 = font.render("attaque",True,black)
    text2 =font.render("potion",True,black)
    text3 =font.render("fuite",True,black)
    text4 = font.render(ennemi[1].nom,True,black)
    text5 = font.render("attaque physique",True,black)
    text6 = font.render("attaque magique",True,black)

    fenetre.fill(blanc)
    background_image = pygame.image.load("data/background.jpg").convert()
    fenetre.blit(background_image, [0, 0])
    
    fenetre.blit(joueur.img, [10, 50])
    
    
    while continuer == 1:
        if position_bouton == 1:
            pygame.draw.rect(fenetre, blanc, [210, 590, 190, 50], 3)
            pygame.draw.rect(fenetre, blanc, [100, 590, 110, 50], 3)
            pygame.draw.rect(fenetre, black, [0, 590, 100, 50], 3)
        if position_bouton == 2:
            pygame.draw.rect(fenetre, blanc, [0, 590, 100, 50], 3)
            pygame.draw.rect(fenetre, blanc, [210, 590, 190, 50], 3)
            pygame.draw.rect(fenetre, black, [100, 590, 110, 50], 3)
        if position_bouton == 3:
            pygame.draw.rect(fenetre, blanc, [100, 590, 110, 50], 3)
            pygame.draw.rect(fenetre, blanc, [0, 590, 100, 50], 3)
            pygame.draw.rect(fenetre, black, [210, 590, 190, 50], 3)
        fenetre.blit(text1, [10, 600])
        fenetre.blit(text2, [120, 600])
        fenetre.blit(text3, [230, 600])
        fenetre.blit(text4, [430, 600])
        pygame.draw.rect(fenetre, black, [0, 590, 640, 50], 1)
        pygame.draw.line(fenetre, black, [100, 590], [100, 640], 1)
        pygame.draw.line(fenetre, black, [210, 590], [210, 640], 1)
        pygame.draw.line(fenetre, black, [400, 590], [400, 640], 1)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_TAB:
                    continuer = 0
                if event.key == K_UP or event.key == K_RIGHT:
                    if position_bouton <3:
                        position_bouton += 1
                if event.key == K_DOWN or event.key == K_LEFT:
                    if position_bouton >1:
                        position_bouton -= 1

                if event.key == K_RETURN:

                    if position_bouton == 1:
                        joueur.action_type = "attaque"
                        position_bouton =1
                        while continuer == 1:
                            if position_bouton == 1:
                                pygame.draw.rect(fenetre, blanc, [0, 590, 590, 50], 3)
                                pygame.draw.rect(fenetre, black, [590, 590, 50, 50], 3)
                            if position_bouton == 2:
                                pygame.draw.rect(fenetre, blanc, [210, 590, 190, 50], 3)
                                pygame.draw.rect(fenetre, black, [100, 590, 110, 50], 3)
                            pygame.draw.rect(fenetre, blanc, [0, 585, 640, 55])
                            pygame.draw.rect(fenetre, black, [0, 590, 640, 50], 1)
                            pygame.draw.line(fenetre, black, [400, 590], [400, 640], 1)
                            pygame.draw.line(fenetre, black, [200, 590], [200, 640], 1)
                            fenetre.blit(text4, [430, 600])
                            fenetre.blit(text5, [5, 600])
                            fenetre.blit(text6, [210, 600])
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_TAB:
                                        continuer = 0
                                    if event.key == K_UP or event.key == K_RIGHT:
                                        if position_bouton <2:
                                            position_bouton += 1
                                    if event.key == K_DOWN or event.key == K_LEFT:
                                        if position_bouton >1:
                                            position_bouton -= 1
                                    if event.key == K_RETURN:
                                        if position_bouton == 1:
                                            joueur.action = "Physique"
                                        if position_bouton == 2:
                                            joueur.action = "Magique"
                                        select_ennemi(fenetre,joueur,ennemi)

                    if position_bouton == 2:
                        joueur.action_type = "potion"
                        while continuer == 1:

                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_TAB:
                                        continuer = 0

                    if position_bouton == 3:
                        while continuer == 1:

                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_TAB:
                                        continuer = 0


def select_ennemi(fenetre,joueur,ennemi):
    pass
