from article import article

class vetement(article):

    taille=0
    coloris=''

    def getTaille(self):
        return self.taille
    def setTaille(self,taille):
        self.taille=taille
    
    def getcoloris(self):
        return self.coloris
    def setColoris(self,coloris):
        self.coloris=coloris
    
    def __init__(self,reference,designation,prixHT,quantite,taille,coloris):
        super().__init__(reference,designation,prixHT,quantite)
        self.taille=taille
        self.coloris=coloris