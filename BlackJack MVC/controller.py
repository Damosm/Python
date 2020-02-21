
import tkinter as Tk 
from view import View



class Controller:
    def __init__(self):
        self.root = Tk.Tk()
        self.root.title("BlackJack")
        self.root.minsize(400,400)
        
        self.root.geometry("400x400+150+150")        
        self.view = View(self.root)

    def run(self):   
        
        self.root.mainloop()