from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("lets learn")
root.iconbitmap('images/logo.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askokcancel("This is my Popup!", "Hello World!")
    Label(root, text=response).pack()
    # if response == 1:
    #     Label(root, text="You Clicked Yes!").pack()
    # else:
    #     Label(root, text="You Clicked no!").pack()

Button(root, text="Popup", command=popup).pack()


root.mainloop()