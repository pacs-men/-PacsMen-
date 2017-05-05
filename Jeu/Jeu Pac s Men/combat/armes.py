# -*- coding: utf-8 -*-

class arme:
    def __init__(self):
        self.atk=0
        self.mag=0
        
class Livre(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Livre Poussiéreux"
        self.atk=0
        self.mag=125
        
class Parchemin(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Parchemin des Arcanes"
        self.atk=0
        self.mag=150        
        
class Grimoire(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Grimoire de l'Archimage"
        self.atk=0
        self.mag=200      
        
class Dagues(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Dagues fendues"
        self.atk=100
        self.mag=0        
        
class LamesD(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Lames Dansantes"
        self.atk=150
        self.mag=0        
        
class Hachettes(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Hachettes Sanguinaires"
        self.atk=175
        self.mag=0       
        
class Epee(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Épée Rouillée"
        self.atk=75
        self.mag=0
        
class Hache(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Hache de Guerre"
        self.atk=150
        self.mag=0

class EpeeRL(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Épée Runique Légendaire"
        self.atk=150
        self.mag=50        
        
class LamesE(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Lames Empoisonnées"
        self.atk=0
        self.mag=100  
        
class Fouet(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Fouet de Soumission"
        self.atk=0
        self.mag=150          
       
class Crescent(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Crescent blade"
        self.atk=0
        self.mag=150 

class ArcL(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Arc long"
        self.atk=125
        self.mag=0

class Arbalete(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Arbalète de tueur d'ours"
        self.atk=150
        self.mag=0

class ArcA(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Arc d'Artémis"
        self.atk=200
        self.mag=0
        
class Baton(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Bâton tordu"
        self.atk=0
        self.mag=75

class Orbe(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Orbe de régénération"
        self.atk=0
        self.mag=125

class Sceptre(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Sceptre de l'Archange"
        self.atk=25
        self.mag=150 

class RubiksCube(arme):
    def __init__(self):
        arme.__init__(self)
        self.nom="Rubik's Cube"
        self.atk=20
        self.mag=0

