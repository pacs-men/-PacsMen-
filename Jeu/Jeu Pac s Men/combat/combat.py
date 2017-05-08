# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
pygame.init()
noir=(0,0,0)
blanc=(0xFF, 0xFF, 0xFF)
font = pygame.font.SysFont('Calibri', 25, True, False)


        
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
        if participant_vit[i].pv <= 0:
            if participant_vit[i].jouable==True:
                return "Mort joueur"
            else:
                pass
            
        else:
            if participant_vit[i].jouable==True:
                 if participant_vit[i].type_action == "potion":
                     participant_vit[i].popo_actif()
                 elif participant_vit[i].type_action == "attaque":
                     participant_vit[i].attaque()
                     participant_vit[i].popo_def()
            else:
                participant_vit[i].cible_def(participant_vit)
                participant_vit[i].attaque()
                participant_vit[i].popo_def()
            
            
    
    

        
def affiche_combat(fenetre,joueur,ennemi):
    pygame.mixer.music.load('data/05 - Le Voyage de Basile.mp3')
    pygame.mixer.music.play(-1)
    continuer = 1
    position_bouton=1
    tour=1
    text1 = font.render("attaque",True,noir)
    text2 = font.render("potion",True,noir)
    text3 = font.render("fuite",True,noir)
    text4 = font.render(ennemi[1].nom,True,noir)

    background_image = pygame.image.load("data/background.jpg").convert()
    fenetre.blit(background_image, [0, 0])
    fenetre.blit(joueur.img, [10, 50])
    
    
    while continuer == 1:
        text5 = font.render("tour "+str(tour),True,noir)
        text6 = font.render("Pv : "+str(joueur.pv)+"/"+str(joueur.pv_max),True,noir)
        fenetre.fill(blanc)
        fenetre.blit(background_image, [0, 0])
        fenetre.blit(joueur.img, [10, 50])

        if position_bouton == 1:
            pygame.draw.rect(fenetre, noir, [0, 590, 100, 50], 3)

        if position_bouton == 2:
            pygame.draw.rect(fenetre, noir, [100, 590, 110, 50], 3)

        if position_bouton == 3:
            pygame.draw.rect(fenetre, noir, [210, 590, 190, 50], 3)

        fenetre.blit(text1, [10, 600])
        fenetre.blit(text2, [120, 600])
        fenetre.blit(text3, [230, 600])
        fenetre.blit(text4, [430, 600])
        fenetre.blit(text5, [10, 10])
        fenetre.blit(text6, [10, 500])


        pygame.draw.rect(fenetre, noir, [0, 590, 640, 50], 1)
        pygame.draw.line(fenetre, noir, [100, 590], [100, 640], 1)
        pygame.draw.line(fenetre, noir, [210, 590], [210, 640], 1)
        pygame.draw.line(fenetre, noir, [400, 590], [400, 640], 1)
        pygame.display.flip()
        
        for event in pygame.event.get():

            if event.type == QUIT:
                continuer = 0

            if event.type == KEYDOWN:

                if event.key == K_UP or event.key == K_RIGHT:
                    if position_bouton <3:
                        position_bouton += 1

                if event.key == K_DOWN or event.key == K_LEFT:
                    if position_bouton >1:
                        position_bouton -= 1

                if event.key == K_RETURN:

                    if position_bouton == 1:
                        info = attaque_type(fenetre,joueur,ennemi)
                        if info == "End":
                            continuer = 0
                        if info == "Next":
                            tour+=1

                    if position_bouton == 2:
                        info = potion_type(fenetre,joueur,ennemi)
                        if info == "End":
                            continuer = 0
                        if info == "Next":
                            tour+=1

                    if position_bouton == 3:
                        continuer = 2
                        while continuer == 2:

                            for event in pygame.event.get():

                                if event.type == QUIT:
                                    continuer = 0

                                if event.type == KEYDOWN:

                                    if event.key == K_TAB:
                                        continuer = 1
    pygame.mixer.music.load('data/01 - Chanson Pour l Auvergnat.mp3')
    pygame.mixer.music.play(-1)


def select_ennemi(fenetre,joueur,ennemi):
    print "Pour Nassim"
    fenetre.blit(ennemi.img_combat)
    

def attaque_type(fenetre,joueur,ennemi):
    text1 = font.render(ennemi[1].nom,True,noir)
    text2 = font.render("attaque physique",True,noir)
    text3 = font.render("attaque magique",True,noir)
    continuer = 1
    position_bouton = 1
    joueur.action_type = "attaque"
    pygame.draw.rect(fenetre, blanc, [0, 585, 640, 55])
    


    while continuer == 1:

        if position_bouton == 1:
            pygame.draw.rect(fenetre, blanc, [200, 590, 200, 50], 3)
            pygame.draw.rect(fenetre, noir, [0, 590, 200, 50], 3)

        if position_bouton == 2:
            pygame.draw.rect(fenetre, blanc, [0, 590, 200, 50], 3)
            pygame.draw.rect(fenetre, noir, [200, 590, 200, 50], 3)

        pygame.draw.rect(fenetre, noir, [0, 590, 640, 50], 1)
        pygame.draw.line(fenetre, noir, [400, 590], [400, 640], 1)
        pygame.draw.line(fenetre, noir, [200, 590], [200, 640], 1)

        fenetre.blit(text1, [430, 600])
        fenetre.blit(text2, [5, 600])
        fenetre.blit(text3, [210, 600])
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == QUIT:
                return "End"

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

                    return select_ennemi(fenetre,joueur,ennemi)
    return "Retour"

def potion_type(fenetre,joueur,ennemi):
    joueur.action_type = "potion"
    position_bouton = 0
    dessiner=pygame.draw.rect
    ecrire=font.render
    continuer = 1
    while continuer == 1:

        fenetre.fill(blanc)
        
        pygame.draw.rect(fenetre, blanc, [20, 2+45*(position_bouton-1), 450, 40], 3)
        pygame.draw.rect(fenetre, blanc, [20, 2+45*(position_bouton+1), 450, 40], 3)
        pygame.draw.rect(fenetre, noir, [20, 2+45*position_bouton, 450, 40], 3)
        
        dessiner(fenetre, noir,[20, 2, 450, 40],1)
        fenetre.blit(ecrire("Petite potion de vie",True, noir),(30,10))
        fenetre.blit(ecrire(str(joueur.potionvie1),True,noir),(410,10))
        
        dessiner(fenetre, noir,[20, 47, 450, 40],1)
        fenetre.blit(ecrire("Grande potion de vie",True, noir),(30,55))
        fenetre.blit(ecrire(str(joueur.potionvie2),True,noir),(410,55))
        
        dessiner(fenetre, noir,[20, 92, 450, 40],1)
        fenetre.blit(ecrire("Enorme potion de vie",True, noir),(30,100))
        fenetre.blit(ecrire(str(joueur.potionvie3),True,noir),(410,100))
        
        dessiner(fenetre, noir,[20, 137, 450, 40],1)
        fenetre.blit(ecrire("Petite potion d'armure",True, noir),(30,145))
        fenetre.blit(ecrire(str(joueur.potionarmure1),True,noir),(410,145))
        
        dessiner(fenetre, noir,[20, 182, 450, 40],1)
        fenetre.blit(ecrire("Grande potion d'armure",True, noir),(30,190))
        fenetre.blit(ecrire(str(joueur.potionarmure2),True,noir),(410,190))
        
        dessiner(fenetre, noir,[20, 227, 450, 40],1)
        fenetre.blit(ecrire("Enorme potion d'armure",True, noir),(30,235))
        fenetre.blit(ecrire(str(joueur.potionarmure3),True,noir),(410,235))
        
        dessiner(fenetre, noir,[20, 272, 450, 40],1)
        fenetre.blit(ecrire("Petite potion de force",True, noir),(30,280))
        fenetre.blit(ecrire(str(joueur.potionforce1),True,noir),(410,280))
        
        dessiner(fenetre, noir,[20, 317, 450, 40],1)
        fenetre.blit(ecrire("Grande potion de force",True, noir),(30,325))
        fenetre.blit(ecrire(str(joueur.potionforce2),True,noir),(410,325))
        
        dessiner(fenetre, noir,[20, 362, 450, 40],1)
        fenetre.blit(ecrire("Enorme potion de vie",True, noir),(30,370))
        fenetre.blit(ecrire(str(joueur.potionforce3),True,noir),(410,370))
        
        dessiner(fenetre, noir,[20, 407, 450, 40],1)
        fenetre.blit(ecrire("Petite potion de critique",True, noir),(30,415))
        fenetre.blit(ecrire(str(joueur.potioncritique1),True,noir),(410,415))
        
        dessiner(fenetre, noir,[20, 452, 450, 40],1)
        fenetre.blit(ecrire("Grande potion de critique",True, noir),(30,460))
        fenetre.blit(ecrire(str(joueur.potioncritique2),True,noir),(410,460))
        
        dessiner(fenetre, noir,[20, 497, 450, 40],1)
        fenetre.blit(ecrire("Enorme potion de critique",True, noir),(30,505))
        fenetre.blit(ecrire(str(joueur.potioncritique3),True,noir),(410,505))
        
        dessiner(fenetre, noir,[20, 542, 450, 40],1)
        fenetre.blit(ecrire("Potion de vitesse",True, noir),(30,550))
        fenetre.blit(ecrire(str(joueur.potionvitesse),True,noir),(410,550))
        
        dessiner(fenetre, noir,[20, 587, 450, 40],1)
        fenetre.blit(ecrire("Potion de precision",True, noir),(30,595))
        fenetre.blit(ecrire(str(joueur.potionprecision),True,noir),(410,595))
        
        for event in pygame.event.get():

            if event.type == QUIT:
                return "End"

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
                        joueur.action="vie1"
                    if position_bouton==1:
                        joueur.action="vie2"
                    if position_bouton==2:
                        joueur.action="vie3"
                    if position_bouton==3:
                        joueur.action="force1"
                    if position_bouton==4:
                        joueur.action="force2"
                    if position_bouton==5:
                        joueur.action="force3"
                    if position_bouton==6:
                        joueur.action="armure1"
                    if position_bouton==7:
                        joueur.action="armure2"
                    if position_bouton==8:
                        joueur.action="armure3"
                    if position_bouton==9:
                        joueur.action="critique1"
                    if position_bouton==10:
                        joueur.action="critique2"
                    if position_bouton==11:
                        joueur.action="critique3"
                    if position_bouton==12:
                        joueur.action="vitesse"
                    if position_bouton==12:
                        joueur.action="precision"
                    combat_start(joueur,ennemi)
                    return "Next"
                    
        pygame.display.flip()
    return "Retour"