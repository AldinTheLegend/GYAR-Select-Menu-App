import tkinter as tk
import tempfile, base64, zlib

class MyGUI:
    
    def __init__(self):
        root = tk.Tk()
        ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
            'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
 
        _, ICON_PATH = tempfile.mkstemp()
        with open(ICON_PATH, 'wb') as icon_file:
            icon_file.write(ICON) #kod jag snodde från python forum

        root.title("")
        root.iconbitmap(default=ICON_PATH)
        root.overrideredirect(True)

        Lb = tk.Listbox(master=root)
        options = ["option1", "option2", "option3"]
        for i in range(len(options)):
            Lb.insert(i, options[i])
        Lb.pack()

        root.mainloop()

MyGUI()

