import tkinter as tk
from tkinter import *
import os
import subprocess
from PIL import Image, ImageTk
import requests
from io import BytesIO

#pathToGames = "/home/raspberry/Downloads/ROMGames" #C:\\Users\\aldin.jusufagic\\Pictures\\Saved Pictures
#pathToEmulator = "/snap/bin/visualboyadvance-m"
#games = []
#     options = os.listdir(pathToGames)
#     for i in range(len(options)):
#        games.insert(i, options[i])
#    gamelist = tk.Variable(value=games)
#
#callback
#index = event.widget.curselection()
#    selectedItem = event.widget.get(index)
#    command = [pathToEmulator, "--fullscreen", selectedItem, "2/dev/null"]
#    subprocess.call(command)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ga,eList")
        self.initialize()

    def initialize(self):
        height = 270
        width = 308
        #self.overrideredirect(True)
        self.center_window(width=width, height=height)

        background_path = 'bakcground.png'

        original_img = Image.open(background_path)
        self.image = ImageTk.PhotoImage(original_img)
    
        background_label = tk.Label(self, image=self.image)

        #content = tk.Frame(self)
        gamesIcon = tk.Button(background_label, text='Games', height=8, width=20, command=lambda: self.clear(windowIndex=2))
        webbIcon = tk.Button(background_label, text= 'Webb', height=8, width=20)
        filesIcon = tk.Button(background_label, text="Files", height=8, width=20)
        settingsIcon = tk.Button(background_label, text='Settings', height=8, width=20)

        background_label.columnconfigure(0, pad=4)
        background_label.columnconfigure(1, pad=4)
        background_label.rowconfigure(0, pad=4)
        background_label.rowconfigure(1, pad=4) #lägger avstånd mellan knapparna

        background_label.grid(column=0, row=0, columnspan=2, rowspan=2)
        gamesIcon.grid(column=0, row=0)
        webbIcon.grid(column=1, row=0)
        filesIcon.grid(column=0, row=1)
        settingsIcon.grid(column=1, row=1) #placering av allt
        
    def clear(self, windowIndex):
        for widget in self.winfo_children():
            widget.destroy()

        if windowIndex == 1:
            self.initialize()
        elif windowIndex == 2:
            self.openGameMenu()

    def openGameMenu(self):
        self.geometry("1920x1080")
        self.center_window(1920, 1080)
        
        self.addBackgroundToGamesWindow()
        
    def addBackgroundToGamesWindow(self):
        background_path = 'bakcground.png'

        original_img = Image.open(background_path)
        self.image = ImageTk.PhotoImage(original_img)
    
        background_label = tk.Label(self, image=self.image)
        background_label.pack(fill="both", expand=True)
        self.addButtonsToBackground(background_label=background_label)

    def addButtonsToBackground(self, background_label):
        games = ["Pokemon FireRed", "Super Mario Bros.", "Pokemon LeafGreen", "Tetris", "The Legend Of Zelda", "sex", "sju"]

        rows = 3  # Ceiling division to get the number of rows
        columns = 7
        for i in range(columns):
            background_label.columnconfigure(i, weight=1, minsize=0)
        for i in range(rows):
            background_label.rowconfigure(i, weight=1, minsize=0)
    
        for i, game in enumerate(games):
            row, col = divmod(i, columns)  # räknar ut current row och column
    
            button_frame = tk.Frame(background_label, background="#222222")
            button_frame.grid(row=row, column=col, padx=10, pady=10)  # skapa frames för knappar

            #gameArt = ImageTk.PhotoImage(self.getGameArtWork(game=game))
            self.pic = self.getGameArtWork()

            button = tk.Button(button_frame, height=180, width=200, image=self.pic, relief=RIDGE, bd=5)
            button.image = self.pic  
            button.pack()
    
            game_label = tk.Label(button_frame, text=game, background="#222222", foreground="white")  # skapa text under knappar
            game_label.pack()

    def getGameArtWork(self):

        rqst = requests.get('https://cataas.com/cat')
        imgdata = rqst.content

        originalImage = Image.open(BytesIO(imgdata))

        self.pic = ImageTk.PhotoImage(originalImage)
        return self.pic


    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    app = App()
    app.mainloop()