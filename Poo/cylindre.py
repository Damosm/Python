from cercle import cercle

class cylindre(cercle):

    hauteur=0

    def getHauteur(self):
        return self.hauteur
    
    def setHauteur(self,hauteur):
        self.hauteur=hauteur
    
    def __init__(self, rayon, hauteur):
        super().__init__(rayon)
        self.hauteur=hauteur
    
    def volume(self):
        return cylindre.getHauteur(self)*cylindre.surface(self) 