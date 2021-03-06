# -*- coding: utf-8 -*-
import random ,pygame,armes,armure
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
        self.arme=armes.arme()
        self.armure=armure.armure()
        self.type_action=None
        self.action=None
        self.cible=None
        
        #variable potion
        self.armure1=-1
        self.armure1fois=0
        self.armure2=-1
        self.armure2fois=0
        self.armure3=-1
        self.armure3fois=0
        self.force1=-1
        self.force1fois=0
        self.force2=-1
        self.force2fois=0
        self.force3=-1
        self.force3fois=0
        self.critique1=-1
        self.critique1fois=0
        self.critique2=-1
        self.critique2fois=0
        self.critique3=-1
        self.critique3fois=0
        self.vitesse=-1
        self.vitessefois=0
        self.precision=-1
        self.precisionfois=0
        
        #variable inventaire
        self.potionvie1=3
        self.potionvie2=2
        self.potionvie3=0
        self.potionarmure1=2
        self.potionarmure2=0
        self.potionarmure3=0
        self.potionforce1=1
        self.potionforce2=0
        self.potionforce3=0
        self.potioncritique1=1
        self.potioncritique2=0
        self.potioncritique3=0
        self.potionvitesse=0
        self.potionprecision=0
        self.arme_total=[armes.arme,armes.arme,armes.arme]
        self.armure_total=[armure.armure,armure.armure,armure.armure]
        
    def upgrade(self,niveau):
        self.arme = self.arme_total[niveau]()
        self.armure = self.armure_total[niveau]()

    def attaque(self):
        '''
            selection du type d'attaque
        '''
        if self.stun == True:
            self.stun = False
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
                if self.cible.defen+self.cible.armure.defen > 90:
                    self.cible.pv -= (self.atk+self.arme.atk)*(1-float(90)/100)
                else:
                    self.cible.pv -= (self.atk+self.arme.atk)*(1-float(self.cible.defen+self.cible.armure.defen)/100)
            else:
                if self.cible.defen+self.cible.armure.defen > 90:
                    self.cible.pv -= (self.atk+self.arme.atk)*(1-float(90)/100)*2
                else:
                    self.cible.pv -= (self.atk+self.arme.atk)*(1-float(self.cible.defen+self.cible.armure.defen)/100)*2
        if self.cible.pv < 0:
            self.cible.pv = 0
            
            
            
    def AttaqueMagique(self):
        '''
            execution d'une attaque magique
        '''
        if random.randrange(100)<self.prec:
            self.passif_attaque_def()
            if random.randrange(100)>self.crit:
                if self.cible.res+self.cible.armure.res > 90:
                    self.cible.pv -= (self.mag+self.arme.mag)*(1-float(90)/100)
                else:
                    self.cible.pv -= (self.mag+self.arme.mag)*(1-float(self.cible.res+self.cible.armure.res)/100)
                
            else:
                if self.cible.res+self.cible.armure.res > 90:
                    self.cible.pv -= (self.mag+self.arme.mag)*(1-float(90)/100)*2
                else:
                    self.cible.pv -= (self.mag+self.arme.mag)*(1-float(self.cible.res+self.cible.armure.res)/100)*2
        if self.cible.pv < 0:
            self.cible.pv = 0
                
                
                
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
            impact des altérations d'état
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
    
                    
    def popo_actif(self):
        potion=self.action
        if potion == "vie1" and self.potionvie1>0 and self.pv != self.pv_max:
            self.pv += 50
            if self.pv > self.pv_max:
                self.pv = self.pv_max
            self.potionvie1-=1
        
        if potion == "vie2" and self.potionvie2>0 and self.pv != self.pv_max: 
            self.pv += 100
            if self.pv > self.pv_max:
                self.pv = self.pv_max
            self.potionvie2-=1
        
        if potion == "vie3" and self.potionvie3>0 and self.pv != self.pv_max:
            self.pv += 250
            if self.pv > self.pv_max:
                self.pv = self.pv_max
            self.potionvie3-=1
        
        if potion == "force1" and self.potionforce1>0:
            self.atk += 50
            self.mag += 50
            self.force1 =2
            self.force1fois +=1
            self.potionforce1-=1
        
        if potion == "force2" and self.potionforce2>0: 
            self.atk +=100
            self.mag +=100
            self.force1 =2
            self.force2fois +=1
            self.potionforce2-=1
        
        if potion == "force3" and self.potionforce3>0: 
            self.atk +=150
            self.mag +=150
            self.force3 =1  #"tour"
            self.force3fois +=1
            self.potionforce3-=1
            
        if potion == "armure1" and self.potionarmure1>0: 
            self.defen +=5
            self.res +=5
            self.armure1 =2 #"tour"
            self.armure1fois +=1
            self.potionarmure1-=1
            
            
        if potion == "armure2" and self.potionarmure2>0: 
            self.defen +=10
            self.res +=10
            self.armure2 =2 #"tour"
            self.armure2fois +=1
            self.potionarmure2-=1
            
        if potion == "armure3" and self.potionarmure3>0: 
            self.defen +=20
            self.res +=20
            self.armure3 =1 #"tour"
            self.armure3fois +=1
            self.potionarmure3-=1
            
        if potion == "critique1" and self.potioncritique1>0: 
            self.crit += 5
            self.critique1 =4 #"tour"
            self.critique1fois +=1
            self.potioncritique1-=1
            
        if potion == "critique2" and self.potioncritique2>0: 
            self.crit += 10
            self.critique2 =3#"tour"
            self.critique2fois +=1
            self.potioncritique2-=1
            
        if potion == "critique3" and self.potioncritique3>0: 
            self.crit += 15
            self.critique3 =2 #"tour"
            self.critique3fois +=1
            self.potioncritique3-=1
        
        if potion == "vitesse" and self.potionvitesse>0: 
            self.vit += 100
            self.vitesse =1 #"combat"
            self.vitessefois +=1
            self.potionvitesse-=1
            
        if potion == "precision" and self.potionprecision>0: 
            self.prec += 15
            self.precision =1 #"combat"
            self.precisionfois +=1
            self.potionprecision-=1
            
    
    def popo_def(self):
        
        if self.critique3fois >= 0:
            if self.critique3 == 0:
                self.crit -= 15 * self.critique3fois
                self.critique3fois = 0
                self.critique3 -=1
            else:
                self.critique3 -=1
    
        if self.critique2fois >= 0:
            if self.critique2 == 0:
                self.crit -= 10 * self.critique2fois
                self.critique2fois = 0
                self.critique2 -=1 
            else:
                self.critique2 -=1    
    
        if self.critique1fois >= 0:
            if self.critique1 == 0:
                self.crit -= 5 * self.critique1fois
                self.critique1fois = 0
                self.critique1 -=1     
            else:
                self.critique1 -=1     

        if self.armure1fois >= 0:
            if self.armure1 == 0:
                self.defen -= 5 * self.armure1fois
                self.res -=5 * self.armure1fois
                self.armure1fois = 0
                self.armure1 -=1
            else:
                self.armure1 -=1  

        if self.armure2fois >= 0:
            if self.armure2 == 0:
                self.defen -= 10 * self.armure2fois
                self.res -= 10 * self.armure2fois
                self.armure2fois = 0
                self.armure2 -=1
            else:
                self.armure2 -=1      

        if self.armure3fois >= 0:
            if self.armure3 == 0:
                self.defen -= 20 * self.armure3fois
                self.res -= 20 * self.armure3fois
                self.armure3fois = 0
                self.armure3 -=1
            else:
                self.armure3 -=1     
    
        if self.force3fois >= 0:
            if self.force3 == 0:
                self.atk -= 150 * self.force3fois
                self.mag -= 150 * self.force3fois
                self.force3fois = 0
                self.force3 -=1
            else:
                self.force3 -=1       
     
        if self.force2fois >= 0:
            if self.force2 == 0:
                self.atk -= 100 * self.force2fois
                self.mag -= 100 * self.force2fois
                self.force2fois = 0
                self.force2 -=1      
            else:
                self.force2 -=1      
    
        if self.force1fois >= 0:
            if self.force1 == 0:
                self.atk -= 50 * self.force1fois
                self.mag -= 50 * self.force1fois
                self.force1fois = 0
                self.force1 -=1
            else:
                self.force1 -=1
                
    def popo_def_2(self):
        
        if self.precision == 1:
            self.precision -= 15 * self.precisionfois
            self.precisionfois = 0
            self.precision -=1
            
        if self.vitesse == 1:
            self.vitesse -= 15 * self.vitessefois
            self.vitessefois = 0
            self.vitesse -=1
            
class AssassinsMagique(perso):
    def __init__(self):
        perso.__init__(self)
        self.nom="Sebastien"
        self.classe="Assassin Magique"
        self.jouable=True
        self.pv_max=250
        self.pv=250
        self.atk=10
        self.mag=100
        self.defen=5
        self.res=5
        self.vit=80
        self.prec=100
        self.crit=10
        self.arme_total=[armes.LamesE,armes.Fouet,armes.Crescent]
        self.armure_total=[armure.Gilet,armure.Veste,armure.Armurean]
        self.image_complet = pygame.image.load("data/Sebastien/complet.png").convert_alpha()
        self.img_combat = self.image_complet.subsurface((64, 64*11, 64, 64))
        self.ls_haut = [self.image_complet.subsurface((64*i, 64*8, 64, 64)) for i in range(9)]
        self.ls_gauche = [self.image_complet.subsurface((64*i, 64*9, 64, 64)) for i in range(9)]
        self.ls_bas = [self.image_complet.subsurface((64*i, 64*10, 64, 64)) for i in range(9)]
        self.ls_droite = [self.image_complet.subsurface((64*i, 64*11, 64, 64)) for i in range(9)]
        self.ls_images = [self.ls_gauche, self.ls_droite, self.ls_haut, self.ls_bas]
        self.ls_anim=[self.image_complet.subsurface((64*i, 64*15, 64, 64)) for i in range(6)]
        self.ls_anim.append(self.ls_anim[5])
        self.ls_anim.append(self.ls_anim[4])
        self.ls_anim.append(self.ls_anim[3])
        self.ls_anim.append(self.ls_anim[2])
        self.ls_anim.append(self.ls_anim[1])
        self.ls_anim.append(self.ls_anim[0])
        
    def passif_attaque_def(self):
        self.pv += 5
        if self.pv > self.pv_max:
            self.pv = self.pv_max

class Mage(perso):
    
    def __init__(self):
        perso.__init__(self)
        self.nom="Emeric"
        self.classe="Mage"
        self.jouable=True
        self.pv_max=150
        self.pv=150
        self.atk=10
        self.mag=125
        self.defen=5
        self.res=10
        self.vit=80
        self.prec=95
        self.crit=10
        self.arme_total=[armes.Livre,armes.Parchemin,armes.Grimoire]
        self.armure_total=[armure.Robe,armure.TuniqueI,armure.TogeI]
        self.image_complet = pygame.image.load("data/Emeric/complet.png").convert_alpha()
        self.img_combat = self.image_complet.subsurface((64, 64*3, 64, 64))
        self.ls_haut = [self.image_complet.subsurface((64*i, 64*8, 64, 64)) for i in range(9)]
        self.ls_gauche = [self.image_complet.subsurface((64*i, 64*9, 64, 64)) for i in range(9)]
        self.ls_bas = [self.image_complet.subsurface((64*i, 64*10, 64, 64)) for i in range(9)]
        self.ls_droite = [self.image_complet.subsurface((64*i, 64*11, 64, 64)) for i in range(9)]
        self.ls_images = [self.ls_gauche, self.ls_droite, self.ls_haut, self.ls_bas]
        self.ls_anim=[self.image_complet.subsurface((64*i, 64*3, 64, 64)) for i in range(6)]
        self.ls_anim.append(self.ls_anim[5])
        self.ls_anim.append(self.ls_anim[4])
        self.ls_anim.append(self.ls_anim[3])
        self.ls_anim.append(self.ls_anim[2])
        self.ls_anim.append(self.ls_anim[1])
        self.ls_anim.append(self.ls_anim[0])
        
    def passif_attaque_def(self):
        if random.randrange(10)<1:
            self.cible.stun=True
        
        
class AssassinsPhysique(perso):
     def __init__(self):
        perso.__init__(self)
        self.nom="Nassim"
        self.classe="Assassin Physique"
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
        self.arme_total=[armes.Dagues,armes.LamesD,armes.Hachettes]
        self.armure_total=[armure.Tenue,armure.Manteau,armure.Armureco]
        self.image_complet = pygame.image.load("data/Nassim/complet.png").convert_alpha()
        self.img_combat = self.image_complet.subsurface((64, 64*15, 64, 64))
        self.ls_haut = [self.image_complet.subsurface((64*i, 64*8, 64, 64)) for i in range(9)]
        self.ls_gauche = [self.image_complet.subsurface((64*i, 64*9, 64, 64)) for i in range(9)]
        self.ls_bas = [self.image_complet.subsurface((64*i, 64*10, 64, 64)) for i in range(9)]
        self.ls_droite = [self.image_complet.subsurface((64*i, 64*11, 64, 64)) for i in range(9)]
        self.ls_images = [self.ls_gauche, self.ls_droite, self.ls_haut, self.ls_bas]
        self.ls_anim=[self.image_complet.subsurface((64*i, 64*15, 64, 64)) for i in range(6)]
        self.ls_anim.append(self.ls_anim[5])
        self.ls_anim.append(self.ls_anim[4])
        self.ls_anim.append(self.ls_anim[3])
        self.ls_anim.append(self.ls_anim[2])
        self.ls_anim.append(self.ls_anim[1])
        self.ls_anim.append(self.ls_anim[0])
        
     def passif_attaque_def(self):
        self.cible.saignement = 1
        
class Combattant(perso):
    def __init__(self):
        perso.__init__(self)
        self.nom="Pierre Antoine"
        self.classe="Combattant"
        self.jouable=True
        self.pv_max=450
        self.pv=450
        self.atk=75
        self.mag=10
        self.defen=10
        self.res=5
        self.vit=50
        self.prec=100
        self.crit=5
        self.arme_total=[armes.Epee,armes.Hache,armes.EpeeRL]
        self.armure_total=[armure.Armurecu,armure.Plastron,armure.Cuirasse]
        self.image_complet = pygame.image.load("data/PA/complet.png").convert_alpha()
        self.img_combat = self.image_complet.subsurface((70+190, 1990, 140, 60))
        self.ls_haut = [self.image_complet.subsurface((64*i, 64*8, 64, 64)) for i in range(9)]
        self.ls_gauche = [self.image_complet.subsurface((64*i, 64*9, 64, 64)) for i in range(9)]
        self.ls_bas = [self.image_complet.subsurface((64*i, 64*10, 64, 64)) for i in range(9)]
        self.ls_droite = [self.image_complet.subsurface((64*i, 64*11, 64, 64)) for i in range(9)]
        self.ls_images = [self.ls_gauche, self.ls_droite, self.ls_haut, self.ls_bas]
        self.ls_anim=[self.image_complet.subsurface((50+190*i, 1990, 200, 60)) for i in range(6)]
        self.ls_anim.append(self.ls_anim[5])
        self.ls_anim.append(self.ls_anim[4])
        self.ls_anim.append(self.ls_anim[3])
        self.ls_anim.append(self.ls_anim[2])
        self.ls_anim.append(self.ls_anim[1])
        self.ls_anim.append(self.ls_anim[0])


    def passif_def(self,adv):
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
        self.classe="Archer"
        self.jouable=True
        self.pv_max=100
        self.pv=100
        self.atk=125
        self.mag=10
        self.defen=5
        self.res=5
        self.vit=100
        self.prec=90
        self.crit=20
        self.arme_total=[armes.ArcL,armes.Arbalete,armes.ArcA]
        self.armure_total=[armure.Cape,armure.Justaucorps,armure.Cote]
        self.image_complet = pygame.image.load("data/Martin/complet.png").convert_alpha()
        self.img= pygame.image.load("data/perso.png").convert_alpha()
        self.img_combat = self.image_complet.subsurface(64*0, 64*19, 64, 64)
        self.ls_haut = [self.image_complet.subsurface((64*i, 64*8, 64, 64)) for i in range(9)]
        self.ls_gauche = [self.image_complet.subsurface((64*i, 64*9, 64, 64)) for i in range(9)]
        self.ls_bas = [self.image_complet.subsurface((64*i, 64*10, 64, 64)) for i in range(9)]
        self.ls_droite = [self.image_complet.subsurface((64*i, 64*11, 64, 64)) for i in range(9)]
        self.ls_images = [self.ls_gauche, self.ls_droite, self.ls_haut, self.ls_bas]
        self.cible2=None
        self.ls_anim=[self.image_complet.subsurface((64*i, 64*19, 64, 64)) for i in range(13)]
        self.ls_anim.append(self.ls_anim[2])
        self.ls_anim.append(self.ls_anim[1])
        self.ls_anim.append(self.ls_anim[0])
            
        
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
            if random.randrange(100)>self.crit:
                self.cible2.pv -= (self.atk+self.arme.atk)*(1-float(self.cible2.defen+self.cible2.armure.defen)/100)
            else:
                self.cible2.pv -= (self.atk+self.arme.atk)*(1-float(self.cible2.defen+self.cible2.armure.defen)/100)*2
        if self.cible2.pv < 0:
            self.cible2.pv = 0
            
            
            
    def AttaqueMagique2(self):
        '''
            execution d'une attaque magique
        '''
        if random.randrange(100)<self.prec:
            if random.randrange(100)>self.crit:
                self.cible2.pv -= (self.mag+self.arme.mag)*(1-float(self.cible2.res+self.cible2.armure.res)/100)
            else:
                self.cible2.pv -= (self.mag+self.arme.mag)*(1-float(self.cible2.res+self.cible2.armure.res)/100)*2
        if self.cible2.pv < 0:
            self.cible2.pv = 0
        
    def passif_def(self,adv):
        if len(adv) > 2:
            while 1:
                i=random.randrange(len(adv))
                if adv[i].jouable == False and adv[i] != self.cible:
                    self.cible2=adv[i]
                    self.attaque2()
                    break
                
        
        
class Soigneur(perso):
    def __init__(self):
        perso.__init__(self)
        self.nom="Clarisse"
        self.classe="Soigneur"
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
        self.arme_total=[armes.Baton,armes.Orbe,armes.Sceptre]
        self.image_complet = pygame.image.load("data/Emeric/complet.png").convert_alpha()
        self.img= pygame.image.load("data/perso.png").convert_alpha()
        self.img_combat = pygame.image.load("data/perso.png").convert_alpha()
        self.ls_haut = [self.image_complet.subsurface((64*i, 64*8, 64, 64)) for i in range(9)]
        self.ls_gauche = [self.image_complet.subsurface((64*i, 64*9, 64, 64)) for i in range(9)]
        self.ls_bas = [self.image_complet.subsurface((64*i, 64*10, 64, 64)) for i in range(9)]
        self.ls_droite = [self.image_complet.subsurface((64*i, 64*11, 64, 64)) for i in range(9)]
        self.ls_images = [self.ls_gauche, self.ls_droite, self.ls_haut, self.ls_bas]
    def passif_def(self,adv):
        self.pv += 15
        if self.pv>self.pv_max:
            self.pv=self.pv_max
        


class mobs(perso):
    def __init__(self):
        perso.__init__(self)
        self.nombre=1

    def cible_def(self, participant):
        '''        
            IA basique pour definir le type d'attaque
            des ennemis envers le joueur            
        '''
        if self.jouable==False:
            if self.atk > self.mag:
                self.action="Physique"
            else:
                self.action="Magique"
            for i in range (len(participant)):
                if participant[i].jouable==True:
                    self.cible=participant[i]


        
class Rats(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Rats"
        self.pv_max=70
        self.pv=70
        self.atk=15
        self.defen=5
        self.res=10
        self.vit=20
        self.nombre=4
        self.img = pygame.image.load("data/Ennemi/rat_carte.png").convert_alpha()
        self.img_combat = pygame.image.load("data/Ennemi/rat_combat.png").convert_alpha()
        
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
        self.img = pygame.image.load("data/Ennemi/goblin_carte.png").convert_alpha()
        self.img_combat = pygame.image.load("data/Ennemi/goblin_combat.png").convert_alpha()
                
class Aigles(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Aigles"
        self.pv_max=25
        self.pv=25
        self.atk=30
        self.mag=0
        self.defen=10
        self.res=0
        self.vit=120
        self.nombre=2
        self.img = pygame.image.load("data/Ennemi/aigle_carte.png").convert_alpha()
        self.img_combat = pygame.image.load("data/Ennemi/aigle_combat.png").convert_alpha()
        
class Slime(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Slime"
        self.pv_max=100
        self.pv=100
        self.atk=0
        self.mag=30
        self.defen=10
        self.res=20
        self.vit=40
        self.nombre=1
        self.img = pygame.image.load("data/Ennemi/slime_carte.png").convert_alpha()
        self.img_combat = pygame.image.load("data/Ennemi/slime_combat.png").convert_alpha()
        
class Centaures(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Centaures"
        self.pv_max=80
        self.pv=80
        self.atk=0
        self.mag=40
        self.defen=10
        self.res=20
        self.vit=70
        self.nombre=3
        self.img = pygame.image.load("data/perso.png").convert_alpha()
        self.img_combat = pygame.image.load("data/perso.png").convert_alpha()
               
class Loup_garou(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Loup Garou"
        self.pv_max=250
        self.pv=250
        self.atk=50
        self.mag=0
        self.defen=20
        self.res=10
        self.vit=70
        self.nombre=1
        self.img = pygame.image.load("data/Ennemi/loupgarou_carte.png").convert_alpha()
        self.img_combat = pygame.image.load("data/Ennemi/loupgarou_combat.png").convert_alpha()
        
class Araingnees(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Araingnees"
        self.pv_max=20
        self.pv=20
        self.atk=0
        self.mag=30
        self.defen=5
        self.res=5
        self.vit=120
        self.nombre=3
        self.img = pygame.image.load("data/Ennemi/araignee_carte.png").convert_alpha()
        self.img_combat = pygame.image.load("data/Ennemi/araignee_combat.png").convert_alpha()

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
        self.img = pygame.image.load("data/Ennemi/carapateur_carte.png").convert_alpha()
        self.img_combat = pygame.image.load("data/Ennemi/carapateur_combat.png").convert_alpha()
        
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
        self.img = pygame.image.load("data/perso.png").convert_alpha()
        self.img_combat = pygame.image.load("data/perso.png").convert_alpha()
        
class Treant(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Treant"
        self.pv_max=500
        self.pv=500
        self.atk=0
        self.mag=45
        self.defen=20
        self.res=25
        self.vit=10
        self.nombre=1
        self.img = pygame.image.load("data/Ennemi/treant_carte.png").convert_alpha()
        self.img_combat = pygame.image.load("data/Ennemi/treant_combat.png").convert_alpha()

        
class Geant(mobs):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Geant"
        self.pv_max=400
        self.pv=400
        self.atk=40
        self.mag=45
        self.defen=25
        self.res=20
        self.vit=10
        self.nombre=1
        self.img = pygame.image.load("data/Ennemi/geant_carte.png").convert_alpha()
        self.img_combat = pygame.image.load("data/Ennemi/geant_combat.png").convert_alpha()       
        
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
        self.img = pygame.image.load("data/perso.png").convert_alpha()
        self.img_combat = pygame.image.load("data/perso.png").convert_alpha()
        
        
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
        self.vit=90
        self.nombre=2
        self.img = pygame.image.load("data/perso.png").convert_alpha()
        self.img_combat = pygame.image.load("data/perso.png").convert_alpha()
        
class Boss(mobs):
    def __init__(self):
        mobs.__init__(self)

        
class Troll(Boss):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Troll"
        self.pv_max=1000
        self.pv=1000
        self.atk=85
        self.mag=0
        self.defen=60
        self.res=50
        self.vit=15
        self.img = pygame.image.load("data/perso.png").convert_alpha()
        self.img_combat = pygame.image.load("data/perso.png").convert_alpha()
        
class Chimere1(Boss):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Chimère Violette"
        self.pv_max=800
        self.pv=800
        self.atk=0
        self.mag=75
        self.defen=40
        self.res=50
        self.vit=40
        self.img = pygame.image.load("data/perso.png").convert_alpha()
        self.img_combat = pygame.image.load("data/perso.png").convert_alpha()
        
class Chimere2(Boss):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Gueule dentelée"
        self.pv_max=800
        self.pv=800
        self.atk=75
        self.mag=0
        self.defen=50
        self.res=40
        self.vit=40
        self.img = pygame.image.load("data/perso.png").convert_alpha()
        self.img_combat = pygame.image.load("data/perso.png").convert_alpha()
     
        
class Thunderlord(Boss):
    def __init__(self):
        mobs.__init__(self)
        self.nom="Thunderlord"
        self.pv_max=1500
        self.pv=1500
        self.atk=0
        self.mag=150
        self.defen=50
        self.res=55
        self.vit=45
        self.img = pygame.image.load("data/perso.png").convert_alpha()
        self.img_combat = pygame.image.load("data/perso.png").convert_alpha()

liste_boss = [[Troll], [Chimere1, Chimere2], [Thunderlord]]
