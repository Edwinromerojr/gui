from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("lets learn")
root.iconbitmap('images/logo.ico')
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    # hist, pie
    plt.polar(house_prices)
    plt.show()

my_button = Button(root, text="Graph It!", command=graph)
my_button.pack()

root.mainloop()
