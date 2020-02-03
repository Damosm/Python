"""
chaine = ["d","a","e","u","-","b"]

for c in chaine :
    print(c)

x = range(1,14,3)

for d in x :
    print(d)

s = [1,2,3,4,5,6,7,8,9,10]

for t in s :
    print(t)
    if t == 5 :
        break

for q in s :
    if q != 5 :
        print(q)
        continue
"""

n = int(input("entrez un nombre : "))
resultat = n

while n != 1 :
    

    resultat = resultat*(n-1)
    n=n-1
    print(n)
    print(resultat)
        
    continue

print(resultat)   