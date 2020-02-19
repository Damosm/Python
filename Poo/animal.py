class animal :

    couleur=''
    poids=0

    def getCouleur(self):
        return self.couleur
    def setCouleur(self,couleur):
        self.couleur=couleur

    def getPoids(self):
        return self.poids
    def setPoids(self,poids):
        self.poids=poids
     


    def __init__(self,poids):
        #self.couleur=couleur
        self.poids=poids
    
    def afficher_duree_de_vie(self):
        print(animal.getDureedevie(self))
    
    def crier(self):
        print("waaafff")
