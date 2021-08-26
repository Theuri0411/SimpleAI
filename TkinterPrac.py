from tkinter import *

root = Tk()
root.title(input("ENTER TITTLE: "))
myLabel = Label(root, text=input("ENTER MESSAGE: "), font=("serif", 16), background="black", foreground="white",)

myLabel.pack(anchor="w")

root.mainloop()
