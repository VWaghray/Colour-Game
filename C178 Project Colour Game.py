from tkinter import *
import random
root = Tk()
root.geometry("500x500")
root.title("Colour Game")

label = Label(root, font=("Gigi",50,"bold"))
label.place(relx=0.5,rely=0.5,anchor=CENTER)

class game:
    def __init__(self):
        score = 0
        self.__score = score
    def updateGame(self):
        colours=["Red","Blue","Green","Yellow","Crimson","Purple","Pink"]
        self.text = colours
        self.colour= ["red","blue","green","yellow","crimson","purple","pink"]
        self.random_number_for_text = random.randint(0, 6)
        self.random_number_for_colour = random.randint(0, 6)
        label["text"] = self.text[self.random_number_for_text]
        label["fg"] = self.colour[self.random_number_for_colour]
        
obj = game()

btn = Button(root, text = "Start", command = obj.updateGame, bg = "green", fg = "brown", relief=FLAT,font=("Gigi",20))
btn.place(relx=0.7,rely=0.7) 

root.mainloop()
        
