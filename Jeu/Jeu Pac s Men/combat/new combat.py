import pygame,random
from pygame.locals import *
pygame.init()
noir=(0,0,0)
blanc=(0xFF, 0xFF, 0xFF)
bleuClair = (18,158,158)
font = pygame.font.SysFont('Calibri', 25, True, False)
text_attaque = font.render("attaque",True,noir)
text_potion = font.render("potion",True,noir)
text_fuite = font.render("fuite",True,noir)




def mainCombat(Fenetre,Joueur,Ennemi):
    """
        Fonction principal d'un combat
        mainCombat(Fenetre = fenetre Pygame , Joueur = Class , Ennemi = Liste de Class)
    """
    statCombat = {'NumerauxTourActuel' : 1}
    initialisationFenetreCombat(Fenetre,Joueur,Ennemi,statCombat)



def initialisationFenetreCombat(Fenetre,Joueur,Ennemi,StatCombat):
    """
        Fonction d'affichage initial du combat (interne)
        mainCombat(Fenetre = fenetre Pygame , Joueur = Class , Ennemi = Liste de Class , StatCombat = Liste de donnée du combat)
    """
    Fenetre.blit( font.render( "tour " + str(StatCombat['NumerauxTourActuel']) , True , noir ) , [10, 10] ) # placement du nombre de tour
    Fenetre.blit( font.render( "Pv : " + str(Joueur.pv) + "/" + str(Joueur.pv_max) , True , noir ) ,  [10, 500] )

    # placement du fond d'ecran
    Fenetre.blit( pygame.image.load("data/fondcombatmap1.jpg").convert() , [0, 0])

    pygame.draw.rect(fenetre, blanc, [0, 590, 640, 50]) # dessin du menu de combat
    Fenetre.blit(Joueur.img_combat, Joueur.img_combat.get_rect(center=(100, 300))) # placement du joueur

    # placement des ennemis

    for i in range(len(Ennemi)):

        text_pv_ennemi_0 = font.render("Pv : "+str(ennemi[0].pv)+"/"+str(ennemi[0].pv_max),True,noir)
        Fenetre.blit(text_pv_ennemi_0, [500, 350])
        Fenetre.blit(ennemi[0].img_combat, ennemi[0].img_combat.get_rect(center=(500, 300)))