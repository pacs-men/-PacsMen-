# -*- coding: utf-8 -*-

from Tkinter import *
import pickle

nombre_case = 50
l_case=10
largeur = nombre_case*l_case
hauteur = nombre_case*l_case

type_case = "herbe"
vitesse = 0
bouton_1 = False

pos_debut = (0, 0)
pos_fin = (0, 0)

dict_case = {"herbe":"green", "murs":"blue", "sols":"grey", "trous":"black"}

dict_obj = {"coffre":"brown", "Stalagmites" :"cyan", "ennemi":"red","porte":"white"}

def petit(a, b):
    if a<b:
        return a
    else:
        return b
      
def grand(a, b):
    if a>b:
        return a
    else:
        return b


def effobj():
    global type_case
    type_case = "effobj"
    

def lignes():
    for i in range(0,nombre_case*l_case,l_case):
        # les +2 sont à cause de Tkinter qui rajoute 2
        c.create_line(i+2, 0, i+2,nombre_case*l_case+2 , fill = "red")
        c.create_line(0, i+2, nombre_case*l_case+2, i+2, fill = "red")

def creer_fichier():
    with open("carte.mp", "wb") as fichier:
        pick = pickle.Pickler(fichier)
        pick.dump([m, l])

def c_matrice(N):
    m = []
    for i in range(N):
        m.append([])
        for j in range(N):
            m[i].append(type_case)
            
    return m
    
def afficher_matrice(m):
    for i in range(nombre_case):
        for j in range(nombre_case):
            case(i, j, dict_case[m[i][j]])            
            

def case(i, j, color):
    c.create_rectangle(i*l_case , j*l_case, (i*l_case)+l_case, (j*l_case)+l_case,fill = color)    

def c_matrice2(N):    
    l = []
    for x in range(N):
        l.append([])
        for y in range(N):
            l[x].append("")
    return l

def afficher_matrice2(l):
    for i in range(nombre_case):
        for j in range(nombre_case):
            ob = l[i][j]
            if ob!="":            
                objet(i, j, dict_obj[ob])

def click(event):
    global pos_debut
    global pos_fin
    pos_debut = (event.x/l_case, event.y/l_case)


def relache_1(event):   
    global bouton_1
    global m
    global pos_fin
    pos_fin = (event.x/l_case, event.y/l_case)
  
   
    for x in range(petit(pos_debut[0], pos_fin[0]), grand(pos_debut[0], pos_fin[0])+1):
        for y in range(petit(pos_debut[1], pos_fin[1]), grand(pos_debut[1], pos_fin[1])+1):                
            if type_case in dict_case.keys():
                m[x][y]=type_case
            elif type_case in dict_obj.keys():
                l[x][y] = type_case
            elif type_case == "effobj":
                l[x][y] = ""

def objet(x, y, color):
    c.create_rectangle(x*l_case+3, y*l_case+3, (x*l_case)+l_case-3, (y*l_case)+l_case-3,fill = color) 

def ch_lb(event):
    global type_case
    global listbox
    try:
        i = listbox.get(listbox.curselection())
        print i
        type_case = i
    except:
        print "probleme"
        
fenetre = Tk()

c = Canvas(fenetre, width= largeur, height= hauteur, bg= "black", borderwidth = -2)

c.bind("<Button-1>", click)
c.bind("<ButtonRelease-1>", relache_1)

listbox = Listbox(fenetre)
for a in dict_case.keys():
    listbox.insert(END, a)
    
for a in dict_obj.keys():
    listbox.insert(END, a)

listbox.pack(side = LEFT)

listbox.bind('<Button-1>', ch_lb)

RQ = Button(fenetre, text="quitter", command=fenetre.quit)
RQ.pack()
SAVE = Button(fenetre, text="sauvgarde_carte", command=creer_fichier)
SAVE.pack()
EFF = Button(fenetre, text="effacer objet", command=effobj)
EFF.pack()   
    
m = c_matrice(nombre_case)
print m
afficher_matrice(m)


l= c_matrice2(nombre_case)
afficher_matrice2(l)

lignes()

c.pack()

c.update()

fenetre.title('Editeur - Jeu PACSMEN')
while True:
    c.after(vitesse)
    afficher_matrice(m)
    afficher_matrice2(l)
    c.update()
    c.delete(ALL)
