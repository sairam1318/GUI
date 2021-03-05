from tkinter import *

root = Tk()
root.geometry('500x900')
f1 = Frame(root, bg = 'pink')
f1.pack(side = LEFT)
label = Label(f1, text = "hai All")
label.pack()

f2 = Frame(root, bg = 'grey')
f1.pack(side = "top")
label = Label(f2, text = "hai All")
label.pack()

root.mainloop()