from tkinter import *
from PIL import Image, ImageTk

root = Tk()

#for title block
root.title("Photo Viewer")

"""Important Lable options
1. text -- adds text
2. bd - for background
3. fg - for foreground
4. font - for desired font
5. padx, pady -- x and y padding
6. relief - border styling (SUNKEN, RAISED, GROOVE, RIDGE)

"""
root.geometry('500x900')

# picture = PhotoImage(file = "hai.png") ''Not Working in my case''
image = Image.open("hai.png")
picture = ImageTk.PhotoImage(image)
label = Label(image = picture)
label.pack()
root.mainloop()