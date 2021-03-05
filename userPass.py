from tkinter import *
def getValues():
	print(userEntry.get())
	print(passEntry.get())

root = Tk()


root.geometry('500x900')


user = Label(text = "UserName")
password = Label(text = "password")
user.grid() # moving to left
password.grid(row = 1) #moving to left 

uservalue = StringVar()
passValue = StringVar()

userEntry = Entry(root)
passEntry = Entry(root)

userEntry.grid(row = 0, column = 1)
passEntry.grid(row = 1, column = 1)
Button(text = "submit", command = getValues).grid()

root.mainloop()