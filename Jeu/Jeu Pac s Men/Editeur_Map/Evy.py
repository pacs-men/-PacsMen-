# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ce script temporaire est sauvegardé ici :
C:\Users\sebastien.thao\.spyder2\.temp.py
"""

# -*- coding: utf-8 -*-

from Tkinter import *
import pickle

nombre_case = 50
l_case=10
largeur = nombre_case*l_case
hauteur = nombre_case*l_case

type_case = "herbe"

fenetre = Tk()
c = Canvas(fenetre, width= largeur, height= hauteur, bg= "black", borderwidth = 0)
c.pack(side = "left")
c.update()




vitesse = 1


def click(event):
    global m
    x = event.x/l_case
    y = event.y/l_case
    if type_case in ["herbe", "mur"]:
        m[x][y]=type_case
    elif type_case in ["coffre", "arbre", "pnj"]:
        l[x][y] = type_case


def mur():
    global type_case
    type_case = "mur"


    
def herbe():
    global type_case
    type_case = "herbe"
    


def coffre():
    global type_case
    type_case = "coffre"

def arbre():
    global type_case
    type_case = "arbre"
 
def pnj():
    global type_case
    type_case = "pnj"   

def lignes():
    for i in range(0,nombre_case*l_case,l_case):
        c.create_line(i+2, 0, i+2,nombre_case*l_case+2 , fill = "red")
        c.create_line(0, i+2, nombre_case*l_case+2, i+2, fill = "red")

def creer_fichier():
    with open("map1.mp", "wb") as fichier:
        #créer un objet pickler de paramètre fichier
        print m
        pick = pickle.Pickler(fichier)
        m2= [m,l] 
        pick.dump(m2)

def import_fichier():
    global m
    global l
    ml = pickle.load(open( "map1.mp", "rb"))
    print ml
    m = ml[0] 
    l = ml[1]
    
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
            if m[i][j] == "herbe":
                case(i,j, "green")
            elif m[i][j] == "mur":
                case(i,j, "brown")
            

def c_matrice2(N):    
    l = []
    for x in range(N):
        l.append([])
        for y in range(N):
            l[x].append("")
    return l

def afficher_matrice2(l):
    for x in range(nombre_case):
        for y in range(nombre_case):
            if l[x][y] == "coffre":
                objet(x,y, "red")
            elif l[x][y] == "arbre":
                objet(x,y, "blue" )
            elif l[x][y] == "pnj":
                objet(x,y, "black" )


def case(i, j, color):
    c.create_rectangle(i*l_case , j*l_case, (i*l_case)+l_case, (j*l_case)+l_case,fill = color)    
            
def objet(x, y, color):
    c.create_rectangle(x*l_case+3, y*l_case+3, (x*l_case)+l_case-3, (y*l_case)+l_case-3,fill = color) 
    
Mur = Button(fenetre, text="mur", command=mur)
Mur.pack(side= "top")  
Herb = Button(fenetre, text="herbe", command=herbe)
Herb.pack(side= "top")
Tree = Button(fenetre, text="arbre", command=arbre)
Tree.pack() 
Coffre = Button(fenetre, text="coffre",command=coffre)
Coffre.pack()
Pnj = Button(fenetre, text="Pnj", command=pnj)
Pnj.pack()
RQ = Button(fenetre, text="quitter", command=fenetre.destroy)
RQ.pack()
SAVE = Button(fenetre, text="sauvegarde_carte", command=creer_fichier)
SAVE.pack()
imp = Button(fenetre, text="map", command=import_fichier)
imp.pack()



lignes() 
m= c_matrice(nombre_case)
l= c_matrice2(nombre_case)
afficher_matrice(m)
afficher_matrice2(l)
c.bind("<Button-1>", click)
fenetre.title("Editeur - Jeu PACSMEN")

while True:
    c.after(vitesse)
    afficher_matrice(m)
    afficher_matrice2(l)
    c.update()
    c.delete(ALL)


fenetre.mainloop()
