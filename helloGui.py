from tkinter import *

sai_root = Tk() #creates a basic gui window

#geometrty = width x Height
sai_root.geometry("400x400")
#setting minimum size 
sai_root.minsize(200, 200)
#setting max size
sai_root.maxsize(1200, 800)

text = Label(text = "Hai ALL")
text.pack() #unless we pack it, it will not be displayed

sai_root.mainloop()


