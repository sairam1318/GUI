from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
def random():
	print("Dude, its just a try")
	a = tmsg.showinfo("Help", "I will help you")
	print(a)

def rate():
	print("Rate")
	value = tmsg.askquestion("Hey User...", "Was your Experience Good? ")
	if value == 'yes':
		msg = "Great"
	else:
		msg = "Nope"
	tmsg.showinfo("Experience", msg)

def divya():

	val = tmsg.askretrycancel("Marry Divya", "Sorry, Divya is already Married")
	if val:
		print("okay")
	else:
		print("okay")



root.title("Menu File")
root.geometry("400x400")

myMenu = Menu(root)

anotherMenu = Menu(myMenu, tearoff = 0)
anotherMenu.add_command(label = "name", command = random)
anotherMenu.add_command(label = "age", command = rate)
anotherMenu.add_separator()
anotherMenu.add_command(label = "Marry Divya", command = divya)
anotherMenu.add_command(label = "profession", command = random)


root.config(menu = myMenu)

myMenu.add_cascade(label = "file", menu = anotherMenu)

# myMenu.add_command(label = "PrintRandomStuff", command = random)
# myMenu.add_command(label = "Exit", command = quit)

root.mainloop()