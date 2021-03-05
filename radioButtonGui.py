from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
def name():
	tmsg.showinfo("Best Friend", "Selected option is {}".format(var.get()))

root.title("Place Order")
root.geometry("400x400")

var = StringVar()
var.set("Radio")

label = Label(root, text = "Who is your best friend? ").pack()
radio = Radiobutton(root, text = "Vamsi", variable = var, value = "Vamsi").pack(anchor = "w")
radio = Radiobutton(root, text = "Pranay", variable = var, value = "Pranay").pack(anchor = "w")
#if we dont give value, all radio buttons default get selectd
#varaible is to say that, we are assigning the value of radiobutton to var varibale


Button(text = "Submit", command = name).pack()

root.mainloop()