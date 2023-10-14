import tkinter as tk
import tempfile, base64, zlib


root = tk.Tk()
ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
 
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON) #kod jag snodde från python forum

root.title("")
root.iconbitmap(default=ICON_PATH)
root.overrideredirect(True)

root.geometry()

root.mainloop()