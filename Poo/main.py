from voiture import voiture
from article import article
from stock import stock
from animal import animal
from chien import chien
from vetement import vetement
from articleDeLuxe import articleDeLuxe
from cercle import cercle
from cylindre import cylindre
from cone import cone


if __name__ == "__main__":
    
    """
    v1= voiture()
    v1.setMarque('Audi')
    v1.setModele("RS6")
    v1.setCouleur("Bleu")

    v2=voiture()
    v2.setMarque('bmw')
    v2.setModele('serie_1')
    v2.setCouleur('noire')

    v3 = voiture()
    v3.setMarque('renault')
    v3.setModele('scenic')
    v3.setCouleur('gris')

    tab=[v1,v2,v3]
    
    for i in tab :
        print(i.getCouleur())
  
a1=article(1,'tasse',5,10)
a2=article(2,'goblet',2,5)
s1=stock()
s1.ajouter(a1,s1)
s1.ajouter(a2,s1)

for i in s1.getStockage():    
    print(i.getDesignation())

s1.retirer(a1,s1)

for i in s1.getStockage():    
    print(i.getDesignation())

a3=vetement(3,'pull',20,6,4,'bleu')
a4=articleDeLuxe(4,'bague',200,2)
print(a4.prixTTc(a4.getPrixHT()))
print(a1.prixTTc(a1.getPrixHT()))
"""

c1=chien()

c1.afficher_duree_de_vie()
c1.crier()

"""
cercle1=cercle(5)
print(cercle1.surface())

cylindre1=cylindre(cercle1.getRayon(),10)
print(cylindre1.volume())

cone1=cone(cylindre1.getRayon(),cylindre1.getHauteur())
print(cone1.volume())
"""
