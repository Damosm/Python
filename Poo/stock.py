from article import article

class stock :

    stockage=[]

    def __init__(self):
        self.stockage=[]
    

    def getStockage(self):
        return self.stockage
    
    def setStockage(self, stockage):
        self.stockage=stockage
    
    def ajouter(self,article,stock):
        stock.getStockage().append(article)
        return stock
    
    def retirer(self,article,stock):
        stock.getStockage().remove(article)
        return stock