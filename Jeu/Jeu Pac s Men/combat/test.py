# -*- coding: utf-8 -*-
import combat
'''
print "class joueur"
class_joueur=raw_input()
print "class enemi"
class_enemi=raw_input()

if class_joueur == "Mage":
    joueur=combat.Mage()
if class_joueur == "Combattant":
    joueur=combat.Combattant()
if class_joueur == "AssassinsMagique":
    joueur=combat.AssassinsMagique()
if class_joueur == "AssassinsPhysique":
    joueur=combat.AssassinsPhysique()
if class_joueur == "Archer":
    joueur=combat.Archer()
if class_joueur == "Soigneur":
    joueur=combat.Soigneur()

if class_enemi == "Mage":
   enemi=combat.Mage()
if class_enemi == "Combattant":
    enemi=combat.Combattant()
if class_enemi == "AssassinsMagique":
    enemi=combat.AssassinsMagique()
if class_enemi == "AssassinsPhysique":
    enemi=combat.AssassinsPhysique()
if class_enemi == "Archer":
    enemi=combat.Archer()
if class_enemi == "Soigneur":
    enemi=combat.Soigneur()
'''
'''
joueur=combat.AssassinsMagique()
enemi=combat.AssassinsPhysique()

tour=0


while joueur.pv > 0 and enemi.pv > 0:
    tour += 1
    
    if joueur.vit > enemi.vit:
        joueur.AttaqueMagique(enemi)
        if enemi.pv > 0:
            enemi.AttaquePhysique(joueur)
    else:
        enemi.AttaquePhysique(joueur)
        if joueur.pv > 0:
            joueur.AttaqueMagique(enemi)
    
    print ("tour "+str(tour))
    
if joueur.pv <= 0 and enemi.pv >= 0:
    
    print "perdu"
    print joueur.pv
    print enemi.pv
    
elif enemi.pv <= 0 and joueur.pv >= 0:
    
    print "gagner"
    print joueur.pv
    print enemi.pv
    
else:
    
    print "egalite"
    print joueur.pv
    print enemi.pv
'''

joueur=combat.AssassinsMagique()
enemi_1=combat.ennemi_test()
enemi_2=combat.ennemi_test()
enemi_3=combat.ennemi_test()
enemi_4=combat.ennemi_test()
armure=combat.TogeA()
arme=combat.Livre()
enemi=[enemi_1,enemi_2,enemi_3,enemi_4]
combat.combat_phase(joueur,arme,armure,enemi_1,"Magique",enemi)
print joueur.pv,enemi_1.pv,enemi_2.pv,enemi_3.pv,enemi_4.pv
enemi=[enemi_1,enemi_2,enemi_3,enemi_4]
combat.combat_phase(joueur,arme,armure,enemi_2,"Magique",enemi)
print joueur.pv,enemi_1.pv,enemi_2.pv,enemi_3.pv,enemi_4.pv
enemi=[enemi_1,enemi_2,enemi_3,enemi_4]
combat.combat_phase(joueur,arme,armure,enemi_3,"Magique",enemi)
print joueur.pv,enemi_1.pv,enemi_2.pv,enemi_3.pv,enemi_4.pv
enemi=[enemi_1,enemi_2,enemi_3,enemi_4]
combat.combat_phase(joueur,arme,armure,enemi_4,"Magique",enemi)
print joueur.pv,enemi_1.pv,enemi_2.pv,enemi_3.pv,enemi_4.pv
enemi=[enemi_1,enemi_2,enemi_3,enemi_4]
