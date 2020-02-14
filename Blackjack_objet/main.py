import pandas as pd
import numpy as np
import random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt 
from tkinter import *
from Joueur import Joueur
from Croupier import Croupier
from JeuDeCarte import JeuDeCarte
from Jeu import Jeu
from Interface import *
import django

if __name__ == "__main__":
    pass
    
    partie=Jeu()   
    #fenetre = Tk()
    #interface = Interface(fenetre)

    #interface.mainloop()
    #interface.destroy()
    
    partie.jeu()
    
    