#!/usr/bin/env python
# ScrotGUI - a graphical user interface for the program "Scrot"
# Author: Nikos-Nikitas
# GitHub: nikosnikitas

from tkinter import *
import subprocess

class ScrotGUI:
    def __init__(self):
        self.win = Tk()
        self.win.title("ScrotGUI")
        self.lbl = Label(text="A GUI for the program Scrot by nikosnikitas v.0.1", font="FreeSans")
        self.fs_btn = Button(text="Capture Full Screen", command=self.__full_screenshot)
        self.rs_btn = Button(text="Capture Specific Region", command=self.__region_screenshot)
        
        self.lbl.pack()
        self.fs_btn.pack()
        self.rs_btn.pack()
    
    def __run(self):
        self.win.mainloop()

    def __full_screenshot(self):
        subprocess.call("scrot", shell=True)

    def __region_screenshot(self):
        subprocess.call("scrot -s", shell=True)

if __name__ == '__main__':
    sg = ScrotGUI()
    sg.__run()

