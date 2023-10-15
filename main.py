import tkinter as tk
import tempfile, base64, zlib
import os

path = "/home/raspberry/Pictures"
class MyGUI:
    def __init__(self):
        root = tk.Tk()
        root.title("")
        root.overrideredirect(True)

        Lb = tk.Listbox(master=root)
        options = os.listdir(path)
        for i in range(len(options)):
            Lb.insert(i, options[i])
        Lb.pack()

        root.mainloop()
MyGUI()

