# -*- coding: utf-8 -*-
import random
import pickle


nb_cell = [48, 48]

def creer_labyrinthe():
    
    mat = creer_matrice(nb_cell[0], nb_cell[1])
    x = random.randrange(nb_cell[0])
    y = random.randrange(nb_cell[1])
    
    mat[x][y] = 1
    ls_possible = [(x, y)]
        
    while ls_possible != []:
        effacer_coords(x, y, ls_possible)
        trouver_nv(x, y, mat, ls_possible)
        
        if ls_possible != []:
            (x, y) = random.choice(ls_possible)
            mat[x][y] = 1
    return mat
    
def creer_matrice(x, y):
    mat = []
    for i in range(x):
        mat.append([])
        for j in range(y):
            mat[i].append(0)
    return mat
    
def nb_voisin(x, y, mat):
    
    nb_voisin = 0
    voisins = ((0, 1), (1, 0), (0, -1), (-1, 0))
    for a in voisins:
        if x+a[0]>=0 and x+a[0]<nb_cell[0] and y+a[1]>=0 and y+a[1]<nb_cell[1]:
            nb_voisin += mat[x+a[0]][y+a[1]]
    
    return nb_voisin
    
        
def trouver_nv(x, y, mat, ls):
    voisins = ((0, 1), (1, 0), (0, -1), (-1, 0))
    for a in voisins:
        if x+a[0]>=0 and x+a[0]<nb_cell[0] and y+a[1]>=0 and y+a[1]<nb_cell[1]:
            if nb_voisin(x+a[0], y+a[1], mat) == 1 and mat[x+a[0]][y+a[1]] == 0:
                ls.append((x+a[0], y+a[1]))
    return ls

def effacer_coords(x, y, ls):
    voisins = ((0, 1), (1, 0), (0, -1), (-1, 0), (0, 0))
    for a in voisins:
        if (x+a[0], y+a[1]) in ls:
            ls.remove((x+a[0], y+a[1]))

def creer_mat_case(lab):
    matrice = []
    for x in range(50):
        matrice.append([])
        for y in range(50):
            matrice[x].append("mur")
    for x in range(24):
        for y in range(24):
            if lab[x][y] == 1:
                matrice[(x*2)+1][(y*2)+1] = "herbe"
    
    for x in range(1, 47, 2):
        for y in range(1, 47, 2):
            if matrice[x][y] == "herbe" and matrice[x+2][y] == "herbe":
                matrice[x+1][y] = "herbe"
                
            if matrice[x][y] == "herbe" and matrice[x][y+2] == "herbe":
                matrice[x][y+1] = "herbe"
    return matrice
    
def c_matrice2(N):    
    l = []
    for x in range(N):
        l.append([])
        for y in range(N):
            l[x].append("")
    return l

def creer_fichier():
    with open("carte.mp", "wb") as fichier:
        pick = pickle.Pickler(fichier)
        pick.dump([mat, c_matrice2(50)])


lab = creer_labyrinthe()
mat = creer_mat_case(lab)
print mat
creer_fichier()
