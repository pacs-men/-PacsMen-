import pygame
from pygame.locals import*

from carte import*
from objet import*

class case:
    def __init__(self):
        self.type = "case"
        self.marchable = True
        self.ouvrable = False
        self.chemin_image = ""
        self.rep = " "
        self.image = None
    
    def load_image(self):
        self.image = pygame.image.load(self.chemin_image)
        
    def __repr__(self):
        if self.dessus == None:
            return self.rep
        else:    
            return self.dessus.rep
        
    def __str__(self):
        return "case de type {} a la position {} \n marchable = {} ouvrable = {} l'image ce trouve en {}".format(
        self.type, self.pos, self.marchable, self.ouvrable, self.image)

      
class mur(case):
    def __init__(self):
      case.__init__(self)
      self.type = "mur"
      self.marchable = False
      self.rep = "M"
      self.chemin_image = "data/Mur.png"
      self.load_image()
      
class herbe1(case):
    def __init__(self):
      case.__init__(self)
      self.type = "herbe1"
      self.rep = "H"
      self.chemin_image = "data/Grass17.png"
      self.load_image()

class herbe2(case):
    def __init__(self):
      case.__init__(self)
      self.type = "herbe2"
      self.rep = "H"
      self.chemin_image = "data/Grass04.png"
      self.load_image()

class herbe3(case):
    def __init__(self):
      case.__init__(self)
      self.type = "herbe3"
      self.rep = "H"
      self.chemin_image = "data/Grass03.png"
      self.load_image()

class herbe4(case):
    def __init__(self):
      case.__init__(self)
      self.type = "herbe4"
      self.rep = "H"
      self.chemin_image = "data/Grass02.png"
      self.load_image()
