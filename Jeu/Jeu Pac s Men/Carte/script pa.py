import pygame
from pygame import *

pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme intro histoire')
pygame.font.init()
noir=(0,0,0)
blanc=(0xFF, 0xFF, 0xFF)
font = pygame.font.Font("data/OLondon_.otf",25)

image=pygame.image.load("data/livreintroisn.png")

fenetre.blit(image,[0,110])

pygame.display.flip()

continuer= True
page= 1
text5 = font.render("C'est l'Histoire ",True,noir)
fenetre.blit(text5,[45,145])

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
                continuer = False
        if event.type==KEYDOWN:
            if event.key==K_RIGHT:
                page +=1
            if event.key==K_LEFT:
                page -=1
        if page>10:
                page=10
        if page<1:
                page=1
        if page== 1:
                fenetre.blit(image,[0,110])
                text1g = font.render("C'est l'Histoire ",True,noir)
                fenetre.blit(text1,[45,145])
                text1d = font.render("Chocolat ",True,noir)
                fenetre.blit(text1,[145,145])
        if page== 2:
                fenetre.blit(image,[0,110])
                text2g = font.render("YOLOLOLO",True,noir)
                fenetre.blit(text2,[45,145])
        if page== 3:
                fenetre.blit(image,[0,110])
                text3 = font.render("YOLOLOLO",True,noir)
                fenetre.blit(text3,[45,145])




    pygame.display.flip()

