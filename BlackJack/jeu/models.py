

class Joueur :

    mainn={}
    nom=""
    Parties_gagnees=""

    def getMain(self):
        return self.mainn

    def setMain(self, mainn):
        self.mainn = mainn
    
    def getNom(self) :
        return self.nom
    
    def setNom(self,nom):
        self.nom = nom

    def getPartie_gagnees(self):
        return self.Parties_gagnees

    def setPartie_gagnees(self,Parties_gagnees):
        self.Parties_gagnees = Parties_gagnees

    def __init__ (self) :               
        self.mainn={}
    
    def __str__(self):
        return self.nom


