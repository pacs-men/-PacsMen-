#-----------------RUBIK'S CUBE-------------------------
import pygame
import random
import time
pygame.init()

#-----------------CREATION DU CUBE ET DES LISTE DE VARIABLES-------------

cube=[['C3N', 'A4N', 'C4N', 'A2N', 'M1N', 'A3N', 'C1N', 'A1N', 'C2N'],
      ['C3R', 'A4R', 'C4R', 'A2R', 'M1R', 'A3R', 'C1R', 'A1R', 'C2R'],
      ['C3B', 'A4B', 'C4B', 'A2B', 'M1B', 'A3B', 'C1B', 'A1B', 'C2B'],
      ['C3O', 'A4O', 'C4O', 'A2O', 'M1O', 'A3O', 'C1O', 'A1O', 'C2O'],
      ['C3V', 'A4V', 'C4V', 'A2V', 'M1V', 'A3V', 'C1V', 'A1V', 'C2V'],
      ['C3J', 'A4J', 'C4J', 'A2J', 'M1J', 'A3J', 'C1J', 'A1J', 'C2J'],
      [['', '', '']]]

couleur1={'noir':(0, 0, 0),
          'blanc':(255, 255, 255),
          'rouge':(255, 0, 0),
          'bleu':(0, 0, 255),
          'orange':(255, 128, 0),
          'vert':(0, 255, 0),
          'jaune':(255, 255, 0)}
          
couleur2={'N':'blanc',
          'R':'rouge',
          'B':'bleu',
          'O':'orange',
          'V':'vert',
          'J':'jaune'}

xy_cube=[10, 55, 100, 145, 190, 235, 280, 325, 370, 415, 460, 505, 550, 595, 640]

dxy_cube={'gx':15, 'gy':-45,
     'nx':-45, 'ny':45+12,
     'rx':0, 'ry':0,
     'bx':-45,'by':-30,
     'ox':-45*3+12, 'oy':-8,
     'vx':45, 'vy':0,
     'jx':0, 'jy':-45}

mouv=["R", "R'", "U", "U'", "L", "L'", "D", "D'", "F", "F'", "B", "B'"]

#listes de coordonnees pour la fonction affichage
#(et oui c'est de la compression manuelle et c'est extremement moche)
aff=[0, 14, 12, 10, 18]+[0]*4+[8]*3+[0, 6]+[0]*3+[2]+[4]*3+[6]+[5]*3
aff+=[6, 0, 0, 3, 6, 1, 0, 3, 6, 0, 0, 3, 6, 0, 6]+[0]*3+[2]+[4]*3
aff+=[6]+[5]*3+[6, 0, 1, 4, 7, 5]+[1, 4, 7, 0, 1, 4, 7, 0]+[6]+[0]*3
aff+=[6]+[4]*3+[6]+[5]*3+[6, 0]+[2, 5, 8, 0]*3+[0]*3+[4, 1]+[2]*3+[0]*5
aff+=[6]*3+[2, 3]+[1]*3+[6]*5+[0]*3+[2, 3, 0, 3, 6]+[0]*5+[6]*4+[3]+[1]*3
aff+=[6]*5+[0]*4+[4, 1, 4, 7]+[0]*5+[6]*4+[3]+[1]*3+[6]*5+[0]*4+[5, 2, 5, 8]
aff+=[0]*10+[2]*3+[0]*5+[6]*3+[3, 6]+[2]*3+[6]*5+[0]*6+[3, 6]+[0]*5+[6]*3
aff+=[3, 6, 2, 2]+[6]*6+[0]*3+[1, 0, 4, 7]+[0]*6+[6]*3+[3, 6, 2 ]+[6]*7+[0]*3
aff+=[2, 0, 8]+[0]*12+[2]+[0]*7+[6]*5+[3]+[6]*7+[0]*5+[6]+[0]*7+[6]*5+[3]
aff+=[6]*7+[0]*5+[7]+[0]*7+[6]*5+[3]+[6]*7+[0]*5+[8]+[0]*7
listg=[6]*3+[17]*3+[28]*3+([0]+[-11]+[-22])*3+[7, 8, 9, 6, 7, 8, 5, 6, 7]
listg+=([8]+[9]+[10])*3+[22]*3+[11]*3+[0]*3+([28, 39, 50])*3+[0]*3+[1]*3
listg+=[2]*3+[4, 3, 2, 5, 4, 3, 6, 5, 4]+[46]*3+[57]*3+[68]*3+([28]+[17]+[6])*3
listg+=[22]*3+[11]*3+[0]*3+([0]+[11]+[22])*3+[18]*3+[29]*3+[40]*3
listg+=([28]+[17]+[6])*3+[50]*3+[39]*3+[28]*3+([40]+[51]+[62])*3+[-22]*3
listg+=[-11]*3+[0]*3+([0]+[-11]+[-22])*3+[50]*3+[39]*3+[28]*3+([68]+[79]+[90])*3
listg+=([4]+[5]+[6])*3+[4]*3+[5]*3+[6]*3+([12]+[13]+[14])*3+[2]*3+[3]*3+[4]*3
listg+=([0]+[1]+[2])*3+[4]*3+[5]*3+[6]*3+([4]+[5]+[6])*3+[8]*3+[9]*3+[10]*3

#listes de valeurs pour les rotations/mouvement de base du cube
var_cube=[]
var1_cube=[]
for i in range(54):
    var_cube.append('')
    var1_cube.append(i)
var2_cube=[0]*9+[1]*9+[2]*9+[3]*9+[4]*9+[5]*9
var3_cube=[0, 1, 2, 3, 4, 5, 6, 7, 8]*6
varu=[0]*9+[1]*3+[2]*3+[3]*3+[4]*3+[0, 1, 2, 3, 4, 5, 6, 7, 8]+[0, 1, 2]*4
varu+=[6, 3, 0, 7, 4, 1, 8, 5, 2, 12, 13, 14, 15, 16, 17, 18, 19, 20, 9, 10, 11]
varf=[42, 39, 36, 43, 40, 37, 44, 41, 38, 15, 12, 9, 16, 13, 10, 17, 14, 11, 6]
varf+=[3, 0, 7, 4, 1, 8, 5, 2, 29, 32, 35, 28, 31, 34, 27, 30, 33, 51, 48, 45]
varf+=[52, 49, 46, 53, 50, 47, 24, 21, 18, 25, 22, 19, 26, 23, 20]
varr=[9, 10, 11, 12, 13, 14, 15, 16, 17, 45, 46, 47, 48, 49, 50, 51, 52, 53]
varr+=[24, 21, 18, 25, 22, 19, 26, 23, 20, 8, 7, 6, 5, 4, 3, 2, 1, 0, 38, 41]
varr+=[44, 37, 40, 43, 36, 39, 42, 35, 34, 33, 32, 31, 30, 29, 28, 27]

#-----------------FIN DES LISTES-----------------

#----------DEBUT DES FONCTIONS DE MOUVEMENT-----------

def fB3(): # f B' en langage universel (ou fw)
    for i in range(54):
        var_cube[var1_cube[i]]=cube[var2_cube[i]][var3_cube[i]]
    for i in range(54):
        cube[var2_cube[i]][var3_cube[i]]=var_cube[varf[i]]
        
def fB33(): # fw' en langage universel
    for i in range(3):
        fB3()
        
def rL3(): # r L' en langage universel (ou rw)
    for i in range(54):
        var_cube[var1_cube[i]]=cube[var2_cube[i]][var3_cube[i]]
    for i in range(54):
        cube[var2_cube[i]][var3_cube[i]]=var_cube[varr[i]]
    
def rL33(): # rw' en langage universel
    for i in range(3):
        rL3()
        
def uD3(): # u D' en langage universel (ou uw)
    rL33()
    fB3()
    rL3()    
    
def uD33(): # uw' en langage universel
    for i in range(3):
        uD3()
        
def U1(): # U en langage universel
    for i in range(21):
        var_cube[i]=cube[varu[i]][varu[i+21]]
    for i in range(21):
        cube[varu[i]][varu[i+21]]=var_cube[varu[i+21*2]]

def U3(): # U' en langage universel
    for i in range(3):
        U1()
    
def u1(): # u en langage universel
    D1()
    uD3()
    
def u3(): # u' en langage universel
    for i in range(3):
        u1()
        
def L1(): # L en langage universel
    fB3()
    U1()
    for i in range(3):
        fB3()

def L3(): # L' en langage universel
    for i in range(3):
        L1()
    
def l1(): # l en langage universel
    R1()
    for i in range(3):
        rL3()
    
def l3(): # l' en langage universel
    for i in range(3):
        l1()
        
def F1(): # F en langage universel
    rL3()
    U1()
    for i in range(3):
        rL3()
    
def F3(): # F' en langage universel
    for i in range(3):
        F1()
    
def f1(): # f en langage universel
    B1()
    fB3()
    
def f3(): # f' en langage universel
    for i in range(3):
        f1()
        
def R1(): # R en langage universel
    for i in range(3):
        fB3()
    U1()
    fB3()    

def R3(): # R' en langage universel
    for i in range(3):
        R1()
    
def r1(): # r en langage universel
    L1()
    rL3()
    
def r3(): # r' en langage universel
    for i in range(3):
        r1()
        
def B1(): # B en langage universel
    for i in range(3):
        rL3()
    U1()
    rL3()
    
def B3(): # B' en langage universel
    for i in range(3):
        B1()
    
def b1(): # b en langage universel
    F1()
    for i in range(3):
        fB3()
        
def b2(): # b2 en langage universel
    b1()
    b1()
        
def b3(): # b' en langage universel
    for i in range(3):
        b1()
        
def D1(): # D en langage universel
    fB3()
    fB3()
    U1()
    fB3()
    fB3()

def D3(): # D' en langage universel
    for i in range(3):
        D1()

def d1(): # d en langage universel
    U1()
    for i in range(3):
        uD3()
        
def d3(): # d' en langage universel
    for i in range(3):
        d1()
        
def M1(): # M' en langage universel mais chez moi c'est M
    r1()
    R3()
    
def M3(): # M en langage universel mais chez moi c'est M'
    for i in  range(3):
        M1()
        
#dictionnaire des fonctions de mouvements
dico_cube={"R":R1, "R'":R3, "r":r1, "r'":r3,
      "U":U1, "U'":U3, "u":u1, "u'":u3,
      "L":L1, "L'":L3, "l":l1, "l'":l3,
      "D":D1, "D'":D3, "d":d1, "d'":d3,
      "F":F1, "F'":F3, "f":f1, "f'":f3,
      "B":B1, "B'":B3, "b":b1, "b'":b3,
      "M":M1, "M'":M3,
      "rw":rL3, "rw'":rL33,
      "uw":uD3, "uw'":uD33,
      "fw":fB3, "fw'":fB33}

#----------FIN DES FONCTIONS DE MOUVEMENT-----------


#----------DEBUT DES FONCTIONS D'AIDE-----------

def afficher_cube():
    for i in range(9):
        pygame.draw.polygon(fenetre, couleur1[couleur2[cube[0][i][2]]], [[listg[i+18*0]+xy_cube[
        listg[i+18*1]]+dxy_cube['gx']+dxy_cube['nx'], listg[i+18*2]+xy_cube[listg[i+18*3]]+dxy_cube['gy']+dxy_cube[
        'ny']], [listg[i+18*4]+xy_cube[listg[i+18*1]]+dxy_cube['gx']+dxy_cube['nx'],listg[i+18*5]+xy_cube[listg[
        i+18*3]]+dxy_cube['gy']+dxy_cube['ny']], [listg[i+18*6]+xy_cube[listg[i+18*1]]+dxy_cube['gx']+dxy_cube['nx'
        ],listg[i+18*7]+xy_cube[listg[i+18*3]]+dxy_cube['gy']+dxy_cube['ny']], [listg[i+18*8]+xy_cube[listg[i+18*1]
        ]+dxy_cube['gx']+dxy_cube['nx'],listg[i+18*9]+xy_cube[listg[i+18*3]]+dxy_cube['gy']+dxy_cube['ny']]])
        pygame.draw.polygon(fenetre, couleur1[couleur2[cube[1][i][2]]], [[xy_cube[listg[i+18*10]
        ]+dxy_cube['gx']+dxy_cube['rx'], xy_cube[listg[i+18*10+9]]+dxy_cube['gy']+dxy_cube['ry']], [xy_cube[listg[i+18*10]
        ]+dxy_cube['gx']+dxy_cube['rx']+40, xy_cube[listg[i+18*10+9]]+dxy_cube['gy']+dxy_cube['ry']], [xy_cube[listg[i+18*10]
        ]+dxy_cube['gx']+dxy_cube['rx']+40, xy_cube[listg[i+18*10+9]]+dxy_cube['gy']+dxy_cube['ry']+40], [xy_cube[listg[i+18*10]
        ]+dxy_cube['gx']+dxy_cube['rx'], xy_cube[listg[i+18*10+9]]+dxy_cube['gy']+dxy_cube['ry']+40]])
        pygame.draw.polygon(fenetre, couleur1[couleur2[cube[2][i][2]]], [[listg[i+18*0+9]+xy_cube[
        listg[i+18*1+9]]+dxy_cube['gx']+dxy_cube['bx'], listg[i+18*2+9]+xy_cube[listg[i+18*3+9]]+dxy_cube['gy']+dxy_cube[
        'by']], [listg[i+18*4+9]+xy_cube[listg[i+18*1+9]]+dxy_cube['gx']+dxy_cube['bx'],listg[i+18*5+9]+xy_cube[
        listg[i+18*3+9]]+dxy_cube['gy']+dxy_cube['by']], [listg[i+18*6+9]+xy_cube[listg[i+18*1+9]]+dxy_cube['gx']+dxy_cube[
        'bx'],listg[i+18*7+9]+xy_cube[listg[i+18*3+9]]+dxy_cube['gy']+dxy_cube['by']], [listg[i+18*8+9]+xy_cube[listg[
        i+18*1+9]]+dxy_cube['gx']+dxy_cube['bx'],listg[i+18*9+9]+xy_cube[listg[i+18*3+9]]+dxy_cube['gy']+dxy_cube['by']]])
        pygame.draw.polygon(fenetre, couleur1[couleur2[cube[3][i][2]]], [[xy_cube[listg[i+18*11]
        ]+dxy_cube['gx']+dxy_cube['ox'], xy_cube[listg[i+18*11+9]]+dxy_cube['gy']+dxy_cube['oy']], [xy_cube[listg[i+18*11]
        ]+dxy_cube['gx']+dxy_cube['ox']+40, xy_cube[listg[i+18*11+9]]+dxy_cube['gy']+dxy_cube['oy']], [xy_cube[listg[i+18*11]
        ]+dxy_cube['gx']+dxy_cube['ox']+40, xy_cube[listg[i+18*11+9]]+dxy_cube['gy']+dxy_cube['oy']+40], [xy_cube[listg[i+18*11]
        ]+dxy_cube['gx']+dxy_cube['ox'], xy_cube[listg[i+18*11+9]]+dxy_cube['gy']+dxy_cube['oy']+40]])
        pygame.draw.polygon(fenetre, couleur1[couleur2[cube[4][i][2]]], [[xy_cube[listg[i+18*12]
        ]+dxy_cube['gx']+dxy_cube['vx'], xy_cube[listg[i+18*12+9]]+dxy_cube['gy']+dxy_cube['vy']], [xy_cube[listg[i+18*12]
        ]+dxy_cube['gx']+dxy_cube['vx']+40, xy_cube[listg[i+18*12+9]]+dxy_cube['gy']+dxy_cube['vy']], [xy_cube[listg[i+18*12]
        ]+dxy_cube['gx']+dxy_cube['vx']+40, xy_cube[listg[i+18*12+9]]+dxy_cube['gy']+dxy_cube['vy']+40], [xy_cube[listg[i+18*12]
        ]+dxy_cube['gx']+dxy_cube['vx'], xy_cube[listg[i+18*12+9]]+dxy_cube['gy']+dxy_cube['vy']+40]])
        pygame.draw.polygon(fenetre, couleur1[couleur2[cube[5][i][2]]], [[xy_cube[listg[i+18*13]
        ]+dxy_cube['gx']+dxy_cube['jx'], xy_cube[listg[i+18*13+9]]+dxy_cube['gy']+dxy_cube['jy']], [xy_cube[listg[i+18*13]
        ]+dxy_cube['gx']+dxy_cube['jx']+40, xy_cube[listg[i+18*13+9]]+dxy_cube['gy']+dxy_cube['jy']], [xy_cube[listg[i+18*13]
        ]+dxy_cube['gx']+dxy_cube['jx']+40, xy_cube[listg[i+18*13+9]]+dxy_cube['gy']+dxy_cube['jy']+40], [xy_cube[listg[i+18*13]
        ]+dxy_cube['gx']+dxy_cube['jx'], xy_cube[listg[i+18*13+9]]+dxy_cube['gy']+dxy_cube['jy']+40]])
        pygame.display.flip()

def lire_algo(a_cube):
    algo=''
    for i in a_cube:
        if i!=' ':
            algo+=i
        else:
            try:
                dico_cube[algo]()
            except:
                print 'Erreur.'
            algo=''

def etat_cube():
    a_cube=0
    for i in range(6):
        for j in range(9):
            if cube[i][j][2]==cube[i][0][2]:
                a_cube*=1
            else:
                a_cube+=1
    if a_cube==0:
        return 1

#creation de la fenetre d'affichage
fenetre = pygame.display.set_mode((640,640))
pygame.display.set_caption("----------------------------------------TRY TO SOLVE THE CUBE----------------------------------------")
fenetre.fill(couleur1['noir'])

#----------DEBUT DU CODE PRINCIPAL-----------

mv = pygame.image.load("tableau plein.png").convert()
fenetre.blit(mv, (88,432))
rg = pygame.image.load("rage.png").convert()
fenetre.blit(rg, (382,240))

cube_continuer=1
a_cube=""
for i in range(50):
    a_cube+=mouv[random.randint(0,11)]+' '
lire_algo(a_cube)

afficher_cube()
while cube_continuer:
    for event in pygame.event.get():
        a_cube=""
        if event.type == pygame.QUIT:
            cube_continuer = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0]>381 and event.pos[0]<582 and event.pos[1]>239 and event.pos[1]<388 and event.button==1:
                cube_continuer=0
            elif event.pos[0]>91 and event.pos[0]<148 and event.pos[1]>435 and event.pos[1]<492:
                if event.button==1:
                    a_cube="R "
                elif event.button==3:
                    a_cube="R' "
            elif event.pos[0]>151 and event.pos[0]<208 and event.pos[1]>435 and event.pos[1]<492:
                if event.button==1:
                    a_cube="U "
                elif event.button==3:
                    a_cube="U' "
            elif event.pos[0]>211 and event.pos[0]<268 and event.pos[1]>435 and event.pos[1]<492:
                if event.button==1:
                    a_cube="F "
                elif event.button==3:
                    a_cube="F' "
            elif event.pos[0]>271 and event.pos[0]<328 and event.pos[1]>435 and event.pos[1]<492:
                if event.button==1:
                    a_cube="L "
                elif event.button==3:
                    a_cube="L' "
            elif event.pos[0]>331 and event.pos[0]<388 and event.pos[1]>435 and event.pos[1]<492:
                if event.button==1:
                    a_cube="D "
                elif event.button==3:
                    a_cube="D' "
            elif event.pos[0]>391 and event.pos[0]<448 and event.pos[1]>435 and event.pos[1]<492:
                if event.button==1:
                    a_cube="B "
                elif event.button==3:
                    a_cube="B' "
            elif event.pos[0]>91 and event.pos[0]<148 and event.pos[1]>495 and event.pos[1]<552:
                if event.button==1:
                    a_cube="r "
                elif event.button==3:
                    a_cube="r' "
            elif event.pos[0]>151 and event.pos[0]<208 and event.pos[1]>495 and event.pos[1]<552:
                if event.button==1:
                    a_cube="u "
                elif event.button==3:
                    a_cube="u' "
            elif event.pos[0]>211 and event.pos[0]<268 and event.pos[1]>495 and event.pos[1]<552:
                if event.button==1:
                    a_cube="f "
                elif event.button==3:
                    a_cube="f' "
            elif event.pos[0]>271 and event.pos[0]<328 and event.pos[1]>495 and event.pos[1]<552:
                if event.button==1:
                    a_cube="l "
                elif event.button==3:
                    a_cube="l' "
            elif event.pos[0]>331 and event.pos[0]<388 and event.pos[1]>495 and event.pos[1]<552:
                if event.button==1:
                    a_cube="d "
                elif event.button==3:
                    a_cube="d' "
            elif event.pos[0]>391 and event.pos[0]<448 and event.pos[1]>495 and event.pos[1]<552:
                if event.button==1:
                    a_cube="M "
                elif event.button==3:
                    a_cube="M' "
            elif event.pos[0]>91 and event.pos[0]<208 and event.pos[1]>553 and event.pos[1]<612:
                if event.button==1:
                    a_cube="rw "
                elif event.button==3:
                    a_cube="rw' "
            elif event.pos[0]>211 and event.pos[0]<328 and event.pos[1]>553 and event.pos[1]<612:
                if event.button==1:
                    a_cube="uw "
                elif event.button==3:
                    a_cube="uw' "
            elif event.pos[0]>331 and event.pos[0]<448 and event.pos[1]>553 and event.pos[1]<612:
                if event.button==1:
                    a_cube="fw "
                elif event.button==3:
                    a_cube="fw' "
            
            lire_algo(a_cube)
            afficher_cube()
            if etat_cube()==1:
                print 'VICTOIRE'
                time.sleep(3)
                #----------------------------Martin c'est pour toi------------------------------------------
                cube_continuer=0 #Fermeture du programme