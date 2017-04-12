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

type_case = "Herbe"
vitesse = 1

def click(event):
    global m
    x = event.x/l_case
    y = event.y/l_case
    m[x][y]=type_case



def mur():
    global type_case
    type_case = "Mur"


    
def herbe():
    global type_case
    type_case = "Herbe"
    


def coffre():
    global type_case
    type_case = "Coffre"
    

def lignes():
    for i in range(0,nombre_case*l_case,l_case):
        # les +2 sont à cause de Tkinter qui rajoute 2
        c.create_line(i+2, 0, i+2,nombre_case*l_case+2 , fill = "red")
        c.create_line(0, i+2, nombre_case*l_case+2, i+2, fill = "red")

def creer_fichier():
    with open("carte.mp", "wb") as fichier:
        pick = pickle.Pickler(fichier)
        pick.dump(m)

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
            if m[i][j] == "Herbe":
                case(i,j, "green")
            elif m[i][j] == "Mur":
                case(i,j, "brown")
            elif m[i][j] == "Coffre":
                case(i,j, "white")
                

def case(i, j, color):
    c.create_rectangle(i*l_case, j*l_case, (i*l_case)+l_case, (j*l_case)+l_case,fill = color)    

fenetre = Tk()

c = Canvas(fenetre, width= largeur, height= hauteur, bg= "black", borderwidth = 0)

c.bind("<Button-1>", click)
M = Button(fenetre, text="mur", command=mur)
M.pack(side = RIGHT)
H = Button(fenetre, text="herbe", command=herbe)
H.pack(side = RIGHT)
Co = Button(fenetre, text="coffre",command=coffre)
Co.pack()
RQ = Button(fenetre, text="quitter", command=fenetre.quit)
RQ.pack()

RQ = Button(fenetre, text="sauvgarde_carte", command=creer_fichier)
RQ.pack()
    
m = c_matrice(nombre_case)
print m
lignes()
afficher_matrice(m)

c.pack()

c.update()

fenetre.title('Editeur - Jeu PACSMEN')
while True:
    c.after(vitesse)
    afficher_matrice(m)
    c.update()
    c.delete(ALL)
fenetre.mainloop()
