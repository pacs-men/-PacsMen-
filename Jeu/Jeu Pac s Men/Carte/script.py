# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 22:38:18 2017

@author: nassim
"""
#import sys
#print u"dépasse".encode( sys.stdout.encoding )

class script1:
    '''une ligne fait exactement 39 caractères avec les paramètres de bases des caracteres'''
    def __init__(self):
        self.page1 = "12345678901234567890123456789012345678901234567890123456789012345678901234567890"
        self.page2 = u"Vous êtes un ancien membre d’une guilde".encode('utf-8')
        self.page3 = "bla bla bla bla bla"
        self.page4 = "bla bla bla bla bla"
        self.page4 = "bla bla bla bla bla"

'''
Vous êtes un ancien membre d’une guilde
nommé les Pac’s Men dont les membres ont
été séparés après la défaite de l’armée
de Dénoma face à celle de Brigos. Pour
échapper à l’esclavage ou à l’exécution
des vaincus vous avez du vous enfuir,
blessé durant le combat. Vous avez du
donner l’équipement qu’il vous restait
pour vous faire soigner et survivre.
Depuis vous travaillez en tant que
mercenaire tout en essayant de
retrouver les autres membres de la
guilde.
Vous êtes actuellement dans une taverne
miteuse dans la ville d’Esthar. Ville
corrompue par la cruauté d’Empyrion
célèbre gouverneur de Brigos mis en
place après la prise de la ville qui
torture lui-même les personnes
suspectées d’aider Dénoma.
'''