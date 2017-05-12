# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:24:09 2017

@author: nassim.zaki et martin.abelard
"""
import pygame
from pygame.locals import *

#pygame.init()
#fenetre=pygame.display.set_mode((640,640))
#pygame.display.set_caption('Programme Pygame de base')
#Joueur = perso.AssassinsMagique()
#Joueur.potionvie1 += 10
#Joueur.pv -= 10

charger = pygame.image.load
black=(0,0,0)
blanc=(0xFF, 0xFF, 0xFF)
jaune=(255, 255, 153)

def inventaire(fenetre,Joueur):
    continuer = 1
    font = pygame.font.SysFont('Calibri', 25, False, False)
    position_bouton = 0
    dessiner=pygame.draw.rect
    ecrire=font.render
    while continuer == 1:
        fenetre.fill(jaune)
        
#        pygame.draw.rect(fenetre, blanc, [20, 2+45*(position_bouton-1), 450, 40], 3)
#        pygame.draw.rect(fenetre, blanc, [20, 2+45*(position_bouton+1), 450, 40], 3)
        pygame.draw.rect(fenetre, black, [20, 2+45*position_bouton, 450, 40], 3)
        
        dessiner(fenetre, black,[20, 2, 450, 40],1)
        potionvie1=ecrire("Petite potion de vie",True, black)
        fenetre.blit(potionvie1,(80,10))
        fenetre.blit(charger("data/potionv2_40.png"),(40,2))
        fenetre.blit(ecrire(str(Joueur.potionvie1),True,black),(410,10))
        
        dessiner(fenetre, black,[20, 47, 450, 40],1)
        potionvie2=ecrire("Grande potion de vie",True, black)
        fenetre.blit(potionvie2,(80,55))
        fenetre.blit(charger("data/perso.png"),(40,47))
        fenetre.blit(ecrire(str(Joueur.potionvie2),True,black),(410,55))
        
        dessiner(fenetre, black,[20, 92, 450, 40],1)
        potionvie3=ecrire("Enorme potion de vie",True, black)
        fenetre.blit(potionvie3,(80,100))
        fenetre.blit(charger("data/potionv3_40.png"),(40,92))
        fenetre.blit(ecrire(str(Joueur.potionvie3),True,black),(410,100))
        
        dessiner(fenetre, black,[20, 137, 450, 40],1)
        potionarmure1=ecrire("Petite potion d'armure",True, black)
        fenetre.blit(potionarmure1,(80,145))
        fenetre.blit(charger("data/potiona2_40.png"),(40,137))
        fenetre.blit(ecrire(str(Joueur.potionarmure1),True,black),(410,145))
        
        dessiner(fenetre, black,[20, 182, 450, 40],1)
        potionarmure2=ecrire("Grande potion d'armure",True, black)
        fenetre.blit(potionarmure2,(80,190))
        fenetre.blit(charger("data/potiona1_40.png"),(40,182))
        fenetre.blit(ecrire(str(Joueur.potionarmure2),True,black),(410,190))
        
        dessiner(fenetre, black,[20, 227, 450, 40],1)
        potionarmure3=ecrire("Enorme potion d'armure",True, black)
        fenetre.blit(potionarmure3,(80,235))
        fenetre.blit(charger("data/potiona3_40.png"),(40,227))
        fenetre.blit(ecrire(str(Joueur.potionarmure3),True,black),(410,235))
        
        dessiner(fenetre, black,[20, 272, 450, 40],1)
        potionforce1=ecrire("Petite potion de force",True, black)
        fenetre.blit(potionforce1,(80,280))
        fenetre.blit(charger("data/potionf2_40.png"),(40,272))
        fenetre.blit(ecrire(str(Joueur.potionforce1),True,black),(410,280))
        
        dessiner(fenetre, black,[20, 317, 450, 40],1)
        potionforce2=ecrire("Grande potion de force",True, black)
        fenetre.blit(potionforce2,(80,325))
        fenetre.blit(charger("data/potionf1_40.png"),(40,317))
        fenetre.blit(ecrire(str(Joueur.potionforce2),True,black),(410,325))
        
        dessiner(fenetre, black,[20, 362, 450, 40],1)
        potionforce3=ecrire("Enorme potion de force",True, black)
        fenetre.blit(potionforce3,(80,370))
        fenetre.blit(charger("data/potionf3_40.png"),(40,362))
        fenetre.blit(ecrire(str(Joueur.potionforce3),True,black),(410,370))
        
        dessiner(fenetre, black,[20, 407, 450, 40],1)
        potioncritique1=ecrire("Petite potion de critique",True, black)
        fenetre.blit(potioncritique1,(80,415))
        fenetre.blit(charger("data/potioncrit2_40.png"),(40,407))
        fenetre.blit(ecrire(str(Joueur.potioncritique1),True,black),(410,415))
        
        dessiner(fenetre, black,[20, 452, 450, 40],1)
        potioncritique2=ecrire("Grande potion de critique",True, black)
        fenetre.blit(potioncritique2,(80,460))
        fenetre.blit(charger("data/perso.png"),(40,452))
        fenetre.blit(ecrire(str(Joueur.potioncritique2),True,black),(410,460))
        
        dessiner(fenetre, black,[20, 497, 450, 40],1)
        potioncritique3=ecrire("Enorme potion de critique",True, black)
        fenetre.blit(potioncritique3,(80,505))
        fenetre.blit(charger("data/perso.png"),(40,497))
        fenetre.blit(ecrire(str(Joueur.potioncritique3),True,black),(410,505))
        
        dessiner(fenetre, black,[20, 542, 450, 40],1)
        potionvitesse=ecrire("Potion de vitesse",True, black)
        fenetre.blit(potionvitesse,(80,550))
        fenetre.blit(charger("data/potionvit1_40.png"),(40,542))
        fenetre.blit(ecrire(str(Joueur.potionvitesse),True,black),(410,550))
        
        dessiner(fenetre, black,[20, 587, 450, 40],1)
        potionprecision=ecrire("Potion de precision",True, black)
        fenetre.blit(potionprecision,(80,595))
        fenetre.blit(charger("data/perso.png"),(40,587))
        fenetre.blit(ecrire(str(Joueur.potionprecision),True,black),(410,595))

		#affichage des stats du personnage
		#affichage de la vie
        pvperso=ecrire("Pv:"+str(Joueur.pv),True,black)
        pvperso_rect=pvperso.get_rect()
        pvperso_rect.right = 630
        pvperso_rect.top = 10
        fenetre.blit(pvperso,pvperso_rect)
		#affichage de l'armure
        if Joueur.defen > 90:
            armureperso=ecrire("Defense:"+str(90),True,black)
        else:
            armureperso=ecrire("Defense:"+str(Joueur.defen),True,black)
        armureperso_rect=armureperso.get_rect()
        armureperso_rect.right = 630
        armureperso_rect.top = 35
        fenetre.blit(armureperso,armureperso_rect)
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_i:
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
                        Joueur.action="armure1"
                    if position_bouton==4:
                        Joueur.action="armure2"
                    if position_bouton==5:
                        Joueur.action="armure3"
                    if position_bouton==6:
                        Joueur.action="force1"
                    if position_bouton==7:
                        Joueur.action="force2"
                    if position_bouton==8:
                        Joueur.action="force3"
                    if position_bouton==9:
                        Joueur.action="critique1"
                    if position_bouton==10:
                        Joueur.action="critique2"
                    if position_bouton==11:
                        Joueur.action="critique3"
                    if position_bouton==12:
                        Joueur.action="vitesse"
                    if position_bouton==13:
                        Joueur.action="precision"
                    Joueur.popo_actif()
                    
        pygame.display.flip()
