from tkinter import *

root = Tk()

root.title("Canavas")
root.geometry("400x400")
canavas_widget = Canvas(root, width = 400, height= 400)
canavas_widget.pack()
canavas_widget.create_line(0, 10, 400, 400)
canavas_widget.create_rectangle(20, 20, 300, 300, fill = "pink")
# canavas_widget.create_line(0, 400, 0, 0)
canavas_widget.create_text(200, 100, text = "Canavas IDLE in Canavas")
canavas_widget.create_oval(100, 100, 200, 300)

root.mainloop()