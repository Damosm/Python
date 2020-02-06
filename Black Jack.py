import pandas as pd
import numpy as np
import random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def jeu_de_carte () :
    
    dic={}
    type=['coeur','carreau','trefle','pique']
    nom=['as de ','2 de ','3 de ','4 de ','5 de ','6 de ','7 de ','8 de ','9 de ','10 de ','valet de ','dame de ','roi de ']
    valeur=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    for i in type :
        for j,k in zip(nom,valeur) :
            dic[j+i]=k
    return dic



def main ():
    k=jeu_de_carte()
    i=0
    joueur={}
    croupier={}
    
    while i<2 :
        e=random.choice(list(k.items()))       
        k.pop(e[0])
        joueur[e[0]]= e[1]

        e=random.choice(list(k.items()))
        k.pop(e[0])
        croupier[e[0]]= e[1]

        i=i+1

    return joueur,croupier,k


def total_main (main) :    
    
    total=0
        
    for key, val in main.items():
        total += val
            
    return total

def tirer_nouvelle_carte(main, reste_carte):

    e=random.choice(list(reste_carte.items()))       
    reste_carte.pop(e[0])
    main[e[0]]= e[1]
    
    

    return main

def affiche_mains_points (main_j,main_c) :
    print ('main joueur: ',main_j)
    print ('main croupier: ',main_c)
    print('total joueur : ',total_main(main_j))
    print('total croupier : ',total_main(main_c))

def ass (main, total) :

    for i,j in main.items() :
        if j==11 and total>21:
            main[i]=1
    return main

def blackjack (main,total) :
    if len(main)==2 and total==21 :
        return True     

def jeu ():    
    
    replay='o'

    while replay=='o' :

        mn=main()
        reste_carte=mn[2]
        print('main joueur : ',mn[0])
        total_joueur = total_main(mn[0])
        total_croupier = total_main(mn[1])
        nouvellecarte='o'
        main_j=mn[0]
        main_c=mn[1]

        a=blackjack(main_j,total_joueur)
        b=blackjack(main_c,total_croupier)

        if a :
            print('Bravo BlackJack !!!!!!!')  
            affiche_mains_points(main_j,main_c)

        elif b :        
            print('Courtier : BlackJack !!!!!!!')  
            affiche_mains_points(main_j,main_c)
            
        else:        

            while total_croupier<17 or total_joueur<21 or nouvellecarte=='o':
                

                if total_joueur<21 or nouvellecarte =='o':

                    nouvellecarte=input("voulez vous une carte (o/n) ?")   
                        
                    if nouvellecarte == 'o' :
                        main_j = tirer_nouvelle_carte(mn[0],reste_carte)
                        total_joueur = total_main(main_j)
                        main_j=ass(main_j,total_joueur)
                        total_joueur = total_main(main_j)
                        if total_joueur>=21 :
                            nouvellecarte='n'
                        print('main joueur : ',main_j)
                    else :
                        main_j = mn[0]

                        #total_croupier= total_main(main[1])    

                    if total_croupier <17 :
                        main_c=tirer_nouvelle_carte(mn[1],reste_carte)
                        total_croupier = total_main(main_c)
                        main_c=ass(main_c,total_croupier)
                    else :
                            main_c=mn[1]   

                    if total_croupier>=17 and nouvellecarte != 'o' : 
                        break
                else :
                    break

            affiche_mains_points(main_j,main_c)
            replay=input('voulez vous rejouer ? o/n')



jeu()

