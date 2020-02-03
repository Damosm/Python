import numpy as np 
import math
"""
a = np.arange(16).reshape(4,4)
print(a)

b=np.rank(a)
print(b)

c=np.linalg.inv(a)
print(c)

d=np.linalg.det(a)
print(d)
#####################################

#ex1

n=5


def vecteur (n) :
    b=(2*n+1)
    a=np.arange(0)
    while b>0 :
        
        if b==n+1 :
            a=np.append(a,[1])
        else :
            a=np.append(a,[0])
        b=b-1
    return a


def vecteur2 (n) :
    b=(2*n+1)
    a=np.arange(0)
    while b>0 :       
       
        a=np.append(a,[1])
        b=b-1
    return a
#y=vecteur(n).reshape(1,2*n+1)
#z=vecteur(n).reshape(1,2*n+1)
#print(y)


def matrice (n) :
    a=vecteur(n).reshape(1,2*n+1)
    b=vecteur2(n).reshape(1,2*n+1)
    c=vecteur(n).reshape(1,2*n+1)
    #m=np.zeros((2*n+1)**2).reshape(2*n+1,2*n+1)    
    #a=np.ones(2*n+1).reshape(1,2*n+1)
    #b=np.ones(2*n+2).reshape(2*n+2,1)
    d=(2*n+1)
    
    while d>0 :

        if d==n+1 :
            c=np.concatenate((c,b),axis=0)
            d=d-1
        else :
            c=np.concatenate((c,a),axis=0)
            d=d-1
    #e=np.concatenate((c,b),axis=1)
    
    return c

print(matrice(n))
#####################################"
#ex2

n=10

def vecteur1 (n) :
    
    a=np.arange(0)
    while n>0 :       
       
        a=np.append(a,[1])
        n=n-1
    return a

def vecteur0 (n) :
    
    a=np.arange(0)
    while n>0 :       
       
        a=np.append(a,[0])
        n=n-1
    return a

def matrice (n) :
    
    a=vecteur1(n).reshape(1,n)
    e=np.ones(n-2)    
    c=vecteur1(n).reshape(1,n)    
    d=n-2
    diago=np.diag(e,2)
    c=np.concatenate((c,diago),axis=0)
    
    
    while d>=0 :

        if d==0 :
            c=np.concatenate((c,a),axis=0)
        d=d-1    
        
    return c

print(matrice(n))
########################################
ex3
"""
n=10

def matrice (n) :
    a=np.arange(0)
    f=np.arange(0)
    b=1
    e=n

    while e>0 :       
       
        a=np.append(a,[b])
        e=e-1
        b=b+1
    
    a=a.reshape(1,n)
    c=a 
    
    t=n  
    b=1
    g=0
    while t>0 :
        b=c[0,g]+1
        while n>0 :       
       
            f=np.append(f,[b])
            n=n-1
            b=b+1
        g=g+1
        n=10
        f=f.reshape(1,n)
        c=np.concatenate((c,f),axis=0)
        f=np.arange(0)
        t=t-1
        
    return c

#print(matrice(n))
############################
def melange (n) :
    b=matrice(n)
    np.random.shuffle(b)(n)
    return  b

#print(matrice(n))
#print(melange(n))
###########################################
#ex4

def somme_m (n) :
    a=matrice(n)
    print(a)
    b=0
    c=[]
    for i in range(len(a)) :
        #if i[0]==j[0] :
        #print(i)
        for k,l in enumerate(a[i]) :
            #print(l)
            if i==k :
                b=a[i,k]+a[k,i]
                c.append(b)
    return c

#print(somme_m(n))
###########################################
#ex4
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(m)
#print(m[::-1]) retourner matrice
#print(np.transpose(m))
