encore = "o"
while encore == "o" :

    moyenne = float(input("moyenne :"))

    if moyenne>=10 and moyenne<12 :
        print("vous étes reçu avec la mention passable")
    elif moyenne>=12 and moyenne<14:
        print("vous étes reçu avec la mention assez bien")
    elif moyenne>=14 and moyenne<16:
        print("vous étes reçu avec la mention bien")
    elif moyenne>=16 :
        print("vous étes reçu avec la mention trés bien")
    elif moyenne<10 :
        print("Vous n'etes pas reçu")
    """
    while encore != "o" or encore != "n" :

        encore = input("Voulez vous continuer ? ")
    """
    encore = input("Voulez vous continuer ? ")
    
print("au revoir")