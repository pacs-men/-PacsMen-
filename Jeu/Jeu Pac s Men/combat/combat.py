# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
pygame.init()
noir=(0,0,0)
blanc=(0xFF, 0xFF, 0xFF)
font = pygame.font.SysFont('Calibri', 25, True, False)
text_attaque = font.render("attaque",True,noir)
text_potion = font.render("potion",True,noir)
text_fuite = font.render("fuite",True,noir)




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
    statut = combat_attaque(participant)
    participant.reverse()
    participant.remove(joueur)
    return statut
    
    
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
    #pygame.mixer.music.load('data/05 - Le Voyage de Basile.mp3')
    #pygame.mixer.music.play(-1)
    nb_ennemis = ennemi[0].nombre
    continuer = 1
    position_bouton=1
    tour=1
    text_ennemi = font.render(ennemi[0].nom,True,noir)
    background_image = pygame.image.load("data/fondcombatmap1.jpg").convert()

    while continuer == 1:
        
        text_tour = font.render("tour "+str(tour),True,noir)
        text_pv_joueur = font.render("Pv : "+str(joueur.pv)+"/"+str(joueur.pv_max),True,noir)
        
        fenetre.blit(background_image, [0, 0])
        pygame.draw.rect(fenetre, blanc, [0, 590, 640, 50])
        fenetre.blit(joueur.img, joueur.img.get_rect(center=(100, 300)))
        
        if nb_ennemis == 1:
            
            text_pv_ennemi_0 = font.render("Pv : "+str(ennemi[0].pv)+"/"+str(ennemi[0].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_0, [500, 350])
            fenetre.blit(ennemi[0].img_combat, ennemi[0].img_combat.get_rect(center=(500, 300)))
            
        if nb_ennemis == 2:
            
            text_pv_ennemi_0 = font.render("Pv : "+str(ennemi[0].pv)+"/"+str(ennemi[0].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_0, [500, 250])
            fenetre.blit(ennemi[1].img_combat, ennemi[1].img_combat.get_rect(center=(500, 200)))
            
            text_pv_ennemi_1 = font.render("Pv : "+str(ennemi[1].pv)+"/"+str(ennemi[1].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_1, [500, 450])
            fenetre.blit(ennemi[1].img_combat, ennemi[1].img_combat.get_rect(center=(500, 400)))
            
        if nb_ennemis == 3 :
            
            text_pv_ennemi_0 = font.render("Pv : "+str(ennemi[0].pv)+"/"+str(ennemi[0].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_0, [500, 200])
            fenetre.blit(ennemi[0].img_combat, ennemi[0].img_combat.get_rect(center=(500, 150)))
            
            text_pv_ennemi_1 = font.render("Pv : "+str(ennemi[1].pv)+"/"+str(ennemi[1].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_1, [500, 350])
            fenetre.blit(ennemi[1].img_combat, ennemi[1].img_combat.get_rect(center=(500, 300)))
            
            text_pv_ennemi_2 = font.render("Pv : "+str(ennemi[2].pv)+"/"+str(ennemi[2].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_2, [500, 500])
            fenetre.blit(ennemi[2].img_combat, ennemi[2].img_combat.get_rect(center=(500, 450)))
            
        if nb_ennemis == 4 :
            
            text_pv_ennemi_0 = font.render("Pv : "+str(ennemi[0].pv)+"/"+str(ennemi[0].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_0, [500, 170])
            fenetre.blit(ennemi[0].img_combat, ennemi[0].img_combat.get_rect(center=(500, 120)))
            
            text_pv_ennemi_1 = font.render("Pv : "+str(ennemi[1].pv)+"/"+str(ennemi[1].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_1, [500, 290])
            fenetre.blit(ennemi[1].img_combat, ennemi[1].img_combat.get_rect(center=(500, 240)))
            
            text_pv_ennemi_2 = font.render("Pv : "+str(ennemi[2].pv)+"/"+str(ennemi[2].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_2, [500, 410])
            fenetre.blit(ennemi[2].img_combat, ennemi[2].img_combat.get_rect(center=(500, 360)))
            
            text_pv_ennemi_3 = font.render("Pv : "+str(ennemi[3].pv)+"/"+str(ennemi[3].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_3, [500, 530])
            fenetre.blit(ennemi[3].img_combat, ennemi[3].img_combat.get_rect(center=(500, 480)))

        if position_bouton == 1:
            pygame.draw.rect(fenetre, noir, [0, 590, 100, 50], 3)

        if position_bouton == 2:
            pygame.draw.rect(fenetre, noir, [100, 590, 110, 50], 3)

        if position_bouton == 3:
            pygame.draw.rect(fenetre, noir, [210, 590, 190, 50], 3)

        fenetre.blit(text_attaque, [10, 600])
        fenetre.blit(text_potion, [120, 600])
        fenetre.blit(text_fuite, [230, 600])
        fenetre.blit(text_ennemi, [430, 600])
        fenetre.blit(text_tour, [10, 10])
        fenetre.blit(text_pv_joueur, [10, 500])


        pygame.draw.rect(fenetre, noir, [0, 590, 640, 50], 1)
        pygame.draw.line(fenetre, noir, [100, 590], [100, 640], 1)
        pygame.draw.line(fenetre, noir, [210, 590], [210, 640], 1)
        pygame.draw.line(fenetre, noir, [400, 590], [400, 640], 1)
        pygame.display.flip()

        pv_toto = 0
        for i in range (nb_ennemis):
            pv_toto += ennemi[i].pv
        if pv_toto == 0:
            return "fin"

        
        for event in pygame.event.get():

            if event.type == QUIT:
                continuer = 0

            if event.type == KEYDOWN:

                if event.key == K_RIGHT:
                    if position_bouton <3:
                        position_bouton += 1

                if event.key == K_LEFT:
                    if position_bouton >1:
                        position_bouton -= 1

                if event.key == K_RETURN:

                    if position_bouton == 1:
                        joueur.type_action = "attaque"
                        info = attaque_type(fenetre,joueur,ennemi,tour)
                        if info == "End":
                            continuer = 0
                        if info == "Mort joueur":
                            return "Mort joueur"
                        if info == "Next":
                            tour+=1

                    if position_bouton == 2:
                        joueur.type_action = "potion"
                        info = potion_type(fenetre,joueur,ennemi)
                        if info == "End":
                            continuer = 0
                        if info == "Next":
                            tour+=1

                    if position_bouton == 3:
                        return "Fuite"

    #pygame.mixer.music.load('data/01 - Chanson Pour l Auvergnat.mp3')
    #pygame.mixer.music.play(-1)


def select_ennemi(fenetre,joueur,ennemi,tour):
    nb_ennemis = ennemi[0].nombre
    continuer = True
    position_bouton= 0
    
    text_ennemi = font.render(ennemi[0].nom,True,noir)
    background_image = pygame.image.load("data/fondcombatmap1.jpg").convert()
    fleche = pygame.image.load("data/fleche.png").convert_alpha()
    
    pygame.draw.rect(fenetre, blanc, [0, 585, 640, 55])
    fenetre.blit(text_ennemi, [430, 600])
    
    
    if nb_ennemis == 1:
         while continuer:
             
            text_tour = font.render("tour "+str(tour),True,noir)
            text_pv_joueur = font.render("Pv : "+str(joueur.pv)+"/"+str(joueur.pv_max),True,noir)
        
            fenetre.blit(background_image, [0, 0])
            fenetre.blit(text_tour, [10, 10])
            fenetre.blit(text_pv_joueur, [10, 500])
            fenetre.blit(joueur.img, joueur.img.get_rect(center=(100, 300)))

            text_pv_ennemi_0 = font.render("Pv : "+str(ennemi[0].pv)+"/"+str(ennemi[0].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_0, [500, 350])
            fenetre.blit(ennemi[0].img_combat, ennemi[0].img_combat.get_rect(center=(500, 300)))

            if position_bouton == 0:
                fenetre.blit(fleche, fleche.get_rect(center=(350, 300)))
            pygame.display.flip()
            for event in pygame.event.get():

                if event.type == QUIT:
                    return "End"

                if event.type == KEYDOWN:
                            
                    if event.key == K_TAB:
                        continuer = False

                    if event.key == K_RETURN:
                        joueur.cible = ennemi[position_bouton]
                        combat_start(joueur,ennemi)
                        return "next"
                                 
    if nb_ennemis == 2:
         while continuer:
             
            text_tour = font.render("tour "+str(tour),True,noir)
            text_pv_joueur = font.render("Pv : "+str(joueur.pv)+"/"+str(joueur.pv_max),True,noir)
        
            fenetre.blit(background_image, [0, 0])
            fenetre.blit(text_tour, [10, 10])
            fenetre.blit(text_pv_joueur, [10, 500])
            fenetre.blit(joueur.img, joueur.img.get_rect(center=(100, 300)))
            
            text_pv_ennemi_0 = font.render("Pv : "+str(ennemi[0].pv)+"/"+str(ennemi[0].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_0, [500, 250])
            fenetre.blit(ennemi[1].img_combat, ennemi[1].img_combat.get_rect(center=(500, 200)))
            
            text_pv_ennemi_1 = font.render("Pv : "+str(ennemi[1].pv)+"/"+str(ennemi[1].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_1, [500, 450])
            fenetre.blit(ennemi[1].img_combat, ennemi[1].img_combat.get_rect(center=(500, 400)))
            
            if position_bouton == 0:
                fenetre.blit(fleche, fleche.get_rect(center=(350, 200)))
            if position_bouton == 1:
                fenetre.blit(fleche, fleche.get_rect(center=(350, 400)))

            for event in pygame.event.get():

                if event.type == QUIT:
                    return "End"

                if event.type == KEYDOWN:
                    
                    if event.key == K_DOWN:
                        if position_bouton <1:
                            position_bouton += 1
                            
                    if event.key == K_UP:
                        if position_bouton >0:
                            position_bouton -= 1
                            
                    if event.key == K_TAB:
                        continuer = False

                    if event.key == K_RETURN:
                        joueur.cible = ennemi[position_bouton]
                        combat_start(joueur,ennemi)
                        return "next"
                        
            pygame.display.flip()
    if nb_ennemis == 3:
         while continuer:
             
            text_tour = font.render("tour "+str(tour),True,noir)
            text_pv_joueur = font.render("Pv : "+str(joueur.pv)+"/"+str(joueur.pv_max),True,noir)
        
            fenetre.blit(background_image, [0, 0])
            fenetre.blit(text_tour, [10, 10])
            fenetre.blit(text_pv_joueur, [10, 500])
            fenetre.blit(joueur.img, joueur.img.get_rect(center=(100, 300)))
            
            text_pv_ennemi_0 = font.render("Pv : "+str(ennemi[0].pv)+"/"+str(ennemi[0].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_0, [500, 200])
            fenetre.blit(ennemi[0].img_combat, ennemi[0].img_combat.get_rect(center=(500, 150)))
            
            text_pv_ennemi_1 = font.render("Pv : "+str(ennemi[1].pv)+"/"+str(ennemi[1].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_1, [500, 350])
            fenetre.blit(ennemi[1].img_combat, ennemi[1].img_combat.get_rect(center=(500, 300)))
            
            text_pv_ennemi_2 = font.render("Pv : "+str(ennemi[2].pv)+"/"+str(ennemi[2].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_2, [500, 500])
            fenetre.blit(ennemi[2].img_combat, ennemi[2].img_combat.get_rect(center=(500, 450)))
            
            if position_bouton == 0:
                fenetre.blit(fleche, fleche.get_rect(center=(350, 150)))
            if position_bouton == 1:
                fenetre.blit(fleche, fleche.get_rect(center=(350, 300)))
            if position_bouton == 2:
                fenetre.blit(fleche, fleche.get_rect(center=(350, 450)))

            for event in pygame.event.get():

                if event.type == QUIT:
                    return "End"

                if event.type == KEYDOWN:
                    
                    if event.key == K_DOWN:
                        if position_bouton <2:
                            position_bouton += 1
                            
                    if event.key == K_UP:
                        if position_bouton >0:
                            position_bouton -= 1
                            
                    if event.key == K_TAB:
                        continuer = False

                    if event.key == K_RETURN:
                        joueur.cible = ennemi[position_bouton]
                        combat_start(joueur,ennemi)
                        return "next"
                        
            pygame.display.flip()
    if nb_ennemis == 4:
         while continuer:
             
            text_tour = font.render("tour "+str(tour),True,noir)
            text_pv_joueur = font.render("Pv : "+str(joueur.pv)+"/"+str(joueur.pv_max),True,noir)
        
            fenetre.blit(background_image, [0, 0])
            fenetre.blit(text_tour, [10, 10])
            fenetre.blit(text_pv_joueur, [10, 500])
            fenetre.blit(joueur.img, joueur.img.get_rect(center=(100, 300)))
            
            text_pv_ennemi_0 = font.render("Pv : "+str(ennemi[0].pv)+"/"+str(ennemi[0].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_0, [500, 170])
            fenetre.blit(ennemi[0].img_combat, ennemi[0].img_combat.get_rect(center=(500, 120)))
            
            text_pv_ennemi_1 = font.render("Pv : "+str(ennemi[1].pv)+"/"+str(ennemi[1].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_1, [500, 290])
            fenetre.blit(ennemi[1].img_combat, ennemi[1].img_combat.get_rect(center=(500, 240)))
            
            text_pv_ennemi_2 = font.render("Pv : "+str(ennemi[2].pv)+"/"+str(ennemi[2].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_2, [500, 410])
            fenetre.blit(ennemi[2].img_combat, ennemi[2].img_combat.get_rect(center=(500, 360)))
            
            text_pv_ennemi_3 = font.render("Pv : "+str(ennemi[3].pv)+"/"+str(ennemi[3].pv_max),True,noir)
            fenetre.blit(text_pv_ennemi_3, [500, 530])
            fenetre.blit(ennemi[3].img_combat, ennemi[3].img_combat.get_rect(center=(500, 480)))
            
            if position_bouton == 0:
                fenetre.blit(fleche, fleche.get_rect(center=(350, 120)))
            if position_bouton == 1:
                fenetre.blit(fleche, fleche.get_rect(center=(350, 240)))
            if position_bouton == 2:
                fenetre.blit(fleche, fleche.get_rect(center=(350, 360)))
            if position_bouton == 3:
                fenetre.blit(fleche, fleche.get_rect(center=(350, 480)))

            for event in pygame.event.get():

                if event.type == QUIT:
                    return "End"

                if event.type == KEYDOWN:
                    
                    if event.key == K_DOWN:
                        if position_bouton <3:
                            position_bouton += 1
                            
                    if event.key == K_UP:
                        if position_bouton >0:
                            position_bouton -= 1
                            
                    if event.key == K_TAB:
                        continuer = False

                    if event.key == K_RETURN:
                        joueur.cible = ennemi[position_bouton]
                        if combat_start(joueur,ennemi) == "Mort joueur":
                            return "Mort joueur"
                        return "next"
                        
            pygame.display.flip()

    return "Retour"

def attaque_type(fenetre,joueur,ennemi,tour):
    text1 = font.render(ennemi[0].nom,True,noir)
    text2 = font.render("attaque physique",True,noir)
    text3 = font.render("attaque magique",True,noir)
    continuer = 1
    position_bouton = 1
    joueur.action_type = "attaque"
    pygame.draw.rect(fenetre, blanc, [0, 590, 640, 50])
    


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

                if event.key == K_DOWN:
                    if position_bouton <2:
                        position_bouton += 1

                if event.key == K_UP:
                    if position_bouton >1:
                        position_bouton -= 1

                if event.key == K_RETURN:

                    if position_bouton == 1:
                        joueur.action = "Physique"

                    if position_bouton == 2:
                        joueur.action = "Magique"

                    return select_ennemi(fenetre,joueur,ennemi,tour)
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
        fenetre.blit(ecrire("Enorme potion de force",True, noir),(30,370))
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

                if event.key == K_DOWN:
                    if position_bouton <13:
                        position_bouton += 1
                if event.key == K_UP:
                    if position_bouton >0:
                        position_bouton -= 1

                if event.key == K_RETURN:
                    if position_bouton==0:
                        joueur.action="vie1"
                    if position_bouton==1:
                        joueur.action="vie2"
                    if position_bouton==2:
                        joueur.action="vie3"
                    if position_bouton==6:
                        joueur.action="force1"
                    if position_bouton==7:
                        joueur.action="force2"
                    if position_bouton==8:
                        joueur.action="force3"
                    if position_bouton==3:
                        joueur.action="armure1"
                    if position_bouton==4:
                        joueur.action="armure2"
                    if position_bouton==5:
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
