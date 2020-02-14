import math

class cercle:

    rayon=0

    def getRayon(self):
        return self.rayon
    def setRayon(self,rayon):
        self.rayon=rayon
    
    def __init__(self,rayon):
        self.rayon=rayon
    
    def surface (self):
        return (cercle.getRayon(self))**2*math.pi