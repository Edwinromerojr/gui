from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("lets learn")
root.iconbitmap('images/logo.ico')

def open():
    global my_img
    top = Toplevel()
    top.title("My Second Window")
    top.iconbitmap('images/logo.ico')
    my_img = ImageTk.PhotoImage(Image.open("images/jslogo.jpg"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()


btn = Button(root,text="Open Second Window", command=open).pack()


root.mainloop()