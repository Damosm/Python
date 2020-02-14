from cylindre import cylindre

class cone(cylindre):

    def __init__(self, rayon, hauteur):
        super().__init__(rayon, hauteur)

    def volume(self):
        return (cylindre.volume(self))/3
