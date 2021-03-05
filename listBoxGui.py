from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Place Order")
root.geometry("400x400")

scrollbar = Scrollbar(root)
scrollbar.pack(side= RIGHT, fill  = Y)

lbx = Listbox(root, yscrollcommand = scrollbar.set)
# lbx.insert(1, "firstItem")
# lbx.insert(2, "secondItem")
# lbx.insert(3, "thirdItem")
# lbx.insert(4, "fourthItem")
# lbx.insert(ACTIVE, 0)

for i in range(300):
	lbx.insert(END, "Item {}".format(str(i)))
	i += 1

scrollbar.config(command = lbx.yview)
#to attach the scroll bar to the list, we need to configure it 
lbx.pack(fill = BOTH)
root.mainloop()