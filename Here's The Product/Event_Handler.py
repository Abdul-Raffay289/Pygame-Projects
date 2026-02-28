from tkinter import *
import tkinter as tk
window = Tk()
window.title('Event Handler')
window.geometry('100x100')
def handle_keypress(event):
    '''Print the character assoociated with keypress'''
    print(event.char) 
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("\nThe button was clicked")
button = Button(text="Click Me")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()