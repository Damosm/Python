class article:

    reference=0
    designation=''
    prixHT=0
    quantite=0

    def getReference(self):
        return self.reference
    
    def setReference(self, reference):
        self.reference=reference
    
    def getDesignation(self):
        return self.designation
    
    def setDesignation(self,designation):
        self.designation= designation
    
    def getPrixHT(self):
        return self.prixHT

    def setPrixHT(self,prixHT):
        self.prixHT=prixHT
    
    def getQuantite(self):
        return self.quantite
    
    def setQuantite(self,quantite):
        self.quantite=quantite
    
    def __init__(self,reference,designation,prixHT,quantite):
        self.reference=reference
        self.designation=designation
        self.prixHT=prixHT
        self.quantite=quantite
    
    def prixTTc(self,prixHT):
        return prixHT*1.20
    
    def prixTransport(self,prixHT):
        return prixHT*0.05
    
    
        


