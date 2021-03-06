import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def create_image (name,h,w) :
    img = np.ones((h, w, 3))
    rouge=[1,0,0]
    cyan=[0,1,1]
    jaune=[1,1,0]
    vert=[0,1,0]
    
    p=0
    x=h
    y=h//2
    s=w//2
    u=w//2
    t=h//2
    while p<=w :
        img[:p,p:x]=rouge
        img[t:,s:u]=cyan
        img[y:t,u:]=jaune
        img[p:x,:p]=vert
        s=s-1
        u=u+1
        t=t+1
        p=p+1
        x=x-1
        y=y-1   
        
    
    plt.imsave(name, img)

    return img
    
a=create_image("matricecolor.png",200,200)

#print(a)
plt.imshow(a)
plt.show()


"""


def inversion (img) :
    
    image1=np.zeros((20,20,3))
    image1=1-img[:,:,:]
    return image1

#b=inversion(a)
#plt.imshow(b)
#plt.show()
"""
def separation (img) :
    n = img.shape
    img_rouge = np.zeros((n[0], n[1], 3))
    img_vert = np.zeros((n[0], n[1], 3))
    img_bleu = np.zeros((n[0], n[1], 3))
    
    
    """
    for i in range(img.shape[0]) :
        for j in range(img.shape[1]) :
            #print(img_rouge[i])
            img_rouge[i,j,0]=img[i,j,0]
    """
    img_rouge[:,:,0]=img[:,:,0]
    img_vert[:,:,1]=img[:,:,1]
    img_bleu[:,:,2]=img[:,:,2]

    return img_rouge

b=separation(a)
plt.imshow(b)
plt.show()
"""
#########################################################################
mpimg.imread('C:/Users/utilisateur/Documents/Python/Python/IA.png')
a = pl.imread('c:/Users/ThinkCentre/Documents/Python/Coline.PNG')
#print(a.shape)
b=a

#b=a[:,:,0]


rouge=[1,0,0]
vert= [0,1,0]
bleu= [0,0,1]

c= np.zeros((10,10,3))
c[:,:]=rouge
"""
"""
def crea(c):
    rouge=[1,0,0]
    
    #im = np.copy(img_orig) # On fait une copie de l'original
    for i in enumerate(c):
        for j in enumerate(i):
            #r, v, b = im[i, j]
            #im[i, j] = (r, 0,0)
            #c[i,j]=rouge
            #print(j)
            for k in enumerate(j) :
                print(k)
 
    return c


def transform (a) :
    
    c= np.copy(a)

    for i in range(c.shape[0]) :
        for j in range(c.shape[1]) :

            #print(c[i,j])
            if np.array_equal(c[i,j], rouge) == True :
                c[i,j]=bleu           
        
    
    return c

def rgb2gray(img):
    return np.dot(img[...,:3], [0.299, 0.587, 0.144])

#c= transform(c)
#c.getpixel((0,0))[0]
c= rgb2gray(a)

print(b)
mpimg.imsave('c:/Users/ThinkCentre/Documents/Python/Coline_modif.PNG',b)

pl.imshow(c)
pl.show()
                
            

        
    
    

b=separation(a)
plt.imshow(b)
plt.show()

"""
