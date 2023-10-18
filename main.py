import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageFont, ImageDraw

path = "/home/raspberry/Pictures" #C:\\Users\\aldin.jusufagic\\Pictures\\Saved Pictures

class MyGUI:
    def __init__(self):
        root = tk.Tk()
        root.title("")
        root.overrideredirect(True)

        #font_path = os.getcwd() + "/avenir-heavy_QYJA9/Avenir Heavy.ttf"
        
        Lb = tk.Listbox(master=root, bd=0)
        options = os.listdir(path)
        for i in range(len(options)):
            Lb.insert(i, options[i])
        Lb.pack()
        
        root.mainloop()
MyGUI()

