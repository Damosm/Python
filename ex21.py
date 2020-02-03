dommage =float(input("Dommages :"))

franchise = dommage*0.1

if franchise<15 :
    franchise=15
    print("La franchise est égale à 15€")
elif franchise>500 :
    franchise=500
    print("La franchise est égale à 500€")
else :
    print("La franchise est égale à ", franchise)

montant = dommage-franchise

if montant <=15 :
    print("vous n'avez droit à aucun remboursement!!!")
else :
    print("le montant remboursé est égale à :", montant, "€") 