# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:44:33 2017

@author: pierre.aubinaud
"""

class potionvie:
    def __init__(self):
        self.pv=0
                
class PoVie1(potionvie):
    def __init__(self):
        potionvie.__init__(self)
        self.nom="potion de vie"
        self.pv=50
                       
class PoVie2(potionvie):
    def __init__(self):
        potionvie.__init__(self)
        self.nom="grande potion de vie"
        self.pv=100   
   
class PoVie3(potionvie):
    def __init__(self):
        potionvie.__init__(self)
        self.nom="Énorme potion de vie"
        self.pv=250
        
class potionforce:
    def __init__(self):
        self.atk=0
        self.mag=0
        
class PoForce1(potionforce):
    def __init__(self):
        potionvie.__init__(self)
        self.nom="potion de force"
        self.atk=50
        self.mag=50    
        
class PoForce2(potionforce):
    def __init__(self):
        potionvie.__init__(self)
        self.nom="grande potion de force"
        self.atk=100
        self.mag=100       
        
class PoForce3(potionforce):
    def __init__(self):
        potionvie.__init__(self)
        self.nom="Énorme potion de force"
        self.atk=150
        self.mag=150        
        
class potionarmure:
    def __init__(self):
        self.defend=0
        self.res=0
        
class PoArmure1(potionarmure):
    def __init__(self):
        potionarmure.__init__(self)
        self.nom="potion d'armure"
        self.defend=5
        self.res=5       
        
class PoArmure2(potionarmure):
    def __init__(self):
        potionarmure.__init__(self)
        self.nom="grande potion d'armure"
        self.defend=10
        self.res=10  
        
class PoArmure3(potionarmure):
    def __init__(self):
        potionarmure.__init__(self)
        self.nom="Énorme potion d'armure"
        self.defend=20
        self.res=20
        
class potioncritique:
    def __init__(self):
        self.crit=0
        
class PoCritique1(potioncritique):
    def __init__(self):
        potioncritique.__init__(self)
        self.nom="potion de critique"
        self.crit=5

class PoCritique2(potioncritique):
    def __init__(self):
        potioncritique.__init__(self)
        self.nom="grande potion de critique"
        self.crit=10      

class PoCritique3(potioncritique):
    def __init__(self):
        potioncritique.__init__(self)
        self.nom="Énorme potion de critique"
        self.crit=15        

class potionprecision:
    def __init__(self):
        self.vit=100
        
class potionvitesse:
    def __init__(self):
        self.prec=50   