import tkinter as tk 
from tkinter import *
import os

path = "C:\\Users\\aldin.jusufagic\\Pictures\\Saved Pictures" #/home/raspberry/Pictures

class MyGUI:
    def __init__(self):
        root = tk.Tk()
        root.title("")
        root.overrideredirect(True)
        
        font_path = "avenir-heavy_QYJA9/Avenir Heavy.ttf"
        custom_font = tk.font.Font(family="avenir", size=12, file=font_path)

        Lb = tk.Listbox(master=root, bd=0, font=custom_font)
        options = os.listdir(path)
        for i in range(len(options)):
            Lb.insert(i, options[i])
        Lb.pack()

        root.mainloop()
MyGUI()

