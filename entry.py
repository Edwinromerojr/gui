from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=50)
e.pack()
#placeholder
e.insert(0, "Enter Your Name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg='blue', bg="red")
myButton.pack()

root.mainloop()