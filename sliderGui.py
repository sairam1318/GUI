from tkinter import *
import tkinter.messagebox as tmsg


def getDollar():
	tmsg.showinfo("Amount credited", f"{mySlider.get()} is credited to you")


root = Tk()
root.geometry("600x600")
root.title("My Slider")

label = Label(text = "How many do you want?").pack()
mySlider = Scale(root, from_= 0, to = 5, orient = HORIZONTAL, tickinterval = 2)
mySlider.set(2)
mySlider.pack()

Button(root, text = "submit", command = getDollar).pack()
root.mainloop() 