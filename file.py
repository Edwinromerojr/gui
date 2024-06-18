from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import os

root = Tk()
root.title("lets learn")
root.iconbitmap('images/logo.ico')


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir= os.path.join(os.getcwd(), 'images'), title="Select A File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()