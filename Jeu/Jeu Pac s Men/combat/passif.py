# -*- coding: utf-8 -*-
import combat

    #mage
    def AttaquePhysique(self,adversaire):
        if random.randrange(100)<self.prec:
            if random.randrange(100)>self.crit:
                adversaire.pv -= self.atk*(1-adversaire.defen/100)
            else:
                adversaire.pv -= self.atk*(1-adversaire.defen/100)*2
                
        if random.randrange(100) < 10:
            return true
        else:
            return false
            
    def AttaqueMagique(self,adversaire):
        if random.randrange(100)<self.prec:
            if random.randrange(100)>self.crit:
                adversaire.pv -= self.mag*(1-adversaire.res/100)
            else:
                adversaire.pv -= self.atk*(1-adversaire.defen/100)*2
                
        if random.randrange(100) < 10:
            return true
        else:
            return false
#combat
def combat(joueur,arme,armure,enemi_1,enemi_2,enemi_3,enemi_4):
    
    passif=0
    while joueur.pv > 0 and (enemi_1.pv > 0 and enemi_2 > 0 and enemi_3 > 0 and enemi_4 > 0):
        tour += 1
        
        if joueur.nom == "Pierre Antoine":
            if joueur.pv < 500*0.7 and passif == 0:
                joueur.defen == joueur.defen*2
                joueur.res == joueur.res*2
                passif += 1
            else:
                passif = 0
                
                
        if joueur.vit > enemi.vit:
            joueur.AttaqueMagique(enemi,arme)
            if enemi.pv > 0:
                enemi.AttaquePhysique(joueur,armure)
        else:
            enemi.AttaquePhysique(joueur,arme)
            if joueur.pv > 0:
                joueur.AttaqueMagique(enemi,armure)

























