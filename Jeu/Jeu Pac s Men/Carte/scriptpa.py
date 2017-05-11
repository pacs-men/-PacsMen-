import pygame
from pygame import *

pygame.init()
fenetre=pygame.display.set_mode((640,640))
pygame.display.set_caption('Programme intro histoire')
pygame.font.init()
noir=(0,0,0)
bleu=(0,0,160)
blanc=(0xFF, 0xFF, 0xFF)
font = pygame.font.Font("data/OLondon_.otf",25)
font2=pygame.font.SysFont('Calibri',20,True)
font3=pygame.font.SysFont('Calibri',20,True,True)


image=pygame.image.load("data/livreintroisn.png")
image1=pygame.image.load("data/imagepage1isn.jpg")
image3=pygame.image.load("data/taverne.jpg")
image2=pygame.image.load("data/page2isn.jpg")
noire=pygame.image.load("data/noir.png")
image4=pygame.image.load("data/devanttaverne.jpg")
image5=pygame.image.load("data/femmeauberge.jpg")
image6=pygame.image.load("data/hood.jpg")
image7=pygame.image.load("data/blancdialogue.jpg")
image8=pygame.image.load("data/plaine.png")

def script_pa(fenetre):
    fenetre.fill(noir)
    continuer= True
    page= 1
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
        if page>9:
            page=9
        if page<1:
            page=1

        if page== 1:
                fenetre.blit(noire,[0,0])
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
                fenetre.blit(noire,[0,0])                
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
                fenetre.blit(noire,[0,0])
                fenetre.blit(image,[0,110])
                text3g1 = font.render("Une jeune femme les larmes ",True,noir)
                fenetre.blit(text3g1,[45,145])
                text3g2 = font.render("aux yeux vient demander de",True,noir)
                fenetre.blit(text3g2,[45,165])
                text3g3 = font.render("l'aide dans la taverne, son",True,noir)
                fenetre.blit(text3g3,[45,185])
                text3g4 = font.render("ami Scrap, un petit golem ",True,noir)
                fenetre.blit(text3g4,[45,205])                
                text3g5 = font.render("de fer ne grace a la magie et ",True,noir)
                fenetre.blit(text3g5,[45,225])                
                text3g6 = font.render("possedant des capacites a ete ",True,noir)
                fenetre.blit(text3g6,[45,245])              
                text3g7 = font.render("capture par les sbires de ",True,noir)
                fenetre.blit(text3g7,[45,265]) 
                text3g8 = font.render("Thunderlord, un savant fou",True,noir)
                fenetre.blit(text3g8,[45,285]) 
                text3g9 = font.render("connu pour creer des mon-",True,noir)
                fenetre.blit(text3g9,[45,305]) 
                text3g10 = font.render("truosites. Les autres ",True,noir)
                fenetre.blit(text3g10,[45,325])                 
                text3g11 = font.render("mercenaires l'ecoute a peine ",True,noir)
                fenetre.blit(text3g11,[45,345]) 
                text3g12 = font.render("mais a un moment elle parle",True,noir)
                fenetre.blit(text3g12,[45,365])
                text3g13 = font.render("d'un chateau, celui de Gorfath",True,noir)
                fenetre.blit(text3g13,[45,385]) 
                text3g14 = font.render("dont elle a entendu les sbires ",True,noir)
                fenetre.blit(text3g14,[45,405])
                text3g15 = font.render("Page 5 ",True,noir)
                fenetre.blit(text3g15,[150,445])
                
                text3d1 = font.render("parler. Entendant cela vous ",True,noir)
                fenetre.blit(text3d1,[350,145])
                text3d2 = font.render("vous levez et allez la voir.",True,noir)
                fenetre.blit(text3d2,[350,165])

                text3d4 = font.render("Taverne des Cavaliers",True,noir)
                fenetre.blit(text3d4,[355,195])
                text3d5 = font.render("Page 6 ",True,noir)
                fenetre.blit(text3d5,[450,445])             
                fenetre.blit(image4,[365,225])
                
                
        if page== 4:
            fenetre.blit(image3,[0,0])
            fenetre.blit(image7,[0,490])
            fenetre.blit(image5,[520,490])
            fenetre.blit(image6,[0,490])
            text4d1 = font2.render("-Savez vous pourquoi il a capture ",True,noir)
            fenetre.blit(text4d1,[150,495])
            text4d2 = font2.render("votre ami ?",True,noir)
            fenetre.blit(text4d2,[150,515])
            text4d3 = font2.render("-Les hommes m'ont dit que",True,bleu)
            fenetre.blit(text4d3,[235,545])
            text4d4 = font2.render("Thunderlord voulait recuperer les",True,bleu)
            fenetre.blit(text4d4,[235,565])            
            text4d5 = font2.render("pouvoirs de Scrap pour pouvoir",True,bleu)
            fenetre.blit(text4d5,[235,585]) 
            text4d6 = font2.render("donner vie a ses creatures.",True,bleu)
            fenetre.blit(text4d6,[235,605])            
            
        if page== 5:
            fenetre.blit(image3,[0,0])
            fenetre.blit(image7,[0,490])
            fenetre.blit(image5,[520,490])
            fenetre.blit(image6,[0,490])
            text5d1 = font2.render("Vous avez parle du chateau de Gorfath ",True,noir)
            fenetre.blit(text5d1,[150,495])
            text4d2 = font2.render("que savez-vous de ce chateau ? ",True,noir)
            fenetre.blit(text4d2,[150,515])
            text4d3 = font2.render("-J'ai entendu les sbires parler",True,bleu)
            fenetre.blit(text4d3,[235,545])
            text4d4 = font2.render("d'une caverne sur le chemin.",True,bleu)
            fenetre.blit(text4d4,[235,565])            
            text4d5 = font2.render("Pouvez-vous m'aider ? ",True,bleu)
            fenetre.blit(text4d5,[235,585]) 
           
        if page== 6:
            fenetre.blit(image3,[0,0])
            fenetre.blit(image7,[0,490])
            fenetre.blit(image5,[520,490])
            fenetre.blit(image6,[0,490])
            text6d1 = font3.render("Vous connaissez ce chateau souterrain",True,noir)
            fenetre.blit(text6d1,[150,495])
            text6d2 = font3.render("vous y etes deja aller avec votre guilde.",True,noir)
            fenetre.blit(text6d2,[150,515])
            text6d3 = font3.render("Peut-etre certains y sont retournes.",True,noir)
            fenetre.blit(text6d3,[150,535])            
            text6d4 = font3.render("Vous decidez de tenter l'aventure. ",True,noir)
            fenetre.blit(text6d4,[150,555])
            
        if page== 7:
            fenetre.blit(image3,[0,0])
            fenetre.blit(image7,[0,490])
            fenetre.blit(image5,[520,490])
            fenetre.blit(image6,[0,490])
            text7d1 = font2.render("-Je vais y aller. ",True,noir)
            fenetre.blit(text7d1,[150,495])
            text7d2 = font2.render("-Merci beaucoup ! Je vais vous",True,bleu)
            fenetre.blit(text7d2,[235,525])
            text7d3 = font2.render("vous donner votre argent.",True,bleu)
            fenetre.blit(text7d3,[235,545])
            text7d4 = font2.render("-Vous me paierez si je reviens ",True,noir)
            fenetre.blit(text7d4,[150,575])
            text7d5 = font2.render("avec Scrap.",True,noir)
            fenetre.blit(text7d5,[150,595])
            
        if page== 8:
            fenetre.blit(image3,[0,0])
            fenetre.blit(image7,[0,490])
            fenetre.blit(image5,[520,490])
            fenetre.blit(image6,[0,490])
            text8d1 = font2.render("-D'accord si vous le voulez.",True,bleu)
            fenetre.blit(text8d1,[235,495])
            text8d2 = font2.render("-Je partirai demain a l'aube. ",True,noir)
            fenetre.blit(text8d2,[150,525])


        if page== 9:
                fenetre.blit(noire,[0,0])
                fenetre.blit(image,[0,110])
                text9g1 = font.render("Vous vous reveillez le",True,noir)
                fenetre.blit(text9g1,[45,145])
                text9g2 = font.render("lendemain vous allez aux",True,noir)
                fenetre.blit(text9g2,[45,165])
                text9g3 = font.render("portes de la ville. Vous",True,noir)
                fenetre.blit(text9g3,[45,185])
                text9g4 = font.render("partez vers le Nord en",True,noir)
                fenetre.blit(text9g4,[45,205])                
                text9g5 = font.render("direction de la caverne par la ",True,noir)
                fenetre.blit(text9g5,[45,225])                
                text9g6 = font.render("plaine de Briliance, le chemin",True,noir)
                fenetre.blit(text9g6,[45,245])              
                text9g7 = font.render("sera long et probablement",True,noir)
                fenetre.blit(text9g7,[45,265]) 
                text9g8 = font.render("seme d'ennemis ...",True,noir)
                fenetre.blit(text9g8,[45,285])
                     
                fenetre.blit(image8,[365,245])
                text9d9 = font.render("Plaine de Briliance",True,noir)
                fenetre.blit(text9d9,[375,215])
                
                text3g15 = font.render("Page 7 ",True,noir)
                fenetre.blit(text3g15,[150,445])
                
                text3d5 = font.render("Page 8 ",True,noir)
                fenetre.blit(text3d5,[450,445])                
                
                
                
                
        pygame.display.flip()