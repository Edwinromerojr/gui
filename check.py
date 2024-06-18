from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("lets learn")
root.iconbitmap('images/logo.ico')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()