import pandas as pd
import numpy as np
import random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt 
from Joueur import Joueur
from Croupier import Croupier
from JeuDeCarte import JeuDeCarte

class __main__ :  
    
    michel=Joueur()
    croupier1=Croupier()
    jeu1 = JeuDeCarte()
    

    def main (self,Joueur,Croupier,JeuDeCarte):

        
        k=self.jeu1.getJdc()
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

        self.michel.setMain(joueur)
        
        self.croupier1.setMain(croupier)

        return joueur,croupier,k
    

    def total_main (self,main) :    
        
        total=0
            
        for key, val in main.items():
            total += val
                
        return total

    def tirer_nouvelle_carte(self,main, reste_carte):

        e=random.choice(list(reste_carte.items()))       
        reste_carte.pop(e[0])
        main[e[0]]= e[1]
        
        

        return main

    def affiche_mains_points (self,main_j,main_c) :
        print ('main joueur: ',main_j)
        print ('main croupier: ',main_c)
        print('total joueur : ',self.total_main(main_j))
        print('total croupier : ',self.total_main(main_c))

    def ass (self,main, total) :

        for i,j in main.items() :
            if j==11 and total>21:
                main[i]=1
        return main

    def blackjack (self,main,total) :
        if len(main)==2 and total==21 :
            return True     

    def jeu(self):    
        
        replay='o'

        while replay=='o' :

            mn=self.main(self.michel,self.croupier1,self.jeu1)
            reste_carte=mn[2]
            print('main joueur : ',mn[0])
            total_joueur = self.total_main(mn[0])
            total_croupier = self.total_main(mn[1])
            nouvellecarte='o'
            main_j=mn[0]
            main_c=mn[1]

            a=self.blackjack(main_j,total_joueur)
            b=self.blackjack(main_c,total_croupier)

            if a :
                print('Bravo BlackJack !!!!!!!')  
                self.affiche_mains_points(main_j,main_c)

            elif b :        
                print('Courtier : BlackJack !!!!!!!')  
                self.affiche_mains_points(main_j,main_c)
                
            else:        

                while total_croupier<17 or total_joueur<21 or nouvellecarte=='o':
                    

                    if total_joueur<21 or nouvellecarte =='o':

                        nouvellecarte=input("voulez vous une carte (o/n) ?")   
                            
                        if nouvellecarte == 'o' :
                            main_j = self.tirer_nouvelle_carte(mn[0],reste_carte)
                            total_joueur = self.total_main(main_j)
                            main_j=self.ass(main_j,total_joueur)
                            total_joueur = self.total_main(main_j)
                            if total_joueur>=21 :
                                nouvellecarte='n'
                            print('main joueur : ',main_j)
                        else :
                            main_j = mn[0]

                            #total_croupier= total_main(main[1])    

                        if total_croupier <17 :
                            main_c=self.tirer_nouvelle_carte(mn[1],reste_carte)
                            total_croupier = self.total_main(main_c)
                            main_c=self.ass(main_c,total_croupier)
                        else :
                                main_c=mn[1]   

                        if total_croupier>=17 and nouvellecarte != 'o' : 
                            break
                    else :
                        break

                self.affiche_mains_points(main_j,main_c)
                replay=input('voulez vous rejouer ? o/n')


        
    self.jeu()
    