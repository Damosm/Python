from animal import animal

class chien(animal):

    dureedevie=0

    def getDureedevie(self):
        return self.dureedevie
    
    def setDureedevie(self,dureedevie):
        self.dureedevie=dureedevie

    def __init__(self):
        super().__init__(20)
        self.dureedevie=15
    
    def afficher_duree_de_vie(self):
        print(chien.getDureedevie(self))

