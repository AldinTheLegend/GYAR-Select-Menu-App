import tkinter as tk
from tkinter import *
import os
import subprocess

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
        self.wm_attributes('-transparentcolor', 'red') #allt som är rött blir genomskinligt
        self.config(background='red')
        self.initialize()

    def initialize(self):
        height = 270
        width = 308

        self.center_window(width=width, height=height)

        content = tk.Frame(self, background='red')
        gamesIcon = tk.Button(content, text='Games', height=8, width=20, command=lambda: self.clear(windowIndex=1))
        webbIcon = tk.Button(content, text= 'Webb', height=8, width=20)
        filesIcon = tk.Button(content, text="Files", height=8, width=20)
        settingsIcon = tk.Button(content, text='Settings', height=8, width=20)

        content.columnconfigure(0, pad=4)
        content.columnconfigure(1, pad=4)
        content.rowconfigure(0, pad=4)
        content.rowconfigure(1, pad=4) #lägger avstånd mellan knapparna

        content.grid(column=0, row=0, columnspan=2, rowspan=2)
        gamesIcon.grid(column=0, row=0)
        webbIcon.grid(column=1, row=0)
        filesIcon.grid(column=0, row=1)
        settingsIcon.grid(column=1, row=1)
        
    def clear(self, windowIndex):
        for widget in self.winfo_children():
            widget.destroy()

        if windowIndex == 1:
            self.openGameMenu()
        elif windowIndex == 2:
            self.initialize()

    def openGameMenu(self):
        self.geometry("1920x1080")
        height = 1080
        width = 1920
        self.center_window(width=width, height=height)

        frame = tk.Frame(master=self, background='green', width=self.winfo_width(), height=self.winfo_height())
        j = 0
        #for column in frame.grid_info():
            #j += 1
            #frame.columnconfigure(j, pad=4)

        frame.rowconfigure(0, pad=4)
        frame.rowconfigure(1, pad=4)

        frame.grid(column=0, row=0)


        games = ["apple", "orange", "banana", "m", "sdad", " asda", "taerf", "bitch", "apple2", "orange2", "banana2", "m2", "sdad2", " asda2"]

        rows = -(-len(games) // 7)  # Ceiling division to get the number of rows
        columns=7  # Maximum 7 columns

        for i, game in enumerate(games):
            print(i)
            button = tk.Button(frame, text=game, height=8, width=20)
            row, col = divmod(i, columns)
            button.grid(row=row, column=col, )#padx=5, pady=5)

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    app = App()
    app.mainloop()