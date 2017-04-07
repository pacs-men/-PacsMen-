# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 10:20:28 2017

@author: pierre.aubinaud
"""

def popo_actif(self):
    potion=self.action
    if potion == "vie1":
        self.pv += 50
        if self.pv > self.pv_max:
            self.pv = self.pv_max
            
    if potion == "vie2":
        self.pv += 100
        if self.pv > self.pv_max:
            self.pv = self.pv_max
            
    if potion == "vie3":
        self.pv += 250
        if self.pv > self.pv_max:
            self.pv = self.pv_max
            
    if potion == "force1":
        self.atk += 50 
    self.mag += 50  
    self.force1 =2
    self.force1fois +=1
    
    if potion == "force2": self.atk +=100
    self.mag +=100
    self.force1 =2
    self.force2fois +=1
    
    if potion == "force3": self.atk +=150
    self.mag +=150
    self.force3 =1  #"tour"
    self.force3fois +=1
    
    if potion == "armure1": self.defend +=5
    self.res +=5
    self.armure1 =2 #"tour"
    self.armure1fois +=1
    
    if potion == "armure2": self.defend +=10
    self.res +=10
    self.armure2 =2 #"tour"
    self.armure2fois +=1
    
    if potion == "armure3": self.defend +=20
    self.res +=20
    self.armure3 =1 #"tour"
    self.armure3fois +=1
    
    if potion == "critique1": self.crit += 5
    self.critique1 =4 #"tour"
    self.critique1fois +=1
    
    if potion == "critique2": self.crit += 10
    self.critique2 =3#"tour"
    self.critique2fois +=1
    
    if potion == "critique3": self.crit += 15
    self.critique3 =2 #"tour"
    self.critique3fois +=1    
    
    if potion == "vitesse": self.vit += 100
    self.vitesse =1 #"combat"
    self.vitessefois +=1
    
    if potion == "precision": self.prec += 15
    self.precision =1 #"combat"
    self.precisionfois +=1
    
    
def popo_def(self):
        if self.precisionfois > 0:
            if self.precision == 0:
                self.prec -= 10
                self.precisionfois -= 1
            else:
                self.precison -=1

        if self.vitessefois > 0:
            if self.vitesse == 0:
                self.vit -= 10
                self.vitessefois -= 1
            else:
                self.vitesse -=1

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
    
    
    
    
    
    
    
    