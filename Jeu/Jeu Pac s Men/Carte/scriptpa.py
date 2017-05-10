import pygame
from pygame import *

pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme intro histoire')
pygame.font.init()
noir=(0,0,0)
blanc=(0xFF, 0xFF, 0xFF)
font = pygame.font.Font("data/fonts/old_london/OldLondon.ttf",25)

image=pygame.image.load("data/livreintroisn.png")
image1=pygame.image.load("data/imagepage1isn.jpg")
image2=pygame.image.load("data/page2isn.jpg")



pygame.display.flip()

continuer= True
page= 1

def script_pa(fenetre):
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                    continuer = False
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    page +=1
                if event.key == K_LEFT:
                    page -=1
                if event.key == K_ESCAPE:
                    continuer = False
        if page>5:
            page=5
        if page<1:
            page=1

        if page== 1:
                fenetre.blit(image,[0,110])
                text1g1 = font.render("Vous etes un ancien membre ",True,noir)
                fenetre.blit(text1g1,[45,145])
                text1g2 = font.render("d'une guilde nomme les Pac's ",True,noir)
                fenetre.blit(text1g2,[45,165])
                text1g3 = font.render("Men dont les membres ont ",True,noir)
                fenetre.blit(text1g3,[45,185])
                text1g4 = font.render("ete separes apres la defaite ",True,noir)
                fenetre.blit(text1g4,[45,205])                
                text1g5 = font.render("de l'armee de Denoma face ",True,noir)
                fenetre.blit(text1g5,[45,225])                
                text1g6 = font.render("a celle de Brigos. Pour ",True,noir)
                fenetre.blit(text1g6,[45,245])              
                text1g7 = font.render("echapper a l'esclavage ou a ",True,noir)
                fenetre.blit(text1g7,[45,265]) 
                text1g8 = font.render("l'execution des vaincus vous  ",True,noir)
                fenetre.blit(text1g8,[45,285]) 
                text1g9 = font.render("avez du vous enfuir, blesse ",True,noir)
                fenetre.blit(text1g9,[45,305]) 
                text1g10 = font.render("durant le combat. Vous avez",True,noir)
                fenetre.blit(text1g10,[45,325])                 
                text1g11 = font.render("du donner l'equipement qu'il ",True,noir)
                fenetre.blit(text1g11,[45,345]) 
                text1g12 = font.render("vous restait pour vous faire",True,noir)
                fenetre.blit(text1g12,[45,365])
                text1g13 = font.render("soigner et survivre. Depuis",True,noir)
                fenetre.blit(text1g13,[45,385]) 
                text1g14 = font.render("vous travaillez en tant que ",True,noir)
                fenetre.blit(text1g14,[45,405])
                text1g15 = font.render("Page 1 ",True,noir)
                fenetre.blit(text1g15,[150,445]) 
                
                text1d1 = font.render("Bataille de Fraktia",True,noir)
                fenetre.blit(text1d1,[375,175])
                text1d2 = font.render("Page 2 ",True,noir)
                fenetre.blit(text1d2,[450,445])             
                fenetre.blit(image1,[365,205])
                
                
                
                
        if page== 2:
                
                fenetre.blit(image,[0,110])
                
                text2g1 = font.render("Ville d'Esthar",True,noir)
                fenetre.blit(text2g1,[100,175])                
                fenetre.blit(image2,[35,205])
                text2g2 = font.render("Page 3 ",True,noir)
                fenetre.blit(text2g2,[150,445])
                
                text2d1 = font.render("mercenaire tout en essayant ",True,noir)
                fenetre.blit(text2d1,[350,145])
                text2d2 = font.render("de retrouver les autres ",True,noir)
                fenetre.blit(text2d2,[350,165])
                text2d3 = font.render("membres de la guilde. Vous",True,noir)
                fenetre.blit(text2d3,[350,185])
                text2d4 = font.render("etes actuellement dans une ",True,noir)
                fenetre.blit(text2d4,[350,205])                
                text2d5 = font.render("taverne miteuse dans la ville",True,noir)
                fenetre.blit(text2d5,[350,225])                
                text2d6 = font.render("d'Esthar. Ville corrompue",True,noir)
                fenetre.blit(text2d6,[350,245])              
                text2d7 = font.render("par la cruaute d'Empyrion ",True,noir)
                fenetre.blit(text2d7,[350,265]) 
                text2d8 = font.render("celebre gouverneur de Brigos",True,noir)
                fenetre.blit(text2d8,[350,285]) 
                text2d9 = font.render("mis en place apres la prise",True,noir)
                fenetre.blit(text2d9,[350,305]) 
                text2d10 = font.render("de la ville qui torture lui-",True,noir)
                fenetre.blit(text2d10,[350,325])                 
                text2d11 = font.render("meme les personnes",True,noir)
                fenetre.blit(text2d11,[350,345]) 
                text2d12 = font.render("suspectees d'aider Denoma.",True,noir)
                fenetre.blit(text2d12,[350,365])

                
                text2d13 = font.render("Page 4 ",True,noir)
                fenetre.blit(text2d13,[450,445])  
                
                
        if page== 3:
                fenetre.blit(image,[0,110])
                text3 = font.render("jhgfd",True,noir)
                fenetre.blit(text3,[45,145])




        pygame.display.flip()

