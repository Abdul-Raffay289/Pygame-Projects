from tkinter import *
import tkinter as tk
from tkinter import messagebox
window = Tk()
window.geometry('200x200')
def msg():
    response = messagebox.askquestion("Question Box", "Do You Want To Continue?")
    if response == 'yes':
        print("Continuing")
    else:
        print("Stopping")
        window.destroy()
msg()
window.mainloop()