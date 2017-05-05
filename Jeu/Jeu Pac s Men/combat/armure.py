# -*- coding: utf-8 -*-

class armure:
    def __init__(self):
        self.defen=0
        self.res=0
        
        
        
class Robe(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Robe en coton"
        self.defen=0
        self.res=20         
        
class TuniqueI(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Tunique d'incantateur"
        self.defen=5
        self.res=25     
        
class TogeI(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Toge de l'Immortel"
        self.defen=10
        self.res=30      

class Tenue(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Tenue d'éclaireur"
        self.defen=10
        self.res=0
        
class Manteau(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Manteau de loup solitaire"
        self.defen=20
        self.res=5      
        
class Armureco(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Armure en cobalt éthérée"
        self.defen=30
        self.res=10        
        
class Armurecu(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Armure en cuir"
        self.defen=20
        self.res=5       
        
class Plastron(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Plastron de chevalier"
        self.defen=30
        self.res=10        
        
class Cuirasse(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Cuirasse en peau de dragon"
        self.defen=40
        self.res=15        
        
class Gilet(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Gilet d'amateur"
        self.defen=0
        self.res=10      
        
class Veste(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Veste de tueur nocturne"
        self.defen=5
        self.res=20
        
class Armurean(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Armure antique de démon"
        self.defen=10
        self.res=30    
        
class Cape(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Cape en tissu"
        self.defen=10
        self.res=0       
        
class Justaucorps(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Justaucorps en écailles"
        self.defen=15
        self.res=5
        
class Cote(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Côte de maille en mithril"
        self.defen=20
        self.res=10       
        
class TuniqueH(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="tunique d'Herbaliste"
        self.defen=5
        self.res=10         
        
class TogeA(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Toge d'amis de la nature"
        self.defen=10
        self.res=15
          
class Corset(armure):
    def __init__(self):
        armure.__init__(self)
        self.nom="Corset de déesse"
        self.defen=15
        self.res=20
