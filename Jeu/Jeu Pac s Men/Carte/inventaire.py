# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:24:09 2017

@author: nassim.zaki
"""
import pygame
from pygame.locals import *
import sys
sys.path.append("../combat")
import perso
pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme Pygame de base')
Joueur = perso.AssassinsMagique()
Joueur.potionvie1 += 10
Joueur.pv -= 10

def inventaire(fenetre,Joueur):
    continuer = 1
    font = pygame.font.SysFont('Calibri', 25, True, False)
    black=(0,0,0)
    blanc=(0xFF, 0xFF, 0xFF)
    position_bouton = 0
    dessiner=pygame.draw.rect
    ecrire=font.render
    while continuer == 1:
        fenetre.fill(blanc)
        
        pygame.draw.rect(fenetre, blanc, [20, 2+45*(position_bouton-1), 450, 40], 3)
        pygame.draw.rect(fenetre, blanc, [20, 2+45*(position_bouton+1), 450, 40], 3)
        pygame.draw.rect(fenetre, black, [20, 2+45*position_bouton, 450, 40], 3)
        
        dessiner(fenetre, black,[20, 2, 450, 40],1)
        potionvie1=ecrire("Petite potion de vie",True, black)
        fenetre.blit(potionvie1,(30,10))
        fenetre.blit(ecrire(str(Joueur.potionvie1),True,black),(410,10))
        
        dessiner(fenetre, black,[20, 47, 450, 40],1)
        potionvie2=ecrire("Grande potion de vie",True, black)
        fenetre.blit(potionvie2,(30,55))
        fenetre.blit(ecrire(str(Joueur.potionvie2),True,black),(410,55))
        
        dessiner(fenetre, black,[20, 92, 450, 40],1)
        potionvie3=ecrire("Enorme potion de vie",True, black)
        fenetre.blit(potionvie3,(30,100))
        fenetre.blit(ecrire(str(Joueur.potionvie3),True,black),(410,100))
        
        dessiner(fenetre, black,[20, 137, 450, 40],1)
        potionarmure1=ecrire("Petite potion d'armure",True, black)
        fenetre.blit(potionarmure1,(30,145))
        fenetre.blit(ecrire(str(Joueur.potionarmure1),True,black),(410,145))
        
        dessiner(fenetre, black,[20, 182, 450, 40],1)
        potionarmure2=ecrire("Grande potion d'armure",True, black)
        fenetre.blit(potionarmure2,(30,190))
        fenetre.blit(ecrire(str(Joueur.potionarmure2),True,black),(410,190))
        
        dessiner(fenetre, black,[20, 227, 450, 40],1)
        potionarmure3=ecrire("Enorme potion d'armure",True, black)
        fenetre.blit(potionarmure3,(30,235))
        fenetre.blit(ecrire(str(Joueur.potionarmure3),True,black),(410,235))
        
        dessiner(fenetre, black,[20, 272, 450, 40],1)
        potionforce1=ecrire("Petite potion de force",True, black)
        fenetre.blit(potionforce1,(30,280))
        fenetre.blit(ecrire(str(Joueur.potionforce1),True,black),(410,280))
        
        dessiner(fenetre, black,[20, 317, 450, 40],1)
        potionforce2=ecrire("Grande potion de force",True, black)
        fenetre.blit(potionforce2,(30,325))
        fenetre.blit(ecrire(str(Joueur.potionforce2),True,black),(410,325))
        
        dessiner(fenetre, black,[20, 362, 450, 40],1)
        potionforce3=ecrire("Enorme potion de vie",True, black)
        fenetre.blit(potionforce3,(30,370))
        fenetre.blit(ecrire(str(Joueur.potionforce3),True,black),(410,370))
        
        dessiner(fenetre, black,[20, 407, 450, 40],1)
        potioncritique1=ecrire("Petite potion de critique",True, black)
        fenetre.blit(potioncritique1,(30,415))
        fenetre.blit(ecrire(str(Joueur.potioncritique1),True,black),(410,415))
        
        dessiner(fenetre, black,[20, 452, 450, 40],1)
        potioncritique2=ecrire("Grande potion de critique",True, black)
        fenetre.blit(potioncritique2,(30,460))
        fenetre.blit(ecrire(str(Joueur.potioncritique2),True,black),(410,460))
        
        dessiner(fenetre, black,[20, 497, 450, 40],1)
        potioncritique3=ecrire("Enorme potion de critique",True, black)
        fenetre.blit(potioncritique3,(30,505))
        fenetre.blit(ecrire(str(Joueur.potioncritique3),True,black),(410,505))
        
        dessiner(fenetre, black,[20, 542, 450, 40],1)
        potionvitesse=ecrire("Potion de vitesse",True, black)
        fenetre.blit(potionvitesse,(30,550))
        fenetre.blit(ecrire(str(Joueur.potionvitesse),True,black),(410,550))
        
        dessiner(fenetre, black,[20, 587, 450, 40],1)
        potionprecision=ecrire("Potion de précision",True, black)
        fenetre.blit(potionprecision,(30,595))
        fenetre.blit(ecrire(str(Joueur.potionprecision),True,black),(410,595))
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_TAB:
                    continuer = 0
                if event.key == K_DOWN or event.key == K_RIGHT:
                    if position_bouton <13:
                        position_bouton += 1
                if event.key == K_UP or event.key == K_LEFT:
                    if position_bouton >0:
                        position_bouton -= 1
                if event.key == K_RETURN:
                    if position_bouton==0:
                        Joueur.action="vie1"
                    if position_bouton==1:
                        Joueur.action="vie2"
                    if position_bouton==2:
                        Joueur.action="vie3"
                    if position_bouton==3:
                        Joueur.action="force1"
                    if position_bouton==4:
                        Joueur.action="force2"
                    if position_bouton==5:
                        Joueur.action="force3"
                    if position_bouton==6:
                        Joueur.action="armure1"
                    if position_bouton==7:
                        Joueur.action="armure2"
                    if position_bouton==8:
                        Joueur.action="armure3"
                    if position_bouton==9:
                        Joueur.action="critique1"
                    if position_bouton==10:
                        Joueur.action="critique2"
                    if position_bouton==11:
                        Joueur.action="critique3"
                    if position_bouton==12:
                        Joueur.action="vitesse"
                    if position_bouton==12:
                        Joueur.action="precision"
                    Joueur.popo_actif()
                    
                    


        pygame.display.flip()
pygame.display.flip()
inventaire(fenetre,Joueur)