import pandas as pd
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

df = pd.read_table('C:/Users/utilisateur/Documents/Python/Python/heart.txt',sep='\t',header=0)

"""
#10 premieres lignes
print(df.head(10))
#10 dernieres lignes
print(df.tail(10))

#noms des colonnes
print(df.columns)

#type colonnes
print(df.dtypes)

#infos donnees
print(df.info)
"""
#print(df['age'])
"""
a = df.hist(column='age')
b = df.boxplot(column='age')
c= df.plot.scatter(x='age',y='taux_max')
d = df['sexe'].value_counts().plot.pie()
"""

#plt.show(d)
#####################################
#ex1

a = pd.read_csv('C:/Users/utilisateur/Documents/Python/Python/Automobile_data.csv',sep=',',header=0)

#########################
#ex2


#print(a[['company','body-style',"price"]][a['price']==a['price'].max()])
#ou
#print(a.loc[a['price']==a['price'].max()])
#########################""
#ex3

#print(a.loc[a['company']=='toyota'])

########################################"
#ex4
#b = a['company'].value_counts().plot.pie()
#plt.show(b)

##########################################
#ex5

#b = a.loc[:,['company','price']].groupby('company').max()
#print(b)
#b.plot(kind='bar')
#plt.show()
####################################################"
#ex6

#b = a.loc[:,['company','average-mileage']].groupby('company').mean()
#print(b)
#b.plot(kind='bar')
#plt.show()
#######################################################
#ex7
b = a.sort_values(by='price')
print(b)

