import tkinter as Tk 
from Joueur import Joueur
from Croupier import Croupier
from JeuDeCarte import JeuDeCarte

import random
from tkinter import messagebox
import controller as ct


class View:
    
    michel=Joueur()
    croupier1=Croupier()
    jeu1 = JeuDeCarte()  
    jeu2 = JeuDeCarte()
    
    def __init__(self, root):
        
        
        replay= True

        while replay== True :
            mn=self.main(self.michel,self.croupier1,self.jeu1)
            reste_carte=mn[2]
            
            
            label0 = Tk.Label(root, text="Tirage : ")
            label0.pack()
            label1 = Tk.Label(root,text=str(mn[0]))
            label1.pack()
            
            
            
            
            total_joueur = self.total_main(mn[0])
            total_croupier = self.total_main(mn[1])
            nouvellecarte=True
            main_j=mn[0]
            main_c=mn[1]

            a=self.blackjack(main_j,total_joueur)
            b=self.blackjack(main_c,total_croupier)

            if a :                
                self.blackjackJ()  
                replay= self.rejouer()
                
                if replay == False : 
                    root.destroy()
                else :
                    root.destroy()
                    c = ct.Controller()
                    c.run()

            elif b :        
                self.blackjackC()
                replay= self.rejouer()
                
                if replay == False : 
                    root.destroy()
                else :
                    root.destroy()
                    c = ct.Controller()
                    c.run()
                
            else:        

                while total_croupier<17 or total_joueur<21 or nouvellecarte==True:
                    

                    if total_joueur<21 or nouvellecarte ==True:
                        
                        
                        nouvellecarte = self.nouvelle_carte()
                        
                        if nouvellecarte == True :
                            main_j = self.tirer_nouvelle_carte(mn[0],reste_carte)
                            total_joueur = self.total_main(main_j)
                            main_j=self.ass(main_j,total_joueur)
                            total_joueur = self.total_main(main_j)
                            if total_joueur>=21 :
                                nouvellecarte='n'
                            label2 = Tk.Label(root, text="Main Joueur : ")
                            label2.pack()
                            label3 = Tk.Label(root,text=str(main_j))
                            label3.pack()
                            
                        else :
                            main_j = mn[0]

                            

                        if total_croupier <17 :
                            main_c=self.tirer_nouvelle_carte(mn[1],reste_carte)
                            total_croupier = self.total_main(main_c)
                            main_c=self.ass(main_c,total_croupier)
                        else :
                                main_c=mn[1]   

                        if total_croupier>=17 and nouvellecarte != True : 
                            break
                    else :
                        break

                self.affiche_mains_points(main_j,main_c,root)
                
                replay= self.rejouer()
                
                if replay == False : 
                    root.destroy()
                else :
                    root.destroy()
                    c = ct.Controller()
                    c.run()
        
        
        
        
        
        
    
        
    
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
        
        label3 = Tk.Label(root,text="Main Joueur : ")
        label4 = Tk.Label(root,text=str(main_j))
        label5 = Tk.Label(root,text="Main Croupier : ")
        label6 = Tk.Label(root,text=str(main_c))
        label7 = Tk.Label(root,text="Total Joueur : ")
        label8 = Tk.Label(root,text=str(self.total_main(main_j)))
        label9 = Tk.Label(root,text="Total Croupier : ")
        label10 = Tk.Label(root,text=str(self.total_main(main_c)))
        label3.pack()
        label4.pack()
        label5.pack()
        label6.pack()
        label7.pack()
        label8.pack()
        label9.pack()
        label10.pack()

    def nouvelle_carte(self):
        a = messagebox.askyesno("Nouvelle Carte","Voulez vous une carte ?")
        return a
    
    def rejouer(self):
        a = messagebox.askyesno("Continuer","Voulez vous rejouer ?")
        return a
    
    def blackjackJ(self):
        a = messagebox.showinfo("Joueur","BlackJack !!!!!")
        
    
    def blackjackC(self):
        a = messagebox.showinfo("Croupier","BlackJack !!!!!")
        
    
    def ass (self,main, total) :

        for i,j in main.items() :
            if j==11 and total>21:
                main[i]=1
        return main

    def blackjack (self,main,total) :
        if len(main)==2 and total==21 :
            return True     
