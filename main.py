import tkinter as tk
from tkinter import *
import os
import subprocess
from PIL import Image, ImageFont, ImageDraw

pathToGames = "/home/raspberry/Downloads/ROMGames" #C:\\Users\\aldin.jusufagic\\Pictures\\Saved Pictures
pathToEmulator = "/snap/bin/visualboyadvance-m"


def callBack(event):

    index = event.widget.curselection()
    selectedItem = event.widget.get(index)
    command = [pathToEmulator, "--fullscreen", selectedItem, "2/dev/null"]
    subprocess.call(command)

class MyGUI:

    def __init__(self):

         root = tk.Tk()
         root.title("GameList")
#        root.configure(bg=" ")
         #root.overrideredirect(True)
         root.eval('tk::PlaceWindow . center')

        #font_path = os.getcwd() + "/avenir-heavy_QYJA9/Avenir Heavy.ttf"
         games = []
         options = os.listdir(pathToGames)
         for i in range(len(options)):
             games.insert(i, options[i])
         gamelist = tk.Variable(value=games)

         lb = tk.Listbox(master=root, listvariable=gamelist, selectmode='single', bd=0, fg='#222222')
         lb.pack()
         lb.bind('<<ListboxSelect>>', callBack)

         root.mainloop()

MyGUI()

