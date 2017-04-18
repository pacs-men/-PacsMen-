# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:24:09 2017

@author: nassim.zaki
"""
import pygame
from pygame.locals import *
import sys
sys.path.append("../combat")
import combat
pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme Pygame de base')
Joueur = combat.AssassinsMagique()


def inventaire(fenetre,Joueur):
    continuer = 1
    font = pygame.font.SysFont('Calibri', 25, True, False)
    black=(0,0,0)
    blanc=(0xFF, 0xFF, 0xFF)
    position_bouton = 1
    fenetre.fill(blanc)
    dessiner=pygame.draw.rect
    ecrire=font.render
    while continuer == 1:
        dessiner(fenetre, black,[20, 2, 450, 40],1)
        potionvie1=ecrire("Petite potion de vie",True, black)
        fenetre.blit(potionvie1,(30,10))
        fenetre.blit(ecrire(str(Joueur.potionvie1),True,black),(410,10))
        dessiner(fenetre, black,[20, 45, 450, 40],1)
        potionvie2=ecrire("Grande potion de vie",True, black)
        fenetre.blit(potionvie2,(30,55))
        fenetre.blit(ecrire(str(Joueur.potionvie2),True,black),(410,55))
        dessiner(fenetre, black,[20, 90, 450, 40],1)
        potionvie3=ecrire("Enorme potion de vie",True, black)
        fenetre.blit(potionvie3,(30,100))
        fenetre.blit(ecrire(str(Joueur.potionvie3),True,black),(410,100))
        dessiner(fenetre, black,[20, 135, 450, 40],1)
        potionarmure1=ecrire("Petite potion d'armure",True, black)
        fenetre.blit(potionarmure1,(30,145))
        fenetre.blit(ecrire(str(Joueur.potionarmure1),True,black),(410,145))
        dessiner(fenetre, black,[20, 180, 450, 40],1)
        potionarmure2=ecrire("Grande potion d'armure",True, black)
        fenetre.blit(potionarmure2,(30,190))
        fenetre.blit(ecrire(str(Joueur.potionarmure2),True,black),(410,190))
        dessiner(fenetre, black,[20, 225, 450, 40],1)
        potionarmure3=ecrire("Enorme potion d'armure",True, black)
        fenetre.blit(potionarmure3,(30,235))
        fenetre.blit(ecrire(str(Joueur.potionarmure3),True,black),(410,235))
        dessiner(fenetre, black,[20, 270, 450, 40],1)
        potionforce1=ecrire("Petite potion de force",True, black)
        fenetre.blit(potionforce1,(30,280))
        fenetre.blit(ecrire(str(Joueur.potionforce1),True,black),(410,280))
        dessiner(fenetre, black,[20, 315, 450, 40],1)
        potionforce2=ecrire("Grande potion de force",True, black)
        fenetre.blit(potionforce2,(30,325))
        fenetre.blit(ecrire(str(Joueur.potionforce2),True,black),(410,325))
        dessiner(fenetre, black,[20, 360, 450, 40],1)
        potionforce3=ecrire("Enorme potion de vie",True, black)
        fenetre.blit(potionforce3,(30,370))
        fenetre.blit(ecrire(str(Joueur.potionforce3),True,black),(410,370))
        dessiner(fenetre, black,[20, 405, 450, 40],1)
        potioncritique1=ecrire("Petite potion de critique",True, black)
        fenetre.blit(potioncritique1,(30,415))
        fenetre.blit(ecrire(str(Joueur.potioncritique1),True,black),(410,415))
        dessiner(fenetre, black,[20, 450, 450, 40],1)
        potioncritique2=ecrire("Grande potion de critique",True, black)
        fenetre.blit(potioncritique2,(30,460))
        fenetre.blit(ecrire(str(Joueur.potioncritique2),True,black),(410,460))
        dessiner(fenetre, black,[20, 495, 450, 40],1)
        potioncritique3=ecrire("Enorme potion de critique",True, black)
        fenetre.blit(potioncritique3,(30,505))
        fenetre.blit(ecrire(str(Joueur.potioncritique3),True,black),(410,505))
        dessiner(fenetre, black,[20, 540, 450, 40],1)
        potionvitesse=ecrire("Potion de vitesse",True, black)
        fenetre.blit(potionvitesse,(30,550))
        fenetre.blit(ecrire(str(Joueur.potionvitesse),True,black),(410,550))
        dessiner(fenetre, black,[20, 585, 450, 40],1)
        potionprecision=ecrire("Potion de précision",True, black)
        fenetre.blit(potionprecision,(30,595))
        fenetre.blit(ecrire(str(Joueur.potionprecision),True,black),(410,595))

#
#        if position_bouton == 1:
#            pygame.draw.rect(fenetre, blanc, [210, 590, 190, 50], 3)
#            pygame.draw.rect(fenetre, blanc, [100, 590, 110, 50], 3)
#            pygame.draw.rect(fenetre, black, [0, 590, 100, 50], 3)
#        if position_bouton == 2:
#            pygame.draw.rect(fenetre, blanc, [0, 590, 100, 50], 3)
#            pygame.draw.rect(fenetre, blanc, [210, 590, 190, 50], 3)
#            pygame.draw.rect(fenetre, black, [100, 590, 110, 50], 3)
#        if position_bouton == 3:
#            pygame.draw.rect(fenetre, blanc, [100, 590, 110, 50], 3)
#            pygame.draw.rect(fenetre, blanc, [0, 590, 100, 50], 3)
#            pygame.draw.rect(fenetre, black, [210, 590, 190, 50], 3)
#        if position_bouton == 4:
#            pygame.draw.rect(fenetre, blanc, [210, 590, 190, 50], 3)
#            pygame.draw.rect(fenetre, blanc, [100, 590, 110, 50], 3)
#            pygame.draw.rect(fenetre, black, [0, 590, 100, 50], 3)
#        if position_bouton == 5:
#            pygame.draw.rect(fenetre, blanc, [0, 590, 100, 50], 3)
#            pygame.draw.rect(fenetre, blanc, [210, 590, 190, 50], 3)
#            pygame.draw.rect(fenetre, black, [100, 590, 110, 50], 3)
#        if position_bouton == 6:
#            pygame.draw.rect(fenetre, blanc, [100, 590, 110, 50], 3)
#            pygame.draw.rect(fenetre, blanc, [0, 590, 100, 50], 3)
#            pygame.draw.rect(fenetre, black, [210, 590, 190, 50], 3)

        print Joueur.potionvie1
        pygame.display.flip()
pygame.display.flip()
inventaire(fenetre,Joueur)