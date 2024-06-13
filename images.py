from tkinter import *
from PIL import Image, ImageTk

img = Image.open('logo.jpg')

img.save('logo.ico')

root = Tk()
root.title("lets learn")
root.iconbitmap('logo.ico')

my_img = ImageTk.PhotoImage(Image.open("logo.jpg"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()