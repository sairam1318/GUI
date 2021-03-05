from tkinter import *
def create(event):
	print("event location is {} {}".format(event.x, event.y))


root = Tk()

root.title("Event handling")
root.geometry("600x660")
button = Button(root, text = "click me")
button.pack()

button.bind('<Button-1>', create)
button.bind('<Double-1>', quit)


root.mainloop()