"""
vec = [-4,-2,0,2,4]

vec = [x**2 for x in vec]

for x in vec :
    print (x)

test = ['tata', 'titi', 'tutut']
test = [weapon.strip() for weapon in test]

for x in test :
    print (x)
#####################

def creer_pile() :
    pile = []

def est_vide(pile) : 
    if len(pile)==0 :
        print('la pile est vide')
    else :
        print('la pile nest pas vide')

def empiler (x, pile) :
    pile.append(x)

def depiler (x,pile) :
    x = pile.pop(pile[-1])
    return x
def sommet (pile) :
    return pile[-1]

def hauteur (pile) :
    return len(pile)
##############################
def creer_file() :
    file = []

def est_vide(file) : 
    if len(file)==0 :
        print('la file est vide')
    else :
        print('la file nest pas vide')

def emfiler (x, file) :
    file.insert(0,x)

def defiler (x,file) :
    x = pile.pop(pile[0])
    return x

def longueur (file) :
    return len(file)

###################

tuple = ('paul',2)
print(tuple)
####################

list_tuple = [(1,2),(3,4),(5,6)]
liste = []
t=0
for x in list_tuple :
   for i in x :
       liste.append(i)
   
    
for x in liste :
    print(x)
baskets = {'nike','adidas','nike','puma','adidas'}

print(baskets)
print('nike' in baskets)
###############

a = set('abracadabra')
print(a)
b= set('123456')
print(b)
######################

dic1 = {'chocolat':1.25,'nutella':2.55,'miel':4.52,'crambar':2.79}

def combien(dico) :
    return len(dico)


def moyenne(dico) :
    l = combien(dico)
    s = 0
    for i,k in dico.items() :
        s = s+k
    
    m = s/l
    return m



def moinscher(dico) :
    a = min(dico)
    return a

a= moinscher(dic1)
print(a)

def dollars(dico) :
    for i,k in dico.items() :
        a = k*1.13
        dico[i]=a
    return dico

a= dollars(dic1)
print(a)
#########################

texte = 'abracadaba_abracadabra'

def comptercars (texte) :
    d = dict()
    for c in texte:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

a= comptercars(texte)
print(a)
#############################"


paul = [1,42,1.70,70]
mathilde = [2,5,1.1,18]
pauline = [2,32,1.6,50]
andre = [1,68,1.73,80]
teo = [1,12,1.50,45]

dico = dict([('paul',paul),('mathilde',mathilde),('pauline',pauline),('andre',andre),('teo',teo)])


def age(dico,prenom) :

    for i in dico :
        if i == prenom :            
            a = dico[i][1]
            return a                       
            
        else :
            a= 0
    return a
    
#a = age(dico,'mathilde')
#print(a)



def nb_femme (dico) :
    f=0
    for i in dico :
        for t in dico[i] :
            if dico[i][0]==2 :
                f = f+1
            break
    return f
#b = nb_femme(dico)
#print(b)

def imc (taille, poids) :
   return poids/taille**2



def surpoids (dico) :    
    liste=[]
    for i in dico :
        for t in dico[i] :
            p = dico[i][3]
            t = dico[i][2]
            if imc(t,p) > 25 :
                liste.append(i)
            break
    return liste

#liste1 = surpoids(dico)
#print(liste1)

def plus1(dico) :
    for i in dico.keys() :
        for t in dico[i] :            
            dico[i][1]+=1            
            break

plus1(dico)
print(dico)
######################################

test1 = {'id1':232,'id2':156,'id3':237,'id4':123,'id5':176}

def moyenne(dico) :
    l = len(dico)
    s = 0
    for i,k in dico.items() :
        s = s+k
    
    m = s/l
    return m

#print(moyenne(test1))

def quiValide(dico) :
    liste=[]
    for i,k in dico.items() :
        if k>200 :
            liste.append(i)
    return liste

#print(quiValide(test1))

def maxi(dico) :
    liste=[]
    a= max(dico.values())
    for i,k in dico.items() :
        if a==k :
            liste.append(i)
    return liste

#print(maxi(test1))

def transfo(dico) :
    
    for i,k in dico.items() :
        if k>200 :
            dico[i]='valid'
    return dico

#print(transfo(test1))

def ajoute(nbpoints, ident, dico) :

    for i,k in dico.items() :
        if i == ident and k != 'valid':
            dico[i]=k+nbpoints
            transfo(dico)
            return dico

    for i,k in dico.items() :
        if i != ident : 
            dico[ident]=nbpoints
            transfo(dico)
            return dico         
    
    

print(ajoute(100,'id5',test1))

###########################################
"""

from random import *

caracterespermis = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']



def creercode(caracterespermis) :

    dic={}
    valeurs=[]
    a= ((len(caracterespermis)))      

    while a > 0 :
        b=randint(1,100)
        valeurs.append(b)
        a-=1

    for i,j in zip(caracterespermis,valeurs) :
        dic[i]=j
    return dic

message='bonjour monsieur'

def coder(message,dico) :
    liste = []
    liste_message=list(message)
    liste_message.remove(' ')
    for x in liste_message :
        for i,j in dico.items() :
            if x ==i :
                liste.append(j)
    return liste

#print(coder(message,creercode(caracterespermis)))
dico1= creercode(caracterespermis)

def inverse(dico) :
    liste=[]
    liste2=[]
    dico_inverse={}
    for i in dico.keys():
        liste.append(i)
    for j in dico.values() :
        liste2.append(j)
    for t, r in zip(liste,liste2) :
        dico_inverse[r]=t
    return dico_inverse



def decoder(message, dico) :
    liste = []
    liste_message=list(message)
    liste_message.remove(' ')
    for x in liste_message :
        for i,j in dico.items() :
            if x ==i :
                liste.append(j)
    return liste
message2=coder(message, dico1)
message3=",".join(message2)
print(message3)
print(decoder(message3,inverse(dico1)))