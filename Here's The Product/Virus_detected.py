from tkinter import *
import tkinter as tk
from tkinter import messagebox
window = Tk()
window.geometry('200x200')
def msg():
    messagebox.showwarning("Alert", "Virus Detected")
btn = Button(window, text="Scan For Virus", command = msg)
btn.place(x=40, y=80)
window.mainloop()