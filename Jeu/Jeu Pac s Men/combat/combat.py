# -*- coding: utf-8 -*-
import random ,pygame
from pygame.locals import *

class perso:
    def __call__(self):
        print "ceci est une fonction"
    
    def __init__(self):
        self.jouable=False
        self.pv_max=0
        self.pv=0       #brut
        self.atk=0      #brut
        self.mag=0      #brut
        self.defen=0    #pourcent
        self.res=0      #pourcent
        self.vit=0      #brut
        self.prec=100   #pourcent
        self.crit=0     #pourcent
        
        #variable passif
        self.passif=0
        self.stun=False
        self.effet=False
        self.brulure=0
        self.saignement=0
        
        #variable equipement
        self.arme=arme()
        self.armure=armure()
        self.type_action=None
        self.action=None
        self.cible=None
        
        #variable potion
        self.armure1=0
        self.armure1fois=0
        self.armure2=0
        self.armure2fois=0
        self.armure3=0
        self.armure3fois=0
        self.force1=0
        self.force1fois=0
        self.force2=0
        self.force2fois=0        
        self.force3=0
        self.force3fois=0
        self.critique1=0
        self.critique1fois=0                
        self.critique2=0
        self.critique2fois=0         
        self.critique3=0
        self.critique3fois=0 
        self.vitesse=0
        self.vitessefois=0
        self.precision=0
        self.precisionfois=0
        
        #variable inventaire
        self.potionvie1=0
        self.potionvie2=0
        self.potionvie3=0
        self.potionarmure1=0
        self.potionarmure2=0
        self.potionarmure3=0
        self.potionforce1=0
        self.potionforce2=0
        self.potionforce3=0
        self.potioncritique1=0
        self.potioncritique2=0
        self.potioncritique3=0
        self.potionvitesse=0
        self.potionprecision=0
        self.arme_total=[]
        self.armure_total=[]

    def attaque(self):
        '''
            selection du type d'attaque
        '''
        if self.stun == True:
            self.stun = False
            pass
        elif self.action == "Physique":
            self.AttaquePhysique()
        elif self.action == "Magique":
            self.AttaqueMagique()
        
        
        
    def AttaquePhysique(self):
        '''
            execution d'une attaque physique
        '''
        if random.randrange(100)<self.prec:
            self.passif_attaque_def()
            if random.randrange(100)>self.crit:
                self.cible.pv -= (self.atk+self.arme.atk)*(1-float(self.cible.defen+self.cible.armure.defen)/100)
            else:
                self.cible.pv -= (self.atk+self.arme.atk)*(1-float(self.cible.defen+self.cible.armure.defen)/100)*2
            
            
            
    def AttaqueMagique(self):
        '''
            execution d'une attaque magique
        '''
        if random.randrange(100)<self.prec:
            self.passif_attaque_def()
            if random.randrange(100)>self.crit:
                self.cible.pv -= (self.mag+self.arme.mag)*(1-float(self.cible.res+self.cible.armure.res)/100)
            else:
                self.cible.pv -= (self.mag+self.arme.mag)*(1-float(self.cible.res+self.cible.armure.res)/100)*2
                
                
                
    def passif_attaque_def(self):
        '''
            effet des passifs d'attaque
        '''
        pass
    
    def passif_def(self,adv):
        '''
            effet des passifs
        '''
        pass
    
    
    def effet_def(self):
        '''
            impact des alterations d'etat
        '''
        if self.effet==True:
            if self.brulure > 0:
                self.pv -= 5
                self.brulure -= 1
            elif self.saignement > 0:
                self.pv -= 10
                self.saignement -= 1
            else:
                self.effet=False
    
    
    
    def cible_def(self, participant):
        '''        
            IA basique pour definir le type d'attaque
            des enemis envers le joueur            
        '''
        if self.jouable==False:
            if self.atk > self.mag:
                self.action="Physique"
            else:
                self.action="Magique"
            for i in range (len(participant)):
                if participant[i].jouable==True:
                    self.cible=participant[i]
                    
    def popo_actif(self):
        potion=self.action
        if potion == "vie1" and self.potionvie1>0:
            self.pv += 50
            if self.pv > self.pv_max:
                self.pv = self.pv_max
                self.pv += 50
            self.potionvie1-=1
        
        if potion == "vie2"and self.potionvie2>0: 
            self.pv += 100
            if self.pv > self.pv_max:
                self.pv = self.pv_max
            self.potionvie2-=1
        
        if potion == "vie3"and self.potionvie3>0:
            self.pv += 250
            if self.pv > self.pv_max:
                self.pv = self.pv_max
            self.potionvie3-=1
        
        if potion == "force1"and self.potionforce1>0:
            self.atk += 50
            self.mag += 50  
            self.force1 =2
            self.force1fois +=1
            self.potionforce1-=1
        
        if potion == "force2"and self.potionforce2>0: 
            self.atk +=100
            self.mag +=100
            self.force1 =2
            self.force2fois +=1
            self.potionforce2-=1
        
        if potion == "force3"and self.potionforce3>0: 
            self.atk +=150
            self.mag +=150
            self.force3 =1  #"tour"
            self.force3fois +=1
            self.potionforce3-=1
            
        if potion == "armure1"and self.potionarmure1>0: 
            self.defend +=5
            self.res +=5
            self.armure1 =2 #"tour"
            self.armure1fois +=1
            self.potionarmure1-=1
            
        if potion == "armure2"and self.potionarmure2>0: 
            self.defend +=10
            self.res +=10
            self.armure2 =2 #"tour"
            self.armure2fois +=1
            self.potionarmure2-=1
            
        if potion == "armure3"and self.potionarmure3>0: 
            self.defend +=20
            self.res +=20
            self.armure3 =1 #"tour"
            self.armure3fois +=1
            self.potionarmure3-=1
            
        if potion == "critique1"and self.potioncritique1>0: 
            self.crit += 5
            self.critique1 =4 #"tour"
            self.critique1fois +=1
            self.potioncritique1-=1
            
        if potion == "critique2"and self.potioncritique2>0: 
            self.crit += 10
            self.critique2 =3#"tour"
            self.critique2fois +=1
            self.potioncritique2-=1
            
        if potion == "critique3"and self.potioncritique3>0: 
            self.crit += 15
            self.critique3 =2 #"tour"
            self.potioncritique3-=1
        
        if potion == "vitesse"and self.potionvitesse>0: 
            self.vit += 100
            self.vitesse =1 #"combat"
            self.vitessefois +=1
            self.potionvitesse-=1
            
        if potion == "precision"and self.potionprecision>0: 
            self.prec += 15
            self.precision =1 #"combat"
            self.precisionfois +=1
            self.potionprecision-=1
            
    
    def popo_def(self):
        
        if self.critique3fois > 0:
            if self.critique3 == 0:
                self.crit -= 15
                self.critique3fois -= 1
            else:
                self.critique3 -=1
    
        if self.critique2fois > 0:
            if self.critique2 == 0:
                self.crit -= 10
                self.critique2fois -= 1
            else:
                self.critique2 -=1    
    
        if self.critique1fois > 0:
            if self.critique1 == 0:
                self.crit -= 5
                self.critique1fois -= 1
            else:
                self.critique1 -=1     

        if self.armure1fois > 0:
            if self.armure1 == 0:
                self.defend -= 5
                self.res -=5
                self.armure1fois -= 1
            else:
                self.armure1 -=1  

        if self.armure2fois > 0:
            if self.armure2 == 0:
                self.defend -= 5
                self.res -=5
                self.armure2fois -= 1
            else:
                self.armure2 -=1      

        if self.armure3fois > 0:
            if self.armure3 == 0:
                self.defend -= 5
                self.res -=5
                self.armure3fois -= 1
            else:
                self.armure3 -=1     
    
        if self.force3fois > 0:
            if self.force3 == 0:
                self.atk -= 150
                self.mag -= 150
                self.force3fois -= 1
            else:
                self.force3 -=1       
     
        if self.force2fois > 0:
            if self.force2 == 0:
                self.atk -= 100
                self.mag -= 100
                self.force2fois -= 1
            else:
                self.force2 -=1      
    
        if self.force1fois > 0:
            if self.force1 == 0:
                self.atk -= 50
                self.mag -= 50
                self.force1fois -= 1
            else:
                self.force1 -=1
                
    def popo_def_2(self):
        
        if self.precision == 1:
            self.precision -= 15 * self.precisionfois
            self.precisionfois -= 1
            self.precision -=1
            
        if self.vitesse == 1:
            self.vitesse -= 15 * self.vitessefois
            self.vitessefois -= 1
            self.vitesse -=1
            
class AssassinsMagique(perso):
    def __init__(self):
        perso.__init__(self)
        self.nom="Sebastien"
        self.jouable=True
        self.pv_max=200
        self.pv=200
        self.atk=10
        self.mag=100
        self.defen=5
        self.res=5
        self.vit=80
        self.prec=100
        self.crit=10
        self.img= pygame.image.load("../data/perso.png").convert_alpha()
        
        def passif_attaque_def(self):
            self.pv += 5

class Mage(perso):
    
    def __init__(self):
        perso.__init__(self)
        self.nom="Emeric"
        self.jouable=True
        self.pv_max=100
        self.pv=100
        self.atk=10
        self.mag=125
        self.defen=5
        self.res=10
        self.vit=80
        self.prec=90
        self.crit=5
        self.img= pygame.image.load("data/perso.png").convert_alpha()
        
    def passif_attaque_def(self):
        if random.randrange(10)<1:
            self.cible.stun=True
        
        
class AssassinsPhysique(perso):
     def __init__(self):
        perso.__init__(self)
        self.nom="nassim"
        self.jouable=True
        self.pv_max=250
        self.pv=250
        self.atk=100
        self.mag=10
        self.defen=5
        self.res=5
        self.vit=80
        self.prec=100
        self.crit=10
        self.img= pygame.image.load("data/perso.png").convert_alpha()
        
     def passif_attaque_def(self):
        self.cible.saignement = 1
        
class Combattant(perso):
    def __init__(self):
        perso.__init__(self)
        self.nom="Pierre Antoine"
        self.jouable=True
        self.pv_max=500
        self.pv=500
        self.atk=75
        self.mag=10
        self.defen=10
        self.res=5
        self.vit=50
        self.prec=100
        self.crit=5
        self.img= pygame.image.load("data/perso.png").convert_alpha()
        
    def passif_def(self):
        if self.pv < 500*0.7 and self.passif == 0:
            self.defen == self.defen*2
            self.res == self.res*2
            self.passif += 1
        elif self.pv < 500*0.7 and self.passif != 0:
            pass
        else:
            self.defen == self.defen/2
            self.res == self.res/2
            self.passif = 0
        
class Archer(perso):
    def __init__(self):
        perso.__init__(self)
        self.nom="Martin"
        self.jouable=True
        self.pv_max=100
        self.pv=100
        self.atk=125
        self.mag=10
        self.defen=5
        self.res=5
        self.vit=100
        self.prec=95
        self.crit=20
        self.img= pygame.image.load("data/perso.png").convert_alpha()
        self.cible2=None
        
    def attaque2(self):
        '''
            selection du type d'attaque
        '''
        if self.stun == True:
            self.stun = False
            pass
        elif self.action == "Physique":
            self.AttaquePhysique2()
        elif self.action == "Magique":
            self.AttaqueMagique2()
        
        
        
    def AttaquePhysique2(self):
        '''
            execution d'une attaque physique
        '''
        if random.randrange(100)<self.prec:
            self.passif_attaque_def()
            if random.randrange(100)>self.crit:
                self.cible2.pv -= (self.atk+self.arme.atk)*(1-float(self.cible2.defen+self.cible2.armure.defen)/100)
            else:
                self.cible2.pv -= (self.atk+self.arme.atk)*(1-float(self.cible2.defen+self.cible2.armure.defen)/100)*2
            
            
            
    def AttaqueMagique2(self):
        '''
            execution d'une attaque magique
        '''
        if random.randrange(100)<self.prec:
            self.passif_attaque_def()
            if random.randrange(100)>self.crit:
                self.cible2.pv -= (self.mag+self.arme.mag)*(1-float(self.cible2.res+self.cible2.armure.res)/100)
            else:
                self.cible2.pv -= (self.mag+self.arme.mag)*(1-float(self.cible2.res+self.cible2.armure.res)/100)*2
        
    def passif_def(self,adv):
        while 1:
            i=random.randrange(len(adv))
            if adv[i].jouable == False and adv[i] != self.cible:
                self.cible2=adv[i]
                self.attaque2()
                
        
        
class Soigneur(perso):
    def __init__(self):
        perso.__init__(self)
        self.nom="Clarisse La BG"
        self.jouable=True
        self.pv_max=175
        self.pv=175
        self.atk=10
        self.mag=75
        self.defen=5
        self.res=5
        self.vit=30
        self.prec=95
        self.crit=0
        self.img= pygame.image.load("data/perso.png").convert_alpha()
        
    def passif_def(self,adv):
        self.pv += 15
        

class ennemi_test(perso):
    def __init__(self):
        perso.__init__(self)
        self.nom="test"
        self.pv_max=100
        self.pv=100
        self.atk=10
        self.vit=10
        self.img= pygame.image.load("data/perso.png").convert_alpha()

class mobs(perso):
    def __init__(self):
        perso.__init__(self)
        self.nombre=1
        
class Rats(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Rats"
        self.pv_max=50
        self.pv=50
        self.atk=15
        self.defen=5
        self.res=10
        self.vit=20
        self.nombre=4
        
class Gobelins(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Gobelins"
        self.pv_max=40
        self.pv=40
        self.atk=0
        self.mag=15
        self.defen=5
        self.res=10
        self.vit=40
        self.nombre=4
                
class Aigles(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Aigles"
        self.pv_max=25
        self.pv=25
        self.atk=40
        self.mag=0
        self.defen=10
        self.res=0
        self.vit=100
        self.nombre=2       
        
class Slime(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Slime"
        self.pv_max=90
        self.pv=90
        self.atk=0
        self.mag=30
        self.defen=10
        self.res=20
        self.vit=40
        self.nombre=1         
        
class Centaures(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Centaures"
        self.pv_max=80
        self.pv=80
        self.atk=0
        self.mag=50
        self.defen=10
        self.res=20
        self.vit=70
        self.nombre=3        
               
class Loup_garou(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Loup Garou"
        self.pv_max=200
        self.pv=200
        self.atk=60
        self.mag=0
        self.defen=25
        self.res=15
        self.vit=70
        self.nombre=1        
        
class Araingnees(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Araingnées"
        self.pv_max=20
        self.pv=20
        self.atk=0
        self.mag=20
        self.defen=5
        self.res=5
        self.vit=120
        self.nombre=3       
                
class Carapateur(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Carapateur"
        self.pv_max=300
        self.pv=300
        self.atk=0
        self.mag=0
        self.defen=25
        self.res=25
        self.vit=10
        self.nombre=1
        
class Golems(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Golem"
        self.pv_max=300
        self.pv=300
        self.atk=0
        self.mag=40
        self.defen=15
        self.res=25
        self.vit=20
        self.nombre=2          
        
class Treant(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Tréant"
        self.pv_max=500
        self.pv=500
        self.atk=0
        self.mag=45
        self.defen=20
        self.res=25
        self.vit=10
        self.nombre=1  
        
class Geant(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Géant"
        self.pv_max=400
        self.pv=400
        self.atk=40
        self.mag=45
        self.defen=25
        self.res=20
        self.vit=10
        self.nombre=1        
        
        
class Nains(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Nains"
        self.pv_max=100
        self.pv=100
        self.atk=40
        self.mag=0
        self.defen=20
        self.res=25
        self.vit=40
        self.nombre=3
        
class Elfs(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Elfs"
        self.pv_max=85
        self.pv=85
        self.atk=0
        self.mag=30
        self.defen=15
        self.res=30
        self.vit=80
        self.nombre=2

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
        
        
        
def combat_start(joueur,participant):
    ''' 
        fonction principale du combat 
        parametre: class joueur , liste des participants
        
        appelle la bonne fonction secondaire en fonction du type d'action du joueur
        trie les participants au combat selon leur vitesse
    '''
    if joueur.type_action == None:
        participant.sort(key=lambda v: v.vit)
        participant.reverse()
        combat_attaque(participant)
    
    if joueur.type_action == "potion":
        joueur.popo_actif()
        participant.sort(key=lambda v: v.vit)
        participant.reverse()
        combat_attaque(participant)
        
    if joueur.type_action == "attaque":
        participant.append(joueur)
        participant.sort(key=lambda v: v.vit)
        participant.reverse()
        combat_attaque(participant)
        participant.remove(joueur)
    
    
def combat_attaque(participant_vit):
    '''
        fonction dans laquelle le joueur attaque
        
        attaque de tous les participants dans l'ordre de vitesse + test de mort
    '''
    for i in range (len(participant_vit)):
        participant_vit[i].passif_def(participant_vit)
        if participant_vit[i].pv < 0:
            if participant_vit[i].jouable==True:
                break
            else:
                pass
            
        else:
            participant_vit[i].cible_def(participant_vit)
            participant_vit[i].attaque()
            participant_vit[i].popo_def()
            
            
    
    
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
        
def affiche_combat(fenetre,joueur,ennemi):
    continuer = 1
    position_bouton=1
    black=(0,0,0)
    blanc=(0xFF, 0xFF, 0xFF)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text1 = font.render("attaque",True,black)
    text2 =font.render("potion",True,black)
    text3 =font.render("fuite",True,black)
    text4 = font.render(ennemi[0].nom,True,black)
    text5 = font.render("attaque physique",True,black)
    text6 = font.render("attaque magique",True,black)

    fenetre.fill(blanc)
    while continuer == 1:
        if position_bouton == 1:
            pygame.draw.rect(fenetre, blanc, [210, 590, 190, 50], 3)
            pygame.draw.rect(fenetre, blanc, [100, 590, 110, 50], 3)
            pygame.draw.rect(fenetre, black, [0, 590, 100, 50], 3)
        if position_bouton == 2:
            pygame.draw.rect(fenetre, blanc, [0, 590, 100, 50], 3)
            pygame.draw.rect(fenetre, blanc, [210, 590, 190, 50], 3)
            pygame.draw.rect(fenetre, black, [100, 590, 110, 50], 3)
        if position_bouton == 3:
            pygame.draw.rect(fenetre, blanc, [100, 590, 110, 50], 3)
            pygame.draw.rect(fenetre, blanc, [0, 590, 100, 50], 3)
            pygame.draw.rect(fenetre, black, [210, 590, 190, 50], 3)
        fenetre.blit(text1, [10, 600])
        fenetre.blit(text2, [120, 600])
        fenetre.blit(text3, [230, 600])
        fenetre.blit(text4, [430, 600])
        pygame.draw.rect(fenetre, black, [0, 590, 640, 50], 1)
        pygame.draw.line(fenetre, black, [100, 590], [100, 640], 1)
        pygame.draw.line(fenetre, black, [210, 590], [210, 640], 1)
        pygame.draw.line(fenetre, black, [400, 590], [400, 640], 1)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_TAB:
                    continuer = 0
                if event.key == K_UP or event.key == K_RIGHT:
                    if position_bouton <3:
                        position_bouton += 1
                if event.key == K_DOWN or event.key == K_LEFT:
                    if position_bouton >1:
                        position_bouton -= 1

                if event.key == K_RETURN:

                    if position_bouton == 1:
                        joueur.action_type = "attaque"
                        while continuer == 1:
                            pygame.draw.rect(fenetre, blanc, [0, 585, 640, 55])
                            pygame.draw.rect(fenetre, black, [0, 590, 640, 50], 1)
                            pygame.draw.line(fenetre, black, [400, 590], [400, 640], 1)
                            pygame.draw.line(fenetre, black, [200, 590], [200, 640], 1)
                            fenetre.blit(text4, [430, 600])
                            fenetre.blit(text5, [10, 600])
                            fenetre.blit(text6, [210, 600])
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_TAB:
                                        continuer = 0
                                    if event.key == K_UP or event.key == K_RIGHT:
                                        if position_bouton <2:
                                            position_bouton += 1
                                    if event.key == K_DOWN or event.key == K_LEFT:
                                        if position_bouton >1:
                                            position_bouton -= 1
                                    if event.key == K_RETURN:
                                        if position_bouton == 1:
                                            joueur.action = "Physique"
                                        if position_bouton == 2:
                                            joueur.action = "Magique"
                                        select_ennemi(fenetre,joueur,ennemi)

                    if position_bouton == 2:
                        joueur.action_type = potion
                        while continuer == 1:

                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_TAB:
                                        continuer = 0

                    if position_bouton == 3:
                        while continuer == 1:

                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_TAB:
                                        continuer = 0


def select_ennemi(fenetre,joueur,ennemi):
    pass
