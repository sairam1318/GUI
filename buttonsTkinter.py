from tkinter import *

def hello():
	print("hello")

root = Tk()
root.geometry('500x900')
f1 = Frame(root, bg = 'pink', borderwidth = 7)
f1.pack(side = LEFT, anchor = "nw")

b = Button(f1, text = "ItsAButton", fg = "red", command = hello)
b.pack()

root.mainloop()