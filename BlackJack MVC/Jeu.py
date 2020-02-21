import pandas as pd
import numpy as np
import random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from Joueur import Joueur
from Croupier import Croupier
from JeuDeCarte import JeuDeCarte
from tkinter import *



class Jeu :

    michel=Joueur()
    croupier1=Croupier()
    jeu1 = JeuDeCarte()  
    jeu2 = JeuDeCarte()
    
    def __init__(self, root):
        self.root= root
    
    # fenetre = Tk()
    # fenetre.title("BlackJack")
    # fenetre.minsize(640,480)
    # fenetre.geometry("640x480+300+150")  
    
    

    #verification singleton
    # print(jeu1)    
    # print(jeu2)
    

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

    def affiche_mains_points (self,main_j,main_c,root) :
        # print("\n")
        # print ('main joueur: ',main_j)
        # print ('main croupier: ',main_c)
        # print('total joueur : ',self.total_main(main_j))
        # print('total croupier : ',self.total_main(main_c))
        # print('\n')
        label3 = Label(root,text=str(main_j))
        label4 = Label(root,text=str(main_c))
        label5 = Label(root,text=str(self.total_main(main_j)))
        label6 = Label(root,text=str(self.total_main(main_c)))
        label3.pack()
        label4.pack()
        label5.pack()
        label6.pack()

    def nouvelle_carte(self):
        messagebox = messagebox.askyesno("voulez vous une carte (o/n) ?")
        
    def ass (self,main, total) :

        for i,j in main.items() :
            if j==11 and total>21:
                main[i]=1
        return main

    def blackjack (self,main,total) :
        if len(main)==2 and total==21 :
            return True     

    def jeu(self,root):           
        
        
        
        replay='o'

        while replay=='o' :
            mn=self.main(self.michel,self.croupier1,self.jeu1)
            reste_carte=mn[2]
            
            
            label0 = Label(root, text="Tirage : ")
            label0.pack()
            label1 = Label(root,text=str(mn[0]))
            label1.pack()
            
            
            
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
                self.affiche_mains_points(main_j,main_c,root)

            elif b :        
                print('Courtier : BlackJack !!!!!!!')  
                self.affiche_mains_points(main_j,main_c,root)
                
            else:        

                while total_croupier<17 or total_joueur<21 or nouvellecarte=='o':
                    

                    if total_joueur<21 or nouvellecarte =='o':
                        
                        
                        
                        nouvellecarte=input("voulez vous une carte (o/n) ?")   
                        
                        # label2 = Label(fenetre,text = "voulez vous une carte (o/n) ?")
                        # label2.pack()
                        
                            
                        if nouvellecarte == 'o' :
                            main_j = self.tirer_nouvelle_carte(mn[0],reste_carte)
                            total_joueur = self.total_main(main_j)
                            main_j=self.ass(main_j,total_joueur)
                            total_joueur = self.total_main(main_j)
                            if total_joueur>=21 :
                                nouvellecarte='n'
                            print('main joueur : ',main_j,)
                            print('\n')
                        else :
                            main_j = mn[0]

                            

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

                self.affiche_mains_points(main_j,main_c,root)
                #messagebox = messagebox.askyesno('Voulez vous rejouer ?')
                #entrer2 = Entry(fenetre,text = 'voulez vous rejouer ? o/n',with = 1)
                #entrer2.pack()
                replay=input('voulez vous rejouer ? o/n')

            # self.fenetre.mainloop()