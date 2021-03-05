from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Place Order")
root.geometry("400x400")
scrollbar = Scrollbar(root)
scrollbar.pack(side= RIGHT, fill  = Y)

text = Text(root, yscrollcommand = scrollbar.set)
text.pack()
scrollbar.config(command = text.yview)

root.mainloop()