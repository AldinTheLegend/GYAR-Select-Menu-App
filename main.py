import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageFont, ImageDraw

pathToGames = "/home/raspberry/Pictures" #C:\\Users\\aldin.jusufagic\\Pictures\\Saved Pictures
pathToEmulator = "/snap/bin/visualboyadvance-m"


def callBack(event):
    print(event.widget.curselection())
    #selection = lb.curselection()
    #print(selection)

class MyGUI:
    def __init__(self):

         root = tk.Tk()
#        root.configure(bg='')
         root.title("")
         root.overrideredirect(True)
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

