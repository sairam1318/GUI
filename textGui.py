from tkinter import *

root = Tk()

root.title("Some Random stuff")

label = Label(text = '''he result set will contain one row for each index giving index sequence, index name and flag \n
	indicating whether the index is unique or not.''', bg = 'pink', fg = 'blue', padx = '190',pady = '400', font = ('Verdana', 20, "bold"), 
	borderwidth = 10, relief = SUNKEN)
#important pack options
#anchor = nw
#side = top, bottom, left, right 
#fill = X, Y
#padx and pady
label.pack()


root.mainloop()