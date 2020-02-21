import pandas as pd
import numpy as np
import random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class Croupier :

    #nom=''
    mainn={}

    def getMain(self):
        return self.mainn

    def setMain(self, mainn):
        self.mainn = mainn

    def __init__ (self) :
        self.mainn={}
