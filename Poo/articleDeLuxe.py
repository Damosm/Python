from article import article

class articleDeLuxe (article):


    def __init__(self,reference,designation,prixHT,quantite):
        super().__init__(reference,designation,prixHT,quantite)
    
    def prixTTc(self, prixHT):
        return prixHT*1.05