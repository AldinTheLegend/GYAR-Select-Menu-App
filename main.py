import tkinter as tk
import tempfile, base64, zlib

class MyGUI:
    
    def __init__(self):
        root = tk.Tk()
        root.title("")
        root.overrideredirect(True)

        Lb = tk.Listbox(master=root)
        options = ["option1", "option2", "option3"]
        for i in range(len(options)):
            Lb.insert(i, options[i])
        Lb.pack()

        root.mainloop()

MyGUI()

