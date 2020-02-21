import pandas as pd
import numpy as np
import random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from Joueur import Joueur
from Croupier import Croupier
from Singleton import InheritableSingleton


class JeuDeCarte (InheritableSingleton):

    jdc ={}

    def getJdc(self):
        return self.jdc

    def setJdc(self, jdc):
        self.jdc = jdc

    def __init__ (self) :
        
        super().__new__(InheritableSingleton)
        jdc={}
        type=['coeur','carreau','trefle','pique']
        nom=['as de ','2 de ','3 de ','4 de ','5 de ','6 de ','7 de ','8 de ','9 de ','10 de ','valet de ','dame de ','roi de ']
        valeur=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        for i in type :
            for j,k in zip(nom,valeur) :
                jdc[j+i]=k
                self.jdc=jdc

    