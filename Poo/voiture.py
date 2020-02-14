class voiture :

    marque = ""
    def getMarque (self) :
        return self.marque

    def setMarque (self,marque) :
        self.marque = marque

    modele = ""
    def getModele(self) :
        return self.modele

    def setModele (self,modele):
        self.modele = modele
    
    couleur = ""
    def getCouleur(self):
        return self.couleur

    def setCouleur(self,couleur) :
        self.couleur = couleur

    

    def __init__(self):
        
        self.marque = ""
        self.modele = "" 
        self.pays = ""
        

        