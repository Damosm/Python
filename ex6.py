"""
stock={"crayon ":43 ," stylobleu ":23 ," stylorouge ":40 ,"gomme":12 ," regle ":25 , "compas":10}
commande1={"crayon ": 3 ," stylovert ":23 ,"gomme":22 ," regle ":5}
commande2={"crayon ": 3 ,"gomme":12 ,"compas":2}

def somm_commande(commande1,commande2) :
    commande_globale={}
    for i,j in commande1.items():
        commande_globale[i]=j
    for i,j in commande2.items():
        commande_globale[i]=j

    for i,j in commande1.items() :
        for k,l in commande2.items() :
            if i==k :
                commande_globale[i]=j+l
        
    return commande_globale

print(somm_commande(commande1,commande2))

############################################"
"""
e1={'alg' : 9.0 , 'python' : 15 , 'anglais' : 7 , 'cNum' : 15}
e2={'alg' : 8 , 'python' : 12 , 'anglais' : 12 , 'cNum' : 14 , 'proba' : 9 , 'SQL' : 11 , 'maths' : 10 }
coeffs={'alg':6 ,'python':6 ,'anglais':2 ,'cNum':4 ,'proba':6 ,'sql':4 , 'maths':2}
liste_etu=[e1,e2]
dico_etu={'e1':e1,'e2':e2}
mat='cNum'
z=0.5


def meilleur_note(dico_notes) :
    liste_matiere=[]
    liste_note=[]
    liste=[]
    for i,j in dico_notes.items() :
        liste_matiere.append(i)
        liste_note.append(j)
    a=max(liste_note)    
    for k,l in zip(liste_matiere,liste_note) :
        if a == l :
            liste.append(k)
    return liste

#print(meilleur_note(e1))
#################################################""

def sommecoef(etud) :
    liste=[]
    for i in coeffs.values() :
        liste.append(i)
    a=sum(liste)
    return a

#print(sommecoef(coeffs))

def moyennecoef (etud,coeffs) :
    liste_matiere=[]
    liste_note=[]
    liste=[]
    a=0
    
    for i,j in etud.items() :
        liste_matiere.append(i)
        liste_note.append(j)
    for k,l in coeffs.items() :
        for m,n in zip(liste_matiere,liste_note) :
            if k==m :
                liste.append(n*l)
                a=a+l
    b=sum(liste)
    m=b/a
    return m

#print(moyennecoef(e1,coeffs))

def recu(etud,coeffs) :
    a=moyennecoef(etud,coeffs)
    b=sommecoef(etud)
    c=''
    if a>=10 and b>=30 :
        c='reçu'
        return c
    elif b<30 :
        c='pas assez de notes'
        return c
    elif a<10 :
        c='recalé'
        return c

    
#print(recu(e1,coeffs))
#################################
def nb_recu(liste_etu,coeffs) :
    liste_recu=[]
    
    for i in liste_etu :
        a=recu(i,coeffs)
        if a=='reçu' :
            liste_recu.append(liste_etu.index(i))
    return liste_recu

def nb_recu1(dico_etu,coeffs) :
    liste_recu=[]
    
    for i,j in dico_etu.items() :
        a=recu(j,coeffs)
        if a=='reçu' :
            liste_recu.append(i)
    return liste_recu

#print(nb_recu(liste_etu,coeffs))
#print(nb_recu1(dico_etu,coeffs))

def modifierlesdicos(liste_etu,mat,z) :
    liste_matiere=[]
    liste_note=[]
    
    a=0
    for i in range(len(liste_etu)) :
        dic={}
        for t,j in liste_etu[i].items() :
            liste_matiere.append(t)
            liste_note.append(j)
            for k,l in zip((range(len(liste_matiere))),(range(len(liste_note)))) :
                if liste_matiere[k]==mat :
                    a=liste_note[l]*z
                    liste_note[k]=a
            for k,l in zip(liste_matiere,liste_note) :
                dic[k]=l                  
            liste_etu[i]=dic
    return liste_etu

def modifierlesdicos2(liste_etu,mat,z) :
    liste_matiere=[]
    liste_note=[]
    
    a=0
    for i,e in enumerate(liste_etu) :
        dic={}
        for t,j in e.items() :
            liste_matiere.append(t)
            liste_note.append(j)
            for k,(l,m) in enumerate(zip(liste_matiere,liste_note)) :
                if l==mat :
                    a=m*z
                    liste_note[k]=a
            for k,l in zip(liste_matiere,liste_note) :
                dic[k]=l                  
            liste_etu[i]=dic
    return liste_etu

#print(modifierlesdicos2(liste_etu,mat,z))
#########################################
dico={'chien' :'dog','rouge' :'red','deux' :'two'}


def invers (dico) :
    dico2 = {}
    for key, values in dico.items():
        dico2[values]=key   
    return dico2
 
#print(invers(dico))
###############################
dic= { 'jean' : 12 , 'pierre' : 12 , 'marc' : 12 , 'anne' : 17 , 'marie' : 7 , 'paul' : 8 , 'pascal' : 7}

def invers2 (dico) :
    dico2 = {}
    liste=[]
    liste2=[]
    dico3 = invers(dico)
    for i in dico3.keys() :
        liste2.append(i)
    
    for i in liste2 :
        liste=[]
      
        for key, values in dico.items():
           
            if values==i :
                    liste.append(key)
                    dico2[values]=liste          
      
    return dico2

print(invers2(dic))








