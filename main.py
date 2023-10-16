import tkinter as tk
import tempfile, base64, zlib
import os

path = "C:\\Users\\aldin.jusufagic\\Pictures\\Saved Pictures" #/home/raspberry/Pictures
class MyGUI:
    def __init__(self):
        root = tk.Tk()
        root.title("")
        root.overrideredirect(True)
        
        Lb = tk.Listbox(master=root, bd=0)
        options = os.listdir(path)
        for i in range(len(options)):
            Lb.insert(i, options[i])
        Lb.pack()

        root.mainloop()
MyGUI()

