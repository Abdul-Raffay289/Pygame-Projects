from tkinter import *
import tkinter as tk
from datetime import date
import datetime
window = Tk()
window.title('Demo Screen')
window.geometry('400x500')
lbl = Label(text="Hey! There", fg='White', bg="#072F5F", height=1, width=300)
name_lbl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()
def display():
    name = name_entry.get()
    global message
    message = "Welcome to the application! \nToday's date is: "
    greet = "Hello "+name+"\n"
    textbox.insert(END, message)
    textbox.insert(END, greet)
    textbox.insert(END, date.today())
textbox = Text(height = 3)
btn = Button(text="Begin", fg='White', bg="#1216A0", height=1, command=display)

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
textbox.pack()

window.mainloop()