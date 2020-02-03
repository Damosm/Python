"""
a=5
b=2

if a==5 and b==2 :
    print("and == &")

a,b = 2,4

if a==4 or b!=4 :
    print("gagné")
elif a==4 or b==4:
    print("presque gagné")

a=False

if not a :
    print("gagné")
elif a :
    print("perdu")
#########################################################"
a,b,c=3,5,7
print(a-b//c)
print(type(a),type(b),type(c))

##########################################################""

a=0
b=32
chaine = range(a,b+1)
r=0
for i in chaine :
  
    if i%3==0 and i%5==0 :
        print(i)
        r=r+i
    
print(r)

#########################################################################""
a=0
b=32
chaine = range(a,b+1)
r=0
for i in chaine :
  
    if i%3==0 or i%5==0 :
        print(i)
        r=r+i
    
print(r)    
###############################################################################""
annee = int(input("entrez une année : "))

if annee%4==0  :
    print("cette annee est bissextile")
elif annee%100==0 and annee%400==0 :
    print("cette annee est bissextile")
elif annee%100==0 :
    print("Cette annee n'est aps bissextile")
else :
    print("Cette annee n'est aps bissextile")

################################################################################################"
choix = input("voulez vous ajouter une valeur à la liste ? o/n : ")
liste = []

while choix=="o" :

    valeur = int(input("entrez une valeur à ajouter à la liste : "))
    liste.append(valeur)
    choix = input("voulez vous ajouter une valeur à la liste ? o/n : ")

choix2 = int(input("Afficher la liste en colonne : 1"+"\n"+"Afficher la liste à l'envers : 2"+"\n"+"Compter le nombre de multiple de 3 : 3"
               +"\n"+"Calculer la somme de toutes les valeurs : 4"+"\n"+"Calculer le maximum et le minimum : 5"+"\n"+"Calculer le produit de toutes les valeurs : 6"+"\n"
               +"Entrez votre choix : "))

if choix2==1 :
    for t in liste :
        print(t)
elif choix2==2 :
    liste.reverse()
    for t in liste :
        print(t)
elif choix2==3 :
    i=0
    for t in liste :
        if t%3==0 :
            i=i+1
    print(i)
elif choix2==4 :
    i=0
    for t in liste :
        i=i+t
    print(t)
elif choix2==5 :
    i=max(liste)
    t=min(liste)
    print("max = ",i,"\n","min = ",t)
elif choix2==6 :
    i=1
    for t in liste :
        i=i*t
    print(i)

#############################################
nom = input("Entrez votre nom : ")
sexe = input("Sexe m/f: ")

if sexe=="m" :
    print("cher Monsieur ",nom)
elif sexe=="f" :
    print("chere Madame", nom)
#########################################



n=int(input("nombre de valeurs :"))

liste=[]

def distance(z) :
    x=0.05*2**z
    return x

def force(d) :
    f=(6.67*10**-11)*((10000*10000)/d**2)
    return f

i=0

while i<=n :

    x=distance(i)   
    liste.append(x)

    i=i+1


for s in liste: 
       
     f = force(s)
     print(s)
     print(f)
########################################

n=int(input('entrez le nombre de notes : '))

notes=[]
i=0

while i<=n :
    x=int(input('entrez votre note : '))
    notes.append(x)
    i+=1



def moyenne (liste_notes) :
    s=sum(liste_notes)
    q=len(liste_notes)
    m=s/q
    
    return m

m=moyenne(notes)

def admis (m) :
    if m>=10 :
        a='vrai'
        return a
        
    else :
        f='faux'
        return f

a=admis(m) 

def mention (m) :
    if m>=10 and m<12 :
        p='passable'
        return p
    elif m>=12 and m<14 :
        ab='assez bien'
        return ab
    elif m>=14 and m<16 :
        b='bien'
        return b
    elif m>=16 :
        tb='tres bien'
        return tb
    elif m<10 :
        n='pas de mention'
        return n

c=mention(m)

print('moyenne : ', m,'\n','resultat : ',a,'\n','mention : ',c)
        



list=['mardi','lundi',2,'janvier']

list[0]
list[-1]

list.insert(0,'mardi')

list3=3*list

for i in list3 :
    print('liste3',i)

x=len(list)
print(x)
################################################

secondes=int(input('entrez un nombre de secondes : '))

heures=secondes/3600

if secondes%3600 != 0 and secondes%60 != 0:
    minutes = (secondes//60)-((secondes//3600)*60)
    secondes = (secondes)-((secondes//60)*60)
    print (int(heures),' heure(s) et ',int(minutes),' minutes et ',secondes,' secondes')
elif secondes%3600 != 0 and secondes%60 == 0:
    minutes = (secondes//60)-((secondes//3600)*60)
    print (int(secondes//3600),' heure(s) et ',int(minutes),' minutes')
elif secondes/60 < 60 :
    print(int(minutes,' minutes'))
else :
    print(int(heures),' heure(s)')
##########################################################

a=int(input('entrez une première longueur a : '))
b=int(input('entrez une deuxième longueur b : '))
c=int(input('entrez une troisième longueur c : '))

liste=[]
liste.append(a)
liste.append(b)
liste.append(c)

liste=sorted(liste)

def triangle_rect(liste) :
    h=liste[2]    
    a=liste[0]    
    b=liste[1]
    

    if h**2==((a**2)+(b**2)) :
        print('le triangle est rectangle')
    else :
        print('ça n est pas un traingle rectangle')
    
    

triangle_rect(liste)

##############################################"

binaire = input('entrez une valeur binaire : ')

liste = binaire.strip()

liste = list(map(int, liste))

l=len(liste)-1
t=0
resultat=0
for i in liste :
    formule=liste[t]*(2**l)
    resultat=resultat+formule
    t=t+1
    l=l-1

print('le nombre décimal est : ',resultat)

###########################################

decimal = int(input('entrez une valeur decimale : '))

liste=[256,128,64,32,16,8,4,2,1]
liste2=[]

for i in liste :
    if decimal//i != 0 :
        liste2.append(decimal//i)
        decimal=decimal-i
    else :
        liste2.append(decimal//i)

liste2 = list(map(str, liste2))
separateur = ''
x = separateur.join(liste2)
print('la valeur binaire est : ',x)
###################################################

liste=[800,3,5,6,42,56,8,7,5,42,4,521,45]
liste2=[]

def croissant(z) :
    liste2=sorted(z)
    return liste2

liste2=croissant(liste)

for i in liste2 :
    print(i)
#######################################################

liste=[788,3,5,6,42,56,8,7,5,42,4,521,45]
liste2=[]

def croissant(z) :
    liste2=sorted(z)
    return liste2

liste2=croissant(liste)

for i in liste :
    print(i)


for i in liste2 :
    print(i)
#################################################
"""

from random import *

liste=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
groupe1=[]
groupe2=[]
groupe3=[]
groupe4=[]
groupe5=[]
groupe6=[]


shuffle(liste)

groupe1=liste[0:4]
groupe1 = list(map(str, groupe1))
separateur = ','
a = separateur.join(groupe1)

groupe2=liste[4:8]
groupe2 = list(map(str, groupe2))
separateur = ','
b = separateur.join(groupe2)

groupe3=liste[8:12]
groupe3 = list(map(str, groupe3))
separateur = ','
c = separateur.join(groupe3)

groupe4=liste[12:16]
groupe4 = list(map(str, groupe4))
separateur = ','
d = separateur.join(groupe4)

groupe5=liste[16:20]
groupe5 = list(map(str, groupe5))
separateur = ','
e = separateur.join(groupe5)

groupe6=liste[20:24]
groupe6 = list(map(str, groupe6))
separateur = ','
f = separateur.join(groupe6)

print('Premier groupe : ', a)
print('Deuxième groupe : ', b)
print('Troisième groupe : ', c)
print('Quatrième groupe : ', d)
print('Cinquième groupe : ', e)
print('Sixième groupe : ', f)

